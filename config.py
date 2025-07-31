import os
from dataclasses import dataclass


@dataclass
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    db_path: str = os.getenv("JOB_DB_PATH", "jobs.db")
    base_resume_path: str = os.getenv("BASE_RESUME_PATH", "resume.txt")
    base_cover_letter_path: str = os.getenv(
        "BASE_COVER_LETTER_PATH", "cover_letter.txt"
    )
    search_query: str = os.getenv("JOB_SEARCH_QUERY", "software engineer")
    relevance_threshold: float = float(os.getenv("RELEVANCE_THRESHOLD", 0.2))


settings = Settings()
