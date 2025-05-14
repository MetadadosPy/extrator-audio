# extrator-audio

Pacote Python para extração otimizada de áudio em formato MP3 a partir de vídeos, com suporte a múltiplos formatos de vídeo e otimização para uso com modelos de transcrição como Whisper.

---

## Funcionalidades

- Detecta automaticamente o formato do arquivo de vídeo (MP4, MOV, MKV, WEBM, AVI).
- Extrai áudio em MP3 mono com taxa de amostragem de 16 kHz, ideal para transcrição automática.
- Otimizado para execução rápida com o FFmpeg, usando múltiplas threads e preset ultrafast.
- Fácil de integrar em projetos Python via importação do pacote.

---

##Dependências

- FFmpeg deve estar instalado e acessível pelo sistema (ffmpeg e ffprobe no PATH).
- Python 3.6 ou superior.
- Biblioteca Python ffmpeg-python (instalada automaticamente pelo pip).

---

##Argumentos da função extract_audio_from_video

- video_path (str): caminho para o arquivo de vídeo.
- audio_format (str, opcional): formato do áudio a ser extraído (default: "mp3").
- Retorna o caminho para o arquivo de áudio extraído.
- Formatos suportados(mp4, mov, mkv, webm, avi)

---


## Instalação

Você pode instalar diretamente do GitHub:

```bash
pip install git+https://github.com/MetadadosPy/extrator-audio.git
```
##Exemplo básico
```
from extrator_audio import extract_audio_from_video

video_path = "meu_video.mp4"

try:
    audio_path = extract_audio_from_video(video_path)
    print(f"Áudio extraído para: {audio_path}")
except Exception as e:
    print(f"Erro: {e}")
```

