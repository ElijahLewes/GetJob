
from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import sys
import subprocess
from storage.db import (
    get_jobs,
    get_job,
    update_job_status,
    delete_job,
)
from config import settings

app = Flask(__name__)

# Track whether the user allowed opening documents in Word
word_permission = False


def open_document(path: str) -> None:
    """Attempt to open the document with the default application."""
    if not os.path.exists(path):
        return
    try:
        if sys.platform.startswith("win"):
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
    except Exception as e:
        print(f"Failed to open {path}: {e}")


@app.route("/")
def index():
    jobs = get_jobs()
    return render_template(
        "index.html", jobs=jobs, word_permission=word_permission
    )


@app.route("/grant_word_access", methods=["POST"])
def grant_word_access():
    global word_permission
    word_permission = True
    return redirect(url_for("index"))


@app.route("/jobs/<int:job_id>/<doc_type>")
def open_doc(job_id: int, doc_type: str):
    job = get_job(job_id)
    if not job:
        return "Job not found", 404
    _, title, company, _, _ = job
    folder = f"{company}_{title.replace(' ', '')}"
    file_name = (
        "customized_resume.docx"
        if doc_type == "resume"
        else "cover_letter.docx"
    )
    path = os.path.join("applications", folder, file_name)
    if word_permission:
        open_document(path)
    return send_file(path, as_attachment=False)


@app.route("/jobs/<int:job_id>/applied")
def mark_applied(job_id: int):
    update_job_status(job_id, "applied")
    return redirect(url_for("index"))


@app.route("/jobs/<int:job_id>/delete")
def delete_job_route(job_id: int):
    delete_job(job_id)
    return redirect(url_for("index"))


@app.route("/upload", methods=["GET", "POST"])
def upload_files():
    if request.method == "POST":
        resume_file = request.files.get("resume")
        if resume_file:
            resume_file.save(settings.base_resume_path)
        cover_file = request.files.get("cover_letter")
        if cover_file:
            cover_file.save(settings.base_cover_letter_path)
        return redirect(url_for("index"))
    return render_template("upload.html")

