import sqlite3
from typing import Dict
from config import settings


def get_connection():
    conn = sqlite3.connect(settings.db_path)
    return conn


def init_db():
    conn = get_connection()
    with open("storage/schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


def insert_job(job: Dict, status: str = "generated") -> None:
    conn = get_connection()
    conn.execute(
        "INSERT INTO jobs (title, company, link, status) VALUES (?, ?, ?, ?)",
        (job["title"], job.get("company", ""), job.get("link", ""), status),

    conn.commit()
    conn.close()


def get_jobs():
    conn = get_connection()
    cur = conn.execute("SELECT id, title, company, link, status FROM jobs")
    rows = cur.fetchall()
    conn.close()

    return rows<<<<<<< 27c411-codex/build-application-from-readme-instructions



def get_job(job_id: int):
    conn = get_connection()
    cur = conn.execute(
        "SELECT id, title, company, link, status FROM jobs WHERE id=?",
        (job_id,),
    )
    row = cur.fetchone()
    conn.close()
    return row


def update_job_status(job_id: int, status: str) -> None:
    conn = get_connection()
    conn.execute("UPDATE jobs SET status=? WHERE id=?", (status, job_id))
    conn.commit()
    conn.close()


def delete_job(job_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM jobs WHERE id=?", (job_id,))
    conn.commit()
    conn.close()

