# 🚀 Query Based Reports


## 📖 Overview

Query Based Reports is an intelligent data query system that converts spreadsheets and documents into a fully queryable SQL database. Users can ask questions in plain English—no SQL or technical expertise required.

The system intelligently ingests data, understands schema context, generates accurate SQL using AI, and returns clean, human-readable responses.

### 🎯 Problem Statement

Traditional database querying requires SQL expertise and deep understanding of complex schemas, creating barriers for non-technical users. Existing natural language querying systems often:

- ❌ Generate incorrect or unsafe SQL
- ❌ Fail to understand business context
- ❌ Produce raw, difficult-to-interpret outputs

**Query Based Reports** solves this by providing validated SQL generation, safe execution, and natural language summaries—democratizing data access and improving decision-making.

---

## ✨ Key Features

### 🔄 Automated Data Ingestion
- 📁 Support for Excel, CSV, PDF, PPT, Images, and text files
- 🧹 Automatic data extraction and cleaning
- 🗄️ Dynamic SQL table creation
- 🔄 Automatic schema change detection and updates

### 🤖 AI-Powered Natural Language Querying
- 💬 Ask questions like *"Show sales for last quarter"*
- 🧠 AI-generated optimized SQL queries
- 🛡️ SQL Guard for safety and validation

### 🧠 Schema Intelligence
- 📊 Schema extraction using SQLAlchemy
- 🎯 Huggingface Embedding model for semantic understanding
- 💾 ChromaDB for intelligent table matching

### 🧩 RAG-Based Prompt Optimization
- 🔗 Combines schema + examples + user query
- ✅ Ensures highly accurate SQL generation

### 📊 Rich Interactive Frontend
- 📤 File upload console
- 💬 Natural language query box
- 📈 Result viewer with tables & charts
- 🛠️ SQL editor for advanced debugging

### 🐳 One-Click Deployment
- 📦 Fully containerized with Docker
- ⚡ Zero manual setup required

---

## 🏗️ System Architecture

```
┌─────────┐     ┌──────────┐     ┌─────────────┐     ┌──────────┐
│  User   │────▶│ Frontend │────▶│   FastAPI   │────▶│  Schema  │
│   UI    │     │    UI    │     │   Backend   │     │ Intelligence│
└─────────┘     └──────────┘     └─────────────┘     └──────────┘
                                         │                    │
                                         ▼                    ▼
                                  ┌─────────────┐     ┌──────────┐
                                  │  RAG + LLM  │────▶│   SQL    │
                                  │  Generator  │     │Validation│
                                  └─────────────┘     └──────────┘
                                         │                    │
                                         ▼                    ▼
                                  ┌─────────────┐     ┌──────────┐
                                  │  Database   │────▶│  Result  │
                                  │  Executor   │     │  Viewer  │
                                  └─────────────┘     └──────────┘
```

---

## 📁 Project Structure

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

## 🛠️ Installation

### Prerequisites

- Docker & Docker Compose
- Python 3.10+
- MySQL 
- Gemini API Key

### Quick Start with Docker (Recommended)

1. **Clone the repository**
   ```bash[
   https://github.ecodesamsung.com/SRIB-PRISM/QueryBasedReports
   cd QueryBasedReports
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with your configuration:
   ```env
   # Database Configuration
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=query_reports
   DB_USER=root
   DB_PASSWORD=your_password
   DB_TYPE=mysql
   
   # AI Configuration
   GEMINI_API_KEY=your_key_here
   ```

3. **Launch the application**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: `streamlit run frontend/app.py`
   - Backend API: `uvicorn main:app --reload`

### Manual Installation

<details>
<summary>Click to expand manual installation steps</summary>

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r backend/requirements.txt
   ```

2. **Set up the database**
   ```bash
   # Create database
   mysql -u root -p -e "CREATE DATABASE query_reports;"
   ```

3. **Run the backend**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

4. **Run the frontend**
   ```bash
   streamlit run frontend/app.py
   ```

</details>

---

## 🎯 Usage

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

- **📊 Tables:** Clean, formatted data tables
- **📈 Charts:** Visual representations of data
- **📝 Summaries:** AI-generated insights
- **🛠️ SQL Editor:** View and edit generated SQL (advanced users)

---

## 🧰 Technologies Used

### Backend
- **FastAPI** - Modern, high-performance web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **MySQL / PostgreSQL** - Relational database
- **ChromaDB** - Vector database for embeddings
- **Jina Embeddings** - Semantic search and matching
- **Gemini LLM** - Natural language understanding

### Frontend
- **Streamlit** - Interactive Python web interface
- **REST API Integration** - Seamless backend communication

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

---

## 📚 Documentation

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

### Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_HOST` | Database host | localhost |
| `DB_PORT` | Database port | 3306 |
| `DB_NAME` | Database name | query_reports |
| `DB_TYPE` | Database type (mysql/postgresql) | mysql |
| `GEMINI_API_KEY` | Google Gemini API key | - |

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Database not connecting | Verify `.env` configuration and ensure database is running |
| Embeddings not loading | Install required model dependencies: `pip install sentence-transformers` |
| Incorrect AI responses | Refresh schema and clear few-shot cache |
| File ingestion errors | Ensure files have proper headers and are not password-protected |
| Docker issues | Run `docker-compose down -v` then restart with `docker-compose up --build` |

---


## 🙏 Acknowledgments

- Google Gemini for powerful LLM capabilities
- ChromaDB for efficient vector storage
- Huggingface Embedding modal for semantic embeddings
- FastAPI and Streamlit communities

---


<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by the Query Based Reports Team

</div>
