# extrator-audio
Comando para instalar:  pip install git+https://github.com/MetadadosPy/extrator-audio.git

Comando para importar: from extrator_audio.api import extract_audio_from_video

Exemplo:

from extrator_audio import extract_audio_from_video

video_path = "video.mp4"  # Substitua pelo caminho do seu vídeo
audio_path = extract_audio_from_video(video_path)
print(f"Áudio extraído para: {audio_path}")
