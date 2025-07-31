from flask import Flask, jsonify
from storage.db import get_jobs

app = Flask(__name__)


@app.route("/jobs")
def list_jobs():
    jobs = get_jobs()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(debug=True)
