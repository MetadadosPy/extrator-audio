from setuptools import setup, find_packages

setup(
    name="extrator_audio",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ffmpeg-python",
        "fastapi",
        "uvicorn"
    ],
    entry_points={
        "console_scripts": [
            "extrator-audio-api=extrator_audio.api:app"
        ]
    },
    author="Seu Nome",
    description="Pacote para extrair áudio de vídeos com suporte a API FastAPI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)