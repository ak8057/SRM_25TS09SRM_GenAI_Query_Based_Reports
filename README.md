# Query Based Reports

*Transform your Excel data into intelligent, queryable insights*

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

## Installation

### Prerequisites

- Docker & Docker Compose
- Python 3.10+
- MySQL
- Gemini API Key

### Docker Installation

1. **Clone the repository**
   ```bash
   git clone https://github.ecodesamsung.com/SRIB-PRISM/QueryBasedReports.git
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
   DB_PASS=your_password
   
   # AI Configuration
   GEMINI_API_KEY=your_key_here
   ```

3. **Launch the application**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: `http://localhost:8501`
   - Backend API: `http://localhost:8000`
   - API Docs: `http://localhost:8000/docs`

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
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Run the frontend**
   ```bash
   cd frontend
   streamlit run app.py
   ```

</details>

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


