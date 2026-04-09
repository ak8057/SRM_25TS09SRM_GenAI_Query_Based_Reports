# Query Based Report

*Transform your Excel data into intelligent, queryable insights*

---
## Complete Project Demo and Explanation
![mqdefault](https://github.ecodesamsung.com/SRIB-PRISM/QueryBasedReports/assets/38880/4db00dd3-6754-4ba0-99c6-798ecf3d0e3a)

https://youtu.be/5Ied6-Ck5FE

Access to .tar files : https://drive.google.com/file/d/1MHhmeR5JtGZzQrHKU5jnFkd43a_EIXAQ/view?usp=sharing

Technical setup document link : https://drive.google.com/file/d/101YWyKTGp1RJCcqk1uew6-lLHLHbXtcm/view?usp=sharing

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
|-- .env
|-- .gitignore
|-- Meeting_ppts.zip
|-- README.md
|-- Testing Dataset
|   |-- Main_Test_Dataset
|   |   |-- chrome
|   |   |   |-- Chrome_Dataset.csv
|   |   |   |-- File1_2008_2011.csv
|   |   |   |-- File1_2008_2011.pdf
|   |   |   |-- File2_2012_2015.csv
|   |   |   |-- File2_2012_2015.pdf
|   |   |   |-- File3_2016_2019.csv
|   |   |   |-- File3_2016_2019.pdf
|   |   |   |-- File4_2020_2023.csv
|   |   |   |-- File4_2020_2023.pdf
|   |   |   |-- chrome_dataset_v2.pdf
|   |   |-- teams
|   |   |   |-- Book1.xlsx
|   |   |   |-- Book2.xlsx
|   |   |   |-- Book3.xlsx
|   |   |   |-- Book4.xlsx
|   |   |   |-- File1.pdf
|   |   |   |-- File2.pdf
|   |   |   |-- File3.pdf
|   |   |   |-- File4.pdf
|   |   |   |-- Teams_Dataset.csv
|   |   |   |-- teams_dataset_v2.pdf
|   |   |-- whatsapp
|   |   |   |-- Book1.xlsx
|   |   |   |-- Book2.xlsx
|   |   |   |-- Book3.xlsx
|   |   |   |-- Book4.xlsx
|   |   |   |-- File1_2009_2012.pdf
|   |   |   |-- File2_2013_2016.pdf
|   |   |   |-- File3_2017_2020.pdf
|   |   |   |-- File4_2021_2024.pdf
|   |   |   |-- Whatsapp_Dataset.csv
|-- backend
|   |-- app
|   |   |-- models
|   |   |   |-- query.py
|   |   |-- routes
|   |   |   |-- db_meta.py
|   |   |   |-- debug_chroma.py
|   |   |   |-- execute_query.py
|   |   |   |-- intelligent_ingest.py
|   |   |   |-- nl2sql.py
|   |   |   |-- refresh_schema.py
|   |   |   |-- summarize.py
|   |   |   |-- upload_excel.py
|   |   |-- services
|   |   |   |-- intelligent_ingestion_service.py
|   |   |   |-- nl2sql_service.py
|   |   |   |-- summarize_service.py
|   |   |   |-- upload_service.py
|   |-- chroma_examples
|   |   |-- fewshot_examples
|   |-- chroma_schemas
|   |-- main.py
|   |-- utils
|   |   |-- chroma_utils.py
|   |   |-- db.py
|   |   |-- db_utils.py
|   |   |-- fewshot_utils.py
|   |   |-- sql_readonly_validator.py
|-- docker-compose.yml
|-- frontend
|   |-- app.py
|   |-- assets
|   |   |-- styles.css
|   |-- components
|   |   |-- data_ingestion.py
|   |   |-- file_upload.py
|   |   |-- followup.py
|   |   |-- nl_query.py
|   |   |-- result_viewer.py
|   |   |-- sidebar.py
|   |   |-- sql_editor.py
|   |   |-- voice_input_component
|   |-- utils
|   |   |-- api.py
|-- requirements.txt

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


