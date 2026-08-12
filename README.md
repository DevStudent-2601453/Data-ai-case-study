# 📚 Data AI Case Study

An end-to-end Data Engineering, Data Analytics, and Generative AI project demonstrating the complete lifecycle of data—from collection and storage to analysis and AI-powered question answering.

This repository contains three independent modules that together showcase modern data workflows.

---

# 📂 Repository Structure

```
Data-ai-case-study/
│
├── analytics/
│   ├── 01_eda.ipynb
│   ├── 02_modeling.ipynb
│   ├── charts/
│   ├── titanic.csv
│   ├── best_titanic_pipeline.pkl
│   ├── requirements.txt
│   └── README.md
│
├── data_pipeline/
│   ├── data/
│   │   ├── raw_books.csv
│   │   ├── clean_books.csv
│   │   ├── bookstore.db
│   │   └── sql_query.txt
│   ├── scraping.py
│   ├── cleaning.py
│   ├── Database.ipynb
│   ├── requirements.txt
│   └── README.md
│
├── support_assistant/
│   ├── app/
│   ├── docs/
│   ├── chroma_db/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
└── README.md
```

---

# 🚀 Modules

## 1️⃣ Data Pipeline

A complete data engineering pipeline that collects book information through web scraping, cleans and transforms the dataset, and stores the processed data in SQLite.

### Features

- Web scraping using Python
- Data cleaning and preprocessing
- CSV generation
- SQLite database creation
- SQL query examples
- Jupyter notebook demonstrating database operations

### Technologies

- Python
- Pandas
- BeautifulSoup
- Requests
- SQLite

---

## 2️⃣ Analytics

A machine learning project using the Titanic dataset to perform exploratory data analysis, feature engineering, model training, and performance evaluation.

### Features

- Exploratory Data Analysis (EDA)
- Data visualization
- Feature engineering
- Multiple classification models
- Model comparison
- Saved trained model
- Performance metrics and confusion matrices

### Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

---

## 3️⃣ AI Support Assistant

A Retrieval-Augmented Generation (RAG) customer support assistant built with LangGraph, FastAPI, ChromaDB, and Large Language Models.

### Features

- Document ingestion
- Vector embeddings
- Semantic search
- Retrieval-Augmented Generation (RAG)
- LangGraph workflow
- FastAPI backend
- Docker support

### Technologies

- Python
- LangChain
- LangGraph
- ChromaDB
- FastAPI
- OpenAI API
- Docker

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- SQLite
- BeautifulSoup
- Requests
- FastAPI
- LangChain
- LangGraph
- ChromaDB
- Docker
- Git & GitHub

---

# ▶️ Running the Projects

Each module is independent and contains its own `README.md` and `requirements.txt`.

### Data Pipeline

```bash
cd data_pipeline
pip install -r requirements.txt
```

---

### Analytics

```bash
cd analytics
pip install -r requirements.txt
```

---

### Support Assistant

```bash
cd support_assistant
pip install -r requirements.txt
python main.py
```

---

# 📊 Project Workflow

```
Web Scraping
      │
      ▼
Data Cleaning
      │
      ▼
SQLite Database
      │
      ▼
Data Analysis
      │
      ▼
Machine Learning
      │
      ▼
Generative AI Support Assistant
```

---

# 📌 Learning Outcomes

This project demonstrates practical experience in:

- Data Collection
- Data Cleaning
- Database Design
- SQL
- Exploratory Data Analysis
- Machine Learning
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- FastAPI Development
- Docker Deployment
- Git Version Control

---

# 📸 Project Modules

| Module | Description |
|---------|-------------|
| Data Pipeline | Data collection, cleaning, SQLite storage |
| Analytics | Titanic EDA and predictive modeling |
| Support Assistant | AI-powered customer support using RAG |

---

# 👨‍💻 Author

**Manoj R**

Data Engineering • Machine Learning • Generative AI

---

# 📄 License

This project is developed for educational purposes as part of a Data AI Case Study assignment.