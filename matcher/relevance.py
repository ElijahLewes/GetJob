from typing import Dict

import re


def _tokenize(text: str) -> set:
    return set(re.findall(r"\w+", text.lower()))


def score_job_against_resume(job: Dict, resume_text: str) -> float:
    """Compute a simple overlap score between resume and job description."""

    desc = job.get("description", "") + " " + job.get("title", "")
    job_tokens = _tokenize(desc)
    resume_tokens = _tokenize(resume_text)
    if not job_tokens:
        return 0.0
    return len(job_tokens & resume_tokens) / len(job_tokens)




