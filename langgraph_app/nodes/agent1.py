#  Agent 1: process_video.py
from langgraph_app.state import AppState
from utils.youtube import download_audio
from utils.transcription import transcribe_audio
from utils.cleaning import clean_transcript

def process_video(state: AppState) -> AppState:
    url = state.get("url")
    if not url:
        raise ValueError("No URL provided in AppState.")

    audio_path = download_audio(url)
    segments, _ = transcribe_audio(audio_path)
    cleaned_text = clean_transcript(segments)

    state["audio_path"] = audio_path
    state["raw_segments"] = segments
    state["transcript"] = cleaned_text

    return state