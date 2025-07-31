import os
from dataclasses import dataclass

@dataclass
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    db_path: str = os.getenv("JOB_DB_PATH", "jobs.db")

settings = Settings()
