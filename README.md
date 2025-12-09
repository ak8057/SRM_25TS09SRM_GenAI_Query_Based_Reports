# Query Based Reports

*Transform your Excel data into intelligent, queryable insights*

---

## What This Does?

Ever wished you could just ask your spreadsheets questions and get smart answers back? That's exactly what this project does. Drop in an Excel, PDF amd the data will be stored dynamically in the relevant table and column and Ask any query and right data for the answer will be retrieved from the DB . 

## How It Works

**1. Data Ingestion** → Your Excel files get processed and stored in a proper SQL database. 
  So any Data in Pdf or Excel (csv , xlsxx etc) can be interpretted and stored in their relevant tables in that database matching the content and primary identifiers and then actual data can be stored based on similairty with the existing column of the table or new      column. 
  
**2. AI Analysis** → Ask questions in plain English and get intelligent answers about your data
  So any NLP query sent by the user , first relevant tables are found by the ChromaDB vectordb based similarity matching then inside the relevant tables the relevant columns for the query are checked , after which the sql query is formed to retireve the result data      which then can also be converted back to NLP 

Think of it as giving your spreadsheets a brain.

## Project Workflow
<img width="1393" alt="image" src="https://github.ecodesamsung.com/SRIB-PRISM/QueryBasedReports/assets/38888/05c1005e-b915-4501-8275-b33b5f08e141">

## User Query Flow
<img width="715" alt="image" src="https://github.ecodesamsung.com/SRIB-PRISM/QueryBasedReports/assets/38888/ef691bd8-ca86-44e7-ba7f-e80ebaa4c871">

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

## 🛠️ Installation

### Prerequisites

- Docker & Docker Compose
- Python 3.10+
- MySQL
- Gemini API Key

### Quick Start with Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/QueryBasedReports.git
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

## What Makes This Special

**Smart Processing** → Handles messy Excel files and creates clean database structures

**Natural Language Queries** → No need to write SQL. Just ask questions like you're talking to a colleague

**Flexible Database Support** → Works with PostgreSQL, MySQL, and can be extended to others

**Containerized Deployment** → Docker makes setup painless across different environments

**Interactive Analysis** → Jupyter notebooks provide a familiar interface for data exploration

## Real-World Example

Let's say you have a sales report in Excel:

1. **Before**: Manually sorting through rows, creating pivot tables, struggling with complex formulas
2. **After**: "Hey, what were our best-selling products last month?" → Get instant insights with charts and explanations

## What Makes This Special

**Smart Processing** → Handles messy Excel files and creates clean database structures

**Natural Language Queries** → No need to write SQL. Just ask questions like you're talking to a colleague

**Flexible Database Support** → Works with PostgreSQL, MySQL, and can be extended to others

**Containerized Deployment** → Docker makes setup painless across different environments

**Interactive Analysis** → Jupyter notebooks provide a familiar interface for data exploration

## Real-World Example

Let's say you have a sales report in Excel:

1. **Before**: Manually sorting through rows, creating pivot tables, struggling with complex formulas
2. **After**: "Hey, what were our best-selling products last month?" → Get instant insights with charts and explanations

## Contributing

Found a bug? Have an idea? Contributions are welcome. This project grows better with community input.

## Database Configuration

Your `.env` file should look something like this:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_TYPE=postgresql  # or mysql
```

## Troubleshooting

**Can't connect to database?** → Check your `.env` file and ensure your database is running

**Excel file not processing?** → Make sure the file isn't password-protected and has clear headers

**AI giving weird answers?** → Verify your table name is correct in the notebook configuration

---

*Built for intelligent data analysis and insights.*


