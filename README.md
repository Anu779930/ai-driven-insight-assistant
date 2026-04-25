# 🤖 AI-Driven Insights Agent

**Author:** Venkata Sai Anusha Kommasani  
**Location:** Minnetonka, Minnesota  
**Date:** October 2025 – December 2025  
**Tools:** Python · Scikit-Learn · OpenAI · Pandas · Typer · Rich  

---

## 🧠 Project Overview
The **AI Driven  Insight Assistant** is a high-performance Python-based data agent. It bridges the gap between raw datasets and executive decision-making by combining **Natural Language Processing (NLP)** for querying with **Unsupervised Machine Learning** for auditing.

This agent doesn't just answer "What happened?"; it uses an **Isolation Forest** algorithm to find "What's wrong?" and **GPT-4o** to explain "What to do next."

---

## 🎯 Objectives
* **Conversational Analytics:** Transform natural-language questions into structured Pandas queries.
* **Automated Auditing:** Identify financial outliers and potential data-entry errors using ML.
* **Generative Insights:** Summarize complex statistical anomalies into human-readable business advice.
* **Enterprise MLOps:** Maintain secure configuration via environment variables and modular CLI architecture.

---

## 🧩 Key Features

### 🗣️ Natural-Language Analytics (`src/`)
Interpret complex queries through a custom NLP parsing engine:
* *"Total sales last month in CA"*
* *"Top 3 categories by sales in 2017"*
* *"Profit by region last year"*

### 🔍 ML-Powered Anomaly Detection (`app/`)
Uses the **Isolation Forest** algorithm to detect outliers in sales and profit distributions.
* Detects pricing errors (e.g., high sales with near-zero profit).
* Prevents "Bill Shock" or "Data Skew" in executive reporting.

### 🤖 Generative AI Reporting (`app/`)
Integrates with **OpenAI's GPT-4o-mini** to provide:
* Prescriptive recommendations based on detected anomalies.
* Automatic KPI trend identification.

### 🛡️ Production-Grade Engineering
* **Secure Config:** Managed via `.env` files to protect API credentials.
* **Robust Ingestion:** Handles schema drift and encoding issues (UTF-8/Latin-1).
* **Styled UI:** Dynamic terminal-based dashboards using the **Rich** library.

---

## 📁 Folder Structure

```text
ai-sales-insight-assistant/
│
├── app/                  # Core AI Agent Logic
│   ├── anomaly.py        # ML Outlier Detection (Isolation Forest)
│   ├── cli.py            # Main Agent CLI Entrance
│   ├── ingestion.py      # Data Ingestion & Encoding Handling
│   ├── insights.py       # LLM Integration (OpenAI)
│   └── preprocessing.py  # Data Cleaning & Normalization
│
├── src/                  # Conversational Chatbot Logic
│   ├── chatbot.py        # NLP Query Interface
│   └── query_engine.py   # SQL-like Analytics Engine
│
├── data/
│   └── Sample - Superstore.csv  # Real-world Sales Dataset
│
├── .env                  # API Keys (Local Only - Not in Git)
├── requirements.txt      # Project Dependencies
└── README.md             # Documentation

## ⚙️ Technologies Used

| Tool | Purpose |
| :--- | :--- |
| **Python 3.10+** | Core Programming |
| **Scikit-Learn** | Unsupervised Machine Learning (Isolation Forest) |
| **OpenAI API** | Generative AI Reasoning (GPT-4o-mini) |
| **Pandas** | Data Wrangling & Analytics |
| **Typer** | Modular Command-Line Interface |
| **Rich** | Styled Console Output & Dashboards |

---

## 🧮 Example Execution

**Run the AI Agent (Anomaly Analysis):**
```powershell
python -m app.cli data/sample.csv

The agent will load the data, run ML detection, and print a magenta-colored AI Business Insight report.

**Run the Chatbot (NLQ):**

```powershell
python -m src.chatbot "profit by region last year"
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Anu779930/ai-sales-insight-assistant.git
cd ai-sales-insight-assistant
```

### 2. Setup Environment

Create a `.env` file in the root directory.

Add your key:

```
OPENAI_API_KEY=sk-your-key-here
```

Ensure `.env` is added to your `.gitignore`.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Agent

```bash
python -m app.cli data/sample.csv
```

---

## 🌟 Future Enhancements

* AgentForce Integration: Connecting the backend to Salesforce Einstein
* Vector Storage: Implementing RAG (Retrieval-Augmented Generation) for unstructured sales notes
* Interactive Dashboards: Building a Streamlit frontend for non-technical users


## 🧾 Requirements

pandas  
typer  
rich 

Install with:  
`pip install -r requirements.txt`

---

## ⚙️ Setup Instructions
1. Clone the repository  
   `git clone https://github.com/Anu779930/ai-sales-insight-assistant.git`  
   `cd ai-sales-insight-assistant`  
2. Create and activate virtual environment  
   - Windows: `.venv\Scripts\activate`  
   - Mac/Linux: `source .venv/bin/activate`  
3. Install dependencies  
   `pip install -r requirements.txt`  
4. Run queries  
   `python -m src.chatbot "profit by region last year"`

---

## 💡 Analytical Capabilities
| Query | Insight |
|-------|----------|
| Profit by Region | Identify most profitable areas |
| Sales by Month | Detect seasonal trends |
| Top Products | Highlight best sellers |
| Category Performance | Compare across product lines |
| State KPIs | Evaluate local sales |

---

## 🌟 Future Enhancements
- Add quarterly and rolling 30/90-day trends  
- Integrate with AgentForce AI / Salesforce Einstein  
- Build a Streamlit dashboard  
- Add voice or chatbot interface  
- Connect to live CRM/SQL pipelines  

---

## 🧠 Conceptual Flow
User Query → NLP Parsing → Intent Extraction → Data Aggregation → Insight Output  

---

## 🧑‍💼 Real-World Applications
- Enterprise sales analysis  
- AI-powered business intelligence  
- Automated KPI reporting  
- CRM analytics (Salesforce/HubSpot)  
- Predictive AI dashboards  

> Ideal for showcasing skills in Data Analytics, AI Automation, and Business Intelligence.  

---

## 👩‍💻 Author
**Venkata Sai Anusha Kommasani**  
📍 Minnetonka, Minnesota  
🎓 M.S. in Information Systems & Technologies — University of North Texas  
💼 Data Analyst | Data Engineer | AI Automation Enthusiast  

**Connect:**  
[LinkedIn](https://www.linkedin.com/in/venkata-sai-anusha/) · [GitHub](https://github.com/Anu779930)

---

## 🏷️ Keywords
`#DataAnalytics` `#AIProjects` `#Python` `#AgentForceAI` `#BusinessIntelligence`  
`#PowerBI` `#SalesAnalytics` `#Automation` `#NaturalLanguageProcessing`

---

## 📚 License
MIT License — open source and free to modify.


