# 📘 ComplianceGPT

AI-powered compliance co-pilot for CA firms serving MSMEs.
Built for ET Gen AI Hackathon 2026 — Phase 2.

---

## 🚀 Getting Started (Both Team Members)

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- [Git](https://git-scm.com/) installed
- A Groq API key from [console.groq.com](https://console.groq.com)

### Setup

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd compliancegpt

# 2. Create your local .env from the example
cp .env.example .env
# → Open .env and paste your GROQ_API_KEY

# 3. Build and start everything
docker-compose up --build

# To stop:
docker-compose down
```

### URLs
| Service  | URL                    |
|----------|------------------------|
| Frontend | http://localhost:8501  |
| Backend  | http://localhost:8000  |
| API Docs | http://localhost:8000/docs |

---

## 🗂️ Project Structure

```
compliancegpt/
├── docker-compose.yml
├── .env.example
├── .gitignore
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
└── frontend/
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

---

## 👥 Team Work Split

| Team Member | Owns |
|-------------|------|
| Member 1    | Frontend (Streamlit pages, UI) |
| Member 2    | Backend (FastAPI routes, RAG, guardrails) |

---

## 📌 Notes

- Code is **volume-mounted** — save a file and it hot-reloads. No rebuilds needed during development.
- Never commit `.env`. It is in `.gitignore`.
- Backend API docs auto-generated at `/docs` (FastAPI Swagger UI).
