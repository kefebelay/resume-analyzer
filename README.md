
# 📄 Resume Analyzer

An automated system to extract, analyze, and store data from PDF resumes using a modern tech stack — including **FastAPI**, **N8N**, **React**, and **Docker**.

![Tech Stack](https://img.shields.io/badge/Backend-FastAPI-green?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Frontend-React-blue?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Automation-N8N-orange?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Containerized-Docker-informational?style=for-the-badge)

---

## 🚀 Features

- ✅ PDF resume upload with drag & drop or click
- ✅ JWT-based authentication (login/signup)
- ✅ LLM-based resume field extraction via **N8N + Gemini/OpenAI**
- ✅ Data transformation into structured JSON
- ✅ Store results in Airtable
- ✅ Fullstack in Docker (frontend + backend + PostgreSQL + N8N)

---

## 🛠️ Tech Stack

| Layer     | Stack                                    |
| --------- | ---------------------------------------- |
| Frontend  | React + Vite + CSS                       |
| Backend   | FastAPI + JWT + python-multipart         |
| Workflow  | N8N with Gemini/OpenAI                   |
| Database  | PostgreSQL (optional), Airtable / Sheets |
| Dev Tools | Docker + VSCode + .env                   |

---

## 📁 Project Structure

resume-analyzer/
│
├── backend/ # FastAPI backend
│ ├── main.py
│ ├── auth.py
│ ├── upload.py
│ ├── uploads/
│ └── requirements.txt
│
├── frontend/ # Vite + React frontend
│ ├── src/
│ ├── public/
│ └── Dockerfile
│
├── docker-compose.yml # Full app setup
├── .env # Environment variables
└── resume_workflow\.json # n8n automation flow



---

## 🧪 Local Setup

### 📦 Prerequisites

- Docker & Docker Compose
- Node.js 
- Python 
- Airtable account

---

### 🔧 Environment Variables

Create a .env file in the root and fill in:

env
JWT_SECRET=your_super_secret
N8N_WEBHOOK_URL=http://n8n:5678/webhook/...


---

### 🐳 Run Entire Stack with Docker

bash
docker-compose up --build

---

## 📤 Uploading a Resume

1. Signup / Login from the frontend.
2. Upload your `.pdf` via drag-and-drop or file selector.
3. Resume is analyzed by the LLM workflow in N8N.
4. Extracted fields are stored in Airtable or Google Sheets.

---

## 🧠 Example Output
[
  {
    "filename": "John_Doe_Resume.pdf",
    "fullname": "John Doe",
    "email": "johndoe@gmail.com",
    "phone": "+1 234 567 890",
    "skills": ["React", "Node.js", "CSS", "Leadership"],
    "experience_years": 3,
    "last_job_title": "Frontend Developer"
  }
]


## 📈 Roadmap

- [x] JWT authentication
- [x] PDF-only upload with validation
- [x] LLM resume parsing
- [x] Airtable 

---
