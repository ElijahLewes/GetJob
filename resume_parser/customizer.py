from typing import Dict
from gpt.client import generate_text


def customize_resume(job: Dict, resume_text: str) -> str:
    """Use GPT to tailor the resume for the specific job."""
    prompt = (
        "Customize the following resume for the job: "
        f"{job['title']} at {job['company']}.\n"
        f"Job description: {job.get('description', '')}\n"
        f"Resume:\n{resume_text}"
    )
    return generate_text(prompt)


def generate_cover_letter(
    job: Dict, resume_text: str, base_letter: str = ""
) -> str:
    """Generate a short cover letter for the job."""
    prompt = (
        "Customize the following cover letter for the position "
        f"{job['title']} at {job['company']}.\n"
        f"Job description: {job.get('description', '')}\n"
        f"Base cover letter:\n{base_letter}\n"
        f"Use the following resume information as context:\n{resume_text}"
    )
    return generate_text(prompt)
