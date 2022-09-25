from flask import Flask, request, send_file, jsonify, session
from elevenlabs import generate, set_api_key, voices, save
import os
import uuid
import numpy
import librosa
import openai
import time
import whisper

app = Flask(__name__)
set_api_key(os.getenv("ELEVEN_KEY"))
app.secret_key = os.getenv("SECRET_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")
model = whisper.load_model("base")