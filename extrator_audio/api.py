from fastapi import FastAPI, UploadFile, File
import shutil
import os
from .extractor import extract_audio_from_video

app = FastAPI()

@app.post("/extrair-audio/")
async def extrair_audio(file: UploadFile = File(...)):
    temp_video = f"temp_{file.filename}"
    with open(temp_video, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    audio_path = extract_audio_from_video(temp_video)
    os.remove(temp_video)

    return {"audio_path": audio_path}