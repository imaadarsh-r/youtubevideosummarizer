# utils/transcription.py

from faster_whisper import WhisperModel
from typing import List, Tuple

def transcribe_audio(audio_path: str, model_size: str = "base.en") -> Tuple[List[str], str]:
    """
    Transcribes audio using faster-whisper.
    Returns (segments, full_text).
    """

    # Load Whisper model (only once per run)
    model = WhisperModel(model_size, compute_type="auto")  # auto = use GPU if available

    # Transcribe the audio
    segments, _ = model.transcribe(audio_path)

    # Store full segments (with timestamps etc.)
    raw_segments = []
    full_text = ""

    for segment in segments:
        raw_segments.append(f"[{segment.start:.2f} - {segment.end:.2f}] {segment.text}")
        full_text += segment.text.strip() + " "

    return raw_segments, full_text.strip()