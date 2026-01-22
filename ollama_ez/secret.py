#!/usr/bin/env python3

from dotenv import dotenv_values
from pathlib import Path

OLLAMA_PATH = Path(__file__).resolve().parent

config = dotenv_values(OLLAMA_PATH/".env")
api_key = config.get("OLLAMA_API_KEY", "")
