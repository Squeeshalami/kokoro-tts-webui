#!/usr/bin/env bash

source .venv/bin/activate

MODULE_NAME="kokoro_api:app"

HOST="127.0.0.1"
PORT="123456"

echo "Starting FastAPI server on $HOST:$PORT"


uvicorn "$MODULE_NAME" --host "$HOST" --port "$PORT" --reload