
import os
import schedule
import time
from job_scraper.fetch_jobs import fetch_jobs
from resume_parser.parser import parse_resume
from resume_parser.customizer import customize_resume, generate_cover_letter
from matcher.relevance import score_job_against_resume
from generator.resume_writer import write_documents
from storage.db import insert_job
from config import settings


def run_job_scraper():
    resume_text = parse_resume(settings.base_resume_path) or ""
    base_cover = parse_resume(settings.base_cover_letter_path) or ""
    jobs = fetch_jobs(settings.search_query)
    for job in jobs:
        score = score_job_against_resume(job, resume_text)
        if score < settings.relevance_threshold:
            continue

        folder_name = f"{job['company']}_{job['title'].replace(' ', '')}"
        out_dir = os.path.join("applications", folder_name)
        os.makedirs(out_dir, exist_ok=True)
        job_desc_path = os.path.join(out_dir, "job_description.txt")
        with open(job_desc_path, "w", encoding="utf-8") as f:
            f.write(job.get("description", ""))

        customized_resume = customize_resume(job, resume_text)
        cover_letter = generate_cover_letter(job, resume_text, base_cover)
        write_documents(job, customized_resume, cover_letter, out_dir)

        insert_job(job, status="generated")



def run():

    schedule.every().hour.do(run_job_scraper)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run()
