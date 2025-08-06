from typing import TypedDict, Optional, List

class AppState(TypedDict, total=False):
    url: str
    audio_path: str
    transcript: str
    raw_segments: List[str]  
    title: str
    blog: str
    summary: str