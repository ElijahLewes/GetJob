import schedule
import time
from job_scraper.fetch_jobs import fetch_jobs
from storage.db import insert_job


def run_job_scraper():
    jobs = fetch_jobs()
    for job in jobs:
        insert_job(job)


def run():
    schedule.every().hour.do(run_job_scraper)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run()
