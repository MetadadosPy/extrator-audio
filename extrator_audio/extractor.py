import ffmpeg
import tempfile

def extract_audio_from_video(video_path: str, audio_format: str = "mp3") -> str:
    temp_audio_path = tempfile.mktemp(suffix=f".{audio_format}")
    try:
        ffmpeg.input(video_path).output(temp_audio_path).run()
        return temp_audio_path
    except Exception as e:
        raise Exception(f"Erro ao extrair áudio do vídeo: {str(e)}")