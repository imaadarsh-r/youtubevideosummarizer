# utils/cleaning.py

import re
from typing import List

def clean_transcript(segments: List[str]) -> str:
    """
    Cleans transcript segments by removing timestamps, filler tokens, and excess whitespace.
    """

    cleaned_lines = []

    for segment in segments:
        # Remove timestamps like [0.00 - 5.00]
        no_time = re.sub(r"\[\d{1,3}\.\d{2}\s*-\s*\d{1,3}\.\d{2}\]", "", segment)

        # Remove filler tokens (e.g., [Music], [Applause])
        no_filler = re.sub(r"\[[^\]]+\]", "", no_time)

        # Normalize spacing and strip
        cleaned = re.sub(r"\s+", " ", no_filler).strip()

        if cleaned:  # skip empty strings
            cleaned_lines.append(cleaned)

    return " ".join(cleaned_lines)