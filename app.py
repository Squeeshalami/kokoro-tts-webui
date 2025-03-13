import gradio as gr
import requests
from voices import voices, language
import uvicorn
import threading
import time
from kokoro_api import generate_tts, TTSRequest
from utils import get_language_code


API_PORT = 12345

def run_fastapi():
    uvicorn.run("kokoro_api:app", host="127.0.0.1", port=API_PORT)

# Start FastAPI in a separate thread
fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
fastapi_thread.start()

# Wait a moment for the server to start
time.sleep(2)

def generate_speech(text, voice, language, speed):
    # Prepare the request payload
    payload = {
        "text": text,
        "voice": voice,
        "language": get_language_code(language),
        "speed": speed
    }
    
    # Make POST request to your local FastAPI endpoint
    response = requests.post(f"http://localhost:{API_PORT}/generate", json=payload)
    
    # Check if request was successful
    if response.status_code == 200:
        # Save the audio to a temporary file
        audio_data = response.content
        return audio_data
    else:
        raise gr.Error(f"Error generating speech: {response.status_code}")


# Create voice options grouped by language
voice_choices = []
for lang_code in language:
    # Filter voices for current language code
    lang_voices = [v for v in voices if v.startswith(get_language_code(lang_code))]
    if lang_voices:
        voice_choices.extend(lang_voices)

# Create the Gradio interface
demo = gr.Interface(
    fn=generate_speech,
    inputs=[
        gr.Textbox(
            label="Text to speak",
            placeholder="Enter the text you want to convert to speech...",
            lines=5
        ),
        gr.Dropdown(
            choices=voice_choices,
            value="af_heart",
            label="Voice"
        ),
        gr.Dropdown(
            choices=language,
            label="Language"
        ),
        gr.Slider(
            minimum=0.5,
            maximum=2.0,
            value=1.0,
            step=0.1,
            label="Speed"
        )
    ],
    outputs=gr.Audio(label="Generated Speech"),
    title="Kokoro Text-to-Speech",
    description="Convert text to speech using various voices and languages."
)

if __name__ == "__main__":
    demo.launch()

