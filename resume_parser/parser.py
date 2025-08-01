from typing import Optional


def parse_resume(path: str) -> Optional[str]:
    """Parse resume text from file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None
