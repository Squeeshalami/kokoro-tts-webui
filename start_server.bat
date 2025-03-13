@echo off
REM Windows batch file to start the Kokoro TTS FastAPI server

REM Activate the virtual environment
call .venv\Scripts\activate.bat

SET MODULE_NAME=kokoro_api:app
SET HOST=127.0.0.1
SET PORT=12345

echo Starting FastAPI server on %HOST%:%PORT%

REM Start the uvicorn server
uvicorn %MODULE_NAME% --host %HOST% --port %PORT%

pause