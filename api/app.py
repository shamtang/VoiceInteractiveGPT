from flask import Flask, request, send_file, jsonify, session
from elevenlabs import generate, set_api_key, voices, save
import os
import uuid
import numpy
import librosa
import openai
import time
