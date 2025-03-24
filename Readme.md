job_search_automation/
│── backend/                    
│   ├── api/                    
│   │   ├── api_manager.py       # Manages API endpoints for job search,   ranking, and email automation
│   │   ├── __init__.py          # Initializes the API module
│   ├── core/                    
│   │   ├── job_scraper.py       # Scrapes job postings from LinkedIn/Indeed APIs or web sources
│   │   ├── ai_ranker.py         # Uses Gemini API to rank jobs based on resume data
│   │   ├── cover_letter_generator.py # Generates a personalized cover letter for job applications
│   │   ├── email_sender.py      # Sends emails to recruiters with the cover letter
│   ├── models/                  
│   │   ├── job_model.py         # Defines the Job data structure (title, company, score, etc.)
│   │   ├── user_model.py        # Defines the User model (name, email, resume, etc.)
│   ├── scripts/                 
│   │   ├── run_scraper.py       # Script to trigger job scraping
│   │   ├── run_ai.py            # Script to trigger AI ranking logic
│
│── frontend/                    
│   ├── app.py                   # Frontend Flask app to display ranked jobs and allow interactions
│   ├── templates/               
│   │   ├── index.html           # HTML page for the UI
│
│── database/                    
│   ├── db_schema.sql            # SQL schema for storing job and user data (if using a database)
│
│── tests/                       
│   ├── test_scraper.py          # Unit tests for the job scraper
│
│── requirements.txt             # Python dependencies
│── .env                         # Environment variables (API keys, DB credentials)
│── README.md                    # Documentation
