import ffmpeg
import tempfile
import os
import subprocess
import json

# Lista de formatos suportados
FORMATOS_SUPORTADOS = {"mp4", "mov", "mkv", "webm", "avi"}

def get_format_from_video(video_path: str) -> str:
    """
    Detecta o formato (container) do arquivo de vídeo usando ffprobe.
    """
    try:
        probe = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-show_entries", "format=format_name",
                "-of", "json",
                video_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        if probe.returncode != 0:
            raise Exception(probe.stderr.strip())

        format_info = json.loads(probe.stdout)
        return format_info["format"]["format_name"].split(",")[0]

    except Exception as e:
        raise Exception(f"Erro ao identificar o formato do vídeo: {str(e)}")


def extract_audio_from_video(video_path: str, audio_format: str = "mp3") -> str:
    """
    Extrai o áudio de um vídeo no formato MP3 otimizado para Whisper.
    Detecta o formato do vídeo, valida e continua com a extração.
    """
    video_format = get_format_from_video(video_path)
    print(f"Formato detectado: {video_format}")

    if video_format.lower() not in FORMATOS_SUPORTADOS:
        raise Exception(f"Formato '{video_format}' não é suportado. "
                        f"Formatos permitidos: {', '.join(FORMATOS_SUPORTADOS)}")

    temp_audio_path = tempfile.mktemp(suffix=f".{audio_format}")

    try:
        (
            ffmpeg
            .input(video_path)
            .output(
                temp_audio_path,
                format="mp3",
                acodec="libmp3lame",
                audio_bitrate="128k",
                threads=0,
                preset="ultrafast",
                ac=1,
                ar="16000"
            )
            .overwrite_output()
            .run(quiet=True)
        )
        return temp_audio_path

    except Exception as e:
        raise Exception(f"Erro ao extrair áudio do vídeo: {str(e)}")
