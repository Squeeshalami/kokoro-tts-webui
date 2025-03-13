# Simple Kokoro-TTS WebUI

An easy to use Text-to-Speech (TTS) application built with Kokoro-82M, FastAPI, and Gradio.

## Overview

The project consists of:

- An independent FastAPI backend for integration with other applications
- A Gradio web interface for easy interaction

## Kokoro-TTS Features

- **Multiple Languages**: Support for American English, British English, Mandarin Chinese, Spanish, Japanese,    French, Hindi, Italian, and Brazilian Portuguese
- **Diverse Voice Options**: Over 40 different voice options across all supported languages
- **Adjustable Speech Speed**: Control the pace of generated speech

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Squeeshalami/kokoro-tts-webui.git
   cd kokoro-tts-webui
   ```

2. Create and activate a virtual environment:
   ```
   # Linux
   python -m venv .venv
   source .venv/bin/activate
   
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt


4. Install espeak-ng 
   
   For Linux:
   ```
   sudo apt-get install espeak-ng
   ```

   ForWindows:
   ```
   https://github.com/espeak-ng/espeak-ng/releases
   ```
   For more information on windows installation, see:
   https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md

   Note: For Chinese language support, run: `pip install misaki[zh]`
   For Japanese language support, run: `pip install misaki[ja]`

## Usage

### Web Interface

1. Run the Gradio web interface:
   ```
   python app.py
   ```

2. Open your browser and navigate to the URL displayed in the terminal (typically http://127.0.0.1:7860)

3. In the web interface:
   - Enter the text you want to convert to speech
   - Select a voice from the dropdown menu
   - Choose the language
   - Adjust the speech speed if needed
   - Click "Submit" to generate and play the audio

### API Usage

You can also use the TTS functionality programmatically via the API:

1. Start the FastAPI server:
   ```
   # Linux/macOS
   ./start_server.sh
   
   # Windows
   start_server.bat
   ```
   
   Or manually:
   ```
   uvicorn kokoro_api:app --host 127.0.0.1 --port 12345
   ```

2. Send a POST request to the `/generate` endpoint:
   ```python
   import requests

   url = "http://127.0.0.1:12345/generate"
   payload = {
       "text": "Text you want to synthesize",
       "voice": "af_heart",  # See voices.py for available options
       "language": "a",      # Language code (a=American English, etc.)
       "speed": 1.0          # Speech speed (0.5-2.0)
   }

   response = requests.post(url, json=payload)
   
   # Save the audio file
   with open("output.wav", "wb") as f:
       f.write(response.content)
   ```

3. Run the test script to verify functionality:
   ```
   python tests.py
   ```

## Available Voices and Languages

The project supports multiple languages, each with several voice options:

- American English (code: 'a'): af_alloy, af_aoede, af_bella, etc.
- British English (code: 'b'): bf_alice, bf_emma, bm_daniel, etc.
- Mandarin Chinese (code: 'z'): zf_xiaobei, zf_xiaoni, etc.
- Spanish (code: 'e'): ef_dora, em_alex, em_santa
- Japanese (code: 'j'): jf_alpha, jf_gongitsune, jm_kumo, etc.
- French (code: 'f'): ff_siwis
- Hindi (code: 'h'): hf_alpha, hf_beta, hm_omega, hm_psi
- Italian (code: 'i'): if_sara, im_nicola
- Brazilian Portuguese (code: 'p'): pf_dora, pm_alex, pm_santa

For a complete list of available voices, see the `voices.py` file.

## System Requirements

- Python 3.8 or higher
- CUDA-compatible GPU recommended for faster processing (falls back to CPU if unavailable)
- Sufficient disk space for model storage

## Troubleshooting

- If you encounter CUDA out-of-memory errors, try using a smaller batch size or switch to CPU mode.
- For language-specific issues, ensure you've installed the required language packages.
- If the web interface doesn't load, check that both the FastAPI server and Gradio interface are running.
- On Windows, if you get "Access is denied" errors when running the batch file, try running Command Prompt as administrator.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project uses the [Kokoro](https://github.com/hexgrad/kokoro || https://huggingface.co/hexgrad/Kokoro-82M) TTS library developed by Hexgrad. 