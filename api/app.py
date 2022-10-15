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

audio_path = "audio"
if not os.path.exists(audio_path):
    os.makedirs(audio_path)
else:
    current_time = time.time()
    for file in os.listdir(audio_path):
        file_path = os.path.join(audio_path, file)
        file_time = os.path.getmtime(file_path)
        if current_time - file_time > 300:
            os.remove(file_path)


@app.route("/convert", methods=["POST"])
def convert():
    audio_file = request.files.get("audio")
    if audio_file:
        file_name = str(uuid.uuid4()) + ".wav"
        file_path = os.path.join(audio_path, file_name)
        audio_file.save(file_path)
        data, sampleRate = librosa.load(file_path)
        result = model.transcribe(numpy.array(data), language="en")
        print(result["text"])
        return result["text"]
    else:
        return jsonify("Invalid audio file.")


@app.route("/chat", methods=["POST"])
def chat():
    audio_file = request.files.get("audio")
    if audio_file:
        file_name = str(uuid.uuid4()) + ".wav"
        file_path = os.path.join(audio_path, file_name)
        audio_file.save(file_path)
        data, sampleRate = librosa.load(file_path)
        user_text = model.transcribe(numpy.array(data))["text"]
        if "messages" not in session:
            session["messages"] = []

        session["messages"].append({"role": "user", "content": user_text})
        if len(session["messages"]) > 10:
            session["messages"].pop(0)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=session["messages"]
        )

      