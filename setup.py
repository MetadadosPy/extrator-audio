# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="extrator_audio",
    version="0.3.0",
    packages=find_packages(),
    install_requires=["ffmpeg-python", "fastapi", "uvicorn"],
    entry_points={
        "console_scripts": [
            "extrair-audio=extrator_audio.api:main"
        ]
    },
    author="Ivys Lima",
    description="Um extrator de áudio a partir de vídeos usando FFmpeg",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
