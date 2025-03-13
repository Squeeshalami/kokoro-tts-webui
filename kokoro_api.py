import io
import torch
import numpy as np
import soundfile as sf
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from kokoro import KPipeline

#Global Pipeline Cache
pipeline_cache = {}

class TTSRequest(BaseModel):
    text: str
    voice: str = 'af_heart'
    language: str = 'a'
    speed: float = 1.0

app = FastAPI()
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")


@app.post("/generate")
def generate_tts(request: TTSRequest):
    """
    Takes in a JSON payload containing:
    {
      "text":  "The text you want to synthesize",
      "voice": "The desired voice name (optional)",
      "language": "The language code (optional)",
      "speed": "The speed of the speech (optional)"
    }
    and returns a WAV audio file as a streaming response.
    """
    # Check if pipeline is already cached
    global pipeline_cache
    cache_key = f"{request.language}_{device}"

    if cache_key not in pipeline_cache:
        pipeline_cache[cache_key] = KPipeline(lang_code=request.language, device=device)
        print(f"Created new pipeline for language: {request.language}")

    pipeline = pipeline_cache[cache_key]

    # A) Run pipeline => yields segments (text, phonemes, audio_array)
    segments = pipeline(
        request.text,
        voice=request.voice,
        speed=request.speed,
        split_pattern=r'\n+'
    )

    # B) Accumulate all audio segments in memory
    all_segments = []
    for i, (graphemes, phonemes, audio_array) in enumerate(segments):
        print(f"Segment {i}: {graphemes[:50]}...")
        all_segments.append(audio_array)

    if not all_segments:
        # No audio generated, return empty or handle gracefully
        # Return an empty WAV or an error response
        return StreamingResponse(io.BytesIO(b""), media_type="audio/wav")

    # C) Concatenate into one long audio array
    combined_audio = np.concatenate(all_segments, axis=0)

    # D) Write to an in-memory buffer
    wav_buffer = io.BytesIO()
    sf.write(wav_buffer, combined_audio, samplerate=24000, format="WAV")
    wav_buffer.seek(0)

    # E) Return as a streaming response
    return StreamingResponse(
        wav_buffer,
        media_type="audio/wav",
        headers={"Content-Disposition": "attachment; filename=output.wav"}
    )
