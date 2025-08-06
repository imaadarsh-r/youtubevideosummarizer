# utils/youtube.py

import os
import uuid
from yt_dlp import YoutubeDL

DOWNLOAD_DIR = "downloads"

def download_audio(url: str) -> str:
    """
    Downloads audio from a YouTube URL and returns the file path (.mp3).
    """

    # Make sure the download directory exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Generate a unique filename (without extension)
    unique_id = uuid.uuid4().hex
    output_template = os.path.join(DOWNLOAD_DIR, unique_id)

    # yt-dlp options
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template + ".%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])

    # Return the expected file path with .mp3
    return output_template + ".mp3"