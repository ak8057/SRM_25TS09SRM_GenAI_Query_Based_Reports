# Query Based Report

*Transform your Excel data into intelligent, queryable insights*

---
## Complete Project Demo and Explanation
![mqdefault](https://github.ecodesamsung.com/SRIB-PRISM/QueryBasedReports/assets/38880/4db00dd3-6754-4ba0-99c6-798ecf3d0e3a)

https://youtu.be/5Ied6-Ck5FE

Acces to .tar files : https://drive.google.com/file/d/196i9_35FM_3DCs79Owkb4tb4T69dQ2Jq/view?usp=sharing
---

## What This Does?

Ever wished you could just ask your spreadsheets questions and get smart answers back? That's exactly what this project does. Drop in an Excel, PDF amd the data will be stored dynamically in the relevant table and column and Ask any query and right data for the answer will be retrieved from the DB . 

---

## How It Works

**1. Data Ingestion** → Your Excel files get processed and stored in a proper SQL database. 
  So any Data in Pdf or Excel (csv , xlsxx etc) can be interpretted and stored in their relevant tables in that database matching the content and primary identifiers and then actual data can be stored based on similairty with the existing column of the table or new      column. 
  
**2. AI Analysis** → Ask questions in plain English and get intelligent answers about your data
  So any NLP query sent by the user , first relevant tables are found by the ChromaDB vectordb based similarity matching then inside the relevant tables the relevant columns for the query are checked , after which the sql query is formed to retireve the result data      which then can also be converted back to NLP 

Think of it as giving your spreadsheets a brain.

---

## Project Workflow
<img width="1393" alt="image" src="https://github.ecodesamsung.com/SRIB-PRISM/QueryBasedReports/assets/38888/05c1005e-b915-4501-8275-b33b5f08e141">

## User Query Flow
<img width="715" alt="image" src="https://github.ecodesamsung.com/SRIB-PRISM/QueryBasedReports/assets/38888/ef691bd8-ca86-44e7-ba7f-e80ebaa4c871">

---

## Project Structure

```
QueryBasedReports/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   └── query.py                    # Data models
│   │   ├── routes/
│   │   │   ├── db_meta.py                  # Database metadata endpoints
│   │   │   ├── debug_chroma.py             # ChromaDB debugging
│   │   │   ├── execute_query.py            # Query execution
│   │   │   ├── intelligent_ingest.py       # Smart data ingestion
│   │   │   ├── nl2sql.py                   # Natural language to SQL
│   │   │   ├── refresh_schema.py           # Schema refresh
│   │   │   ├── summarize.py                # Result summarization
│   │   │   └── upload_excel.py             # File upload handling
│   │   ├── services/
│   │   │   ├── intelligent_ingestion_service.py
│   │   │   ├── nl2sql_service.py
│   │   │   ├── summarize_service.py
│   │   │   └── upload_service.py
│   │   ├── utils/
│   │   │   ├── chroma_utils.py             # Vector DB utilities
│   │   │   ├── db_utils.py                 # Database utilities
│   │   │   ├── db.py                       # Database connection
│   │   │   ├── fewshot_utils.py            # Few-shot learning
│   │   │   └── main.py                     # Utility main
│   │   └── main.py                         # FastAPI application
│   └── requirements.txt
│
├── frontend/
│   ├── components/
│   │   ├── data_ingestion.py               # Data ingestion UI
│   │   ├── file_upload.py                  # File upload component
│   │   ├── followup.py                     # Follow-up queries
│   │   ├── nl_query.py                     # Natural language query UI
│   │   ├── result_viewer.py                # Results display
│   │   ├── sidebar.py                      # Sidebar navigation
│   │   └── sql_editor.py                   # SQL editor component
│   │
│   ├── utils/
│   │   ├── api.py                          # API client
│   │   └── app.py                          # App utilities
│   │
│   └── app.py                              # Main Streamlit app
│
├── Testing Dataset/
│   └── Main_Test_Dataset/
│       ├── chrome/                         # Chrome test data
│       ├── teams/                          # Teams test data
│       └── whatsapp/                       # WhatsApp test data
│
├── docker-compose.yml                      # Docker orchestration
├── .env.example                            # Environment variables template
├── README.md                               # This file
└── requirements.txt                        # Python dependencies
```
---

# 📦 SETUP GUIDE

## GenAI | Query-Based Reports

This document provides **complete setup instructions** for running the system using three different methods:

1. 🌐 Docker Hub (Recommended)
2. 📦 Offline `.tar` Deployment
3. 🔧 Local Development Setup

---

# 🔷 Prerequisites

Ensure the following are installed:

* Docker & Docker Compose
* MySQL Server (local or Docker)
* Gemini API Key
* Python 3.10+ (only for local setup)

---

# 📁 Required File Structure

```text
nl2sql/
│
├── docker-compose.yml
├── .env
├── 25TS09SRM_docker_backend.tar   (optional)
├── 25TS09SRM_docker_frontend.tar  (optional)
```

---

# 🌐 METHOD 1: Docker Hub Deployment (Recommended)

---

## Step 1 — Create Folder

```bash
mkdir nl2sql
cd nl2sql
```

---

## Step 2 — Create `.env`

```env
DB_USER=root
DB_PASS=your_password
DB_HOST=host.docker.internal
DB_PORT=3306
DB_NAME=your_database

GEMINI_API_KEY=your_gemini_api_key
```

---

## 🧠 Database Configuration Notes

You can use either:

### 🔹 Local MySQL (Recommended)

```env
DB_HOST=host.docker.internal
DB_PORT=3306
```

👉 Ensure MySQL is running locally.

---

### 🔹 Docker MySQL

```env
DB_HOST=mysql
DB_PORT=3306
```

👉 Use only if MySQL is added as a Docker service.

---

⚠️ Do NOT use:

```env
DB_HOST=localhost
```

(inside Docker, this refers to the container itself)

---

## Step 3 — Create `docker-compose.yml`

```yaml
version: "3.9"

services:

  backend:
    image: abhay2kumar/25ts09srm-nl2sql-backend
    container_name: fastapi_backend
    ports:
      - "8000:8000"
    env_file:
      - .env
    restart: unless-stopped

  frontend:
    image: abhay2kumar/25ts09srm-nl2sql-frontend
    container_name: streamlit_frontend
    ports:
      - "8501:8501"
    env_file:
      - .env
    environment:
      - BACKEND_URL=http://backend:8000
    depends_on:
      - backend
    restart: unless-stopped
```

---

## Step 4 — Run

```bash
docker-compose up
```

---

## Step 5 — Access

* Frontend → http://localhost:8501
* Backend → http://localhost:8000

---

---

# 📦 METHOD 2: Offline Deployment (.tar)

---

## Step 1 — Place Files

```text
25TS09SRM_docker_backend.tar
25TS09SRM_docker_frontend.tar
docker-compose.yml
.env
```

---

## Step 2 — Load Images

```bash
docker load -i 25TS09SRM_docker_backend.tar
docker load -i 25TS09SRM_docker_frontend.tar
```

---

## Step 3 — Verify

```bash
docker images
```

Expected:

```text
abhay2kumar/25ts09srm-nl2sql-backend
abhay2kumar/25ts09srm-nl2sql-frontend
```

---

## Step 4 — Update docker-compose.yml

```yaml
version: "3.9"

services:

  backend:
    image: abhay2kumar/25ts09srm-nl2sql-backend:latest
    ports:
      - "8000:8000"
    env_file:
      - .env
    restart: unless-stopped

  frontend:
    image: abhay2kumar/25ts09srm-nl2sql-frontend:latest
    ports:
      - "8501:8501"
    env_file:
      - .env
    environment:
      - BACKEND_URL=http://backend:8000
    depends_on:
      - backend
    restart: unless-stopped
```

---

## Step 5 — Run

```bash
docker-compose up
```

---

---

# 🔧 METHOD 3: Local Development Setup

---

## Step 1 — Clone Repository

```bash
git clone https://github.ecodesamsung.com/SRIB-PRISM/QueryBasedReports.git
cd QueryBasedReports
```

---

## Step 2 — Setup Environment

```bash
cp .env.example .env
```

Edit `.env`:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=query_reports
DB_USER=root
DB_PASS=your_password

GEMINI_API_KEY=your_key_here
```

---

## Step 3 — Virtual Environment

```bash
python3.10 -m venv venv

# Activate
source venv/bin/activate
```

---

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 — Setup Database

```bash
mysql -u root -p -e "CREATE DATABASE query_reports;"
```

---

## Step 6 — Run Backend

```bash
cd backend
uvicorn main:app --reload
```

---

## Step 7 — Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

---

# 🧪 TROUBLESHOOTING

---

## Port already in use

```bash
lsof -i :8501
kill <PID>
```

---

## Backend not connecting

* Check `.env`
* Ensure MySQL is running
* Ensure correct `DB_HOST`

---

## YAML errors

```bash
docker-compose config
```

---

## Gemini API Error

* Free tier limit reached
* Wait or reduce requests

---

## Usage

### 1. Upload Data Files

Navigate to the frontend UI and upload your data files:

- **Supported formats:** Excel (.xlsx, .xls), CSV, PDF, PPT, Images, Text files
- Files are automatically processed and stored in SQL tables
- Schema is extracted and indexed for intelligent querying

### 2. Query Your Data in Natural Language

Simply type questions in plain English:

```
"Show me sales for Q3"
"List all employees who joined after 2021"
"Top 10 products by revenue last month"
"Find orders where amount > 5000 and status = pending"
"What is the average salary by department?"
```

### 3. View Results

- **Tables:** Clean, formatted data tables
- **Charts:** Visual representations of data
- **Summaries:** AI-generated insights
- **SQL Editor:** View and edit generated SQL (advanced users)

---

## Technologies Used

### Backend
- **FastAPI** - Modern, high-performance web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **MySQL / PostgreSQL** - Relational database
- **ChromaDB** - Vector database for embeddings
- **HuggingFace Embedding Model** - Semantic search and matching
- **Gemini LLM** - Natural language understanding

### Frontend
- **Streamlit** - Interactive Python web interface
- **REST API Integration** - Seamless backend communication

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

---

## Documentation

### API Endpoints

<details>
<summary>View available endpoints</summary>

#### Data Ingestion
- `POST /upload/excel` - Upload and process Excel/CSV files
- `POST /ingest/intelligent` - Intelligent data ingestion

#### Querying
- `POST /nl2sql` - Convert natural language to SQL
- `POST /execute` - Execute SQL query
- `POST /summarize` - Generate result summary

#### Schema Management
- `GET /db/meta` - Get database metadata
- `POST /refresh/schema` - Refresh schema embeddings

#### Debugging
- `GET /debug/chroma` - Debug ChromaDB collections

</details>

---

##  Troubleshooting

| Issue | Solution |
|-------|----------|
| Database not connecting | Verify `.env` configuration and ensure database is running |
| Embeddings not loading | Install required model dependencies: `pip install sentence-transformers` |
| Incorrect AI responses | Refresh schema and clear few-shot cache |
| File ingestion errors | Ensure files have proper headers and are not password-protected |
| Docker issues | Run `docker-compose down -v` then restart with `docker-compose up --build` |

*Built for intelligent data analysis and insights.*


