# GetJob
Timed job matching and resume generating desktop applicaiton using GPT 4.0

Project Summary: Job Matcher System

This project is a modular job application assistant that automates the discovery, customization, and tracking of job applications using AI and a local database. It is designed to streamline the job search process for users by integrating web scraping, GPT-powered resume tailoring, and a user-facing interface for management.

---

### **Core Functions**

#### 1. **Job Discovery**

- **Module**: `job_scraper/fetch_jobs.py`
    
- Automatically scrapes or queries job boards based on user-defined prompts and preferences.
    

#### 2. **Resume and Prompt Processing**

- **Modules**: `resume_parser/parser.py`, `matcher/relevance.py`
    
- Parses the user’s base resume and evaluates job matches using semantic similarity techniques.
    

#### 3. **AI Customization via GPT**

- **Modules**: `gpt/client.py`, `resume_parser/customizer.py`
    
- Uses GPT (e.g., `gpt-4o`) to generate tailored resumes and cover letters based on the job description and resume.
    
- Outputs are saved as `.docx` files in a job-specific folder.
    

#### 4. **File Generation**

- **Module**: `generator/resume_writer.py`
    
- Writes generated resume and cover letter content to `.docx` files using templating or direct formatting.
    

#### 5. **Application Tracking with SQLite**

- **Modules**: `storage/db.py`, `storage/schema.sql`
    
- Stores job metadata, status (e.g., `generated`, `submitted`), and job links in a local SQLite database.
    

#### 6. **User Interface**

- **Module**: `ui/app.py`
    
- A lightweight Flask or Streamlit app that allows users to:
    
    - View job matches
        
    - Update application status
        
    - Export all data as a CSV file
        

#### 7. **Notifications (Optional)**

- **Module**: `notifier/emailer.py`
    
- Can be used to notify users of new matches via email or other platforms.
    

---

This system combines automation and personalization to give job seekers a faster, smarter way to apply to relevant positions. Ready to scale or integrate into a portfolio site or career dashboard.




### File Structure:
project_root/
├── main.py                        # Main entry point
├── config.py                      # Configuration (API keys, settings, OpenAI key)
├── scheduler.py                   # Hourly job scheduler
├── job_scraper/
│   ├── __init__.py
│   └── fetch_jobs.py              # Scraping logic or API fetching
├── matcher/
│   ├── __init__.py
│   └── relevance.py               # Resume/job matching logic
├── resume_parser/
│   ├── __init__.py
│   ├── parser.py                  # Resume and prompt parsing
│   └── customizer.py              # GPT-powered resume and cover letter generator
├── generator/
│   ├── __init__.py
│   └── resume_writer.py           # DOCX/PDF writer for resume & cover letter
├── gpt/
│   ├── __init__.py
│   └── client.py                  # OpenAI API interaction logic
├── storage/
│   ├── __init__.py
│   ├── db.py                      # Store and retrieve past job matches
│   └── schema.sql                 # SQLite database schema
├── ui/
│   ├── __init__.py
│   └── app.py                     # Flask or Streamlit app to view/update/export jobs
├── notifier/
│   ├── __init__.py
│   └── emailer.py                 # Notify user (email or other)
├── templates/
│   ├── email_template.txt         # Plain-text email layout
│   ├── resume_template.docx       # Optional resume boilerplate
│   └── cover_letter_template.txt  # Optional cover letter boilerplate
└── applications/
    └── [Company_JobTitle]/        # One folder per matched job
        ├── job_description.txt    # Parsed job text
        ├── customized_resume.docx # Tailored resume
        └── cover_letter.docx      # Tailored cover letter

## Build and Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the database:

```bash
python -c "from storage.db import init_db; init_db()"
```

Set the required environment variables. At minimum provide an OpenAI API key and
path to your base resume text file:

```bash
export OPENAI_API_KEY="sk-..."
export BASE_RESUME_PATH="/path/to/resume.txt"
export BASE_COVER_LETTER_PATH="/path/to/cover_letter.txt"
export JOB_SEARCH_QUERY="python developer"
export RELEVANCE_THRESHOLD="0.2"
export JOB_DB_PATH="jobs.db"
```

Start the job scheduler:

```bash
python main.py
```

Launch the UI separately if desired:

```bash
python ui/app.py
```

The web interface lets you manage saved jobs, mark them as applied, and
download or open the generated Word documents. You can also upload your
base resume and cover letter from the **Upload** page.

Generated resumes and cover letters will be written to the `applications/`
directory in a subfolder named after each job.
