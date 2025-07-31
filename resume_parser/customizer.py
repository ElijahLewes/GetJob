from gpt.client import generate_text
from typing import Dict


def customize_resume(job: Dict, resume_text: str) -> str:
    prompt = f"Customize the following resume for the job: {job['title']} at {job['company']}\n{resume_text}"
    return generate_text(prompt)
