# AI Business Analytics Assistant

An AI-powered Business Analytics Assistant that allows users to ask business questions in natural language. The application converts the user's question into SQL using Google's Gemini AI, executes it on a SQLite database, and displays the results with interactive visualizations and business insights.

---

## Features

- Natural Language to SQL using Gemini AI
- SQLite database integration
- Interactive Streamlit dashboard
- KPI cards for business metrics
- Query history
- Data visualization using Plotly
- Download query results as CSV
- Business insights generated from query results
- Error handling for API quota limits

---

## Project Structure

```
OneTapp_AI_Assistant/
│
├── app.py                     # Streamlit application
├── ai_engine.py               # Gemini AI integration
├── database.py                # Database creation and CSV import
├── query_engine.py            # SQLite query execution
├── requirements.txt
├── README.md
├── .env
│
├── assets/
│   └── style.css
│
├── data/
│   └── SampleSuperstore.csv
│
├── database/
│   └── sales.db
│
├── screenshots/
│
└── report/
```

---

## Technologies Used

- Python 3.10+
- Streamlit
- SQLite
- Pandas
- Plotly
- Google Gemini API
- Python Dotenv

---

## Dataset

The project uses the Sample Superstore dataset containing sales transactions.

Columns include:

- Ship Mode
- Segment
- Country
- City
- State
- Postal Code
- Region
- Category
- Sub-Category
- Sales
- Quantity
- Discount
- Profit

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Move into the project folder.

```bash
cd OneTapp_AI_Assistant
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Generate an API key from Google AI Studio.

---

## Create Database

Run

```bash
python database.py
```

This imports the CSV into SQLite.

---

## Run Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Example Questions

- Which region has the highest sales?
- Show total sales by category.
- Which state generated the highest profit?
- Show top 10 cities by sales.
- Which segment has the highest profit?
- Show average discount by category.
- What is the total quantity sold?
- Which category generated the lowest profit?

---

## Workflow

```
User Question
      │
      ▼
Gemini AI
      │
Generate SQL
      ▼
SQLite Database
      │
Execute Query
      ▼
Pandas DataFrame
      │
Dashboard + Charts + Insights
```

---

## Screenshots

Add screenshots inside the `screenshots/` folder.

Example:

- Dashboard
- Query Result
- Charts
- SQL Generated

---

## Future Enhancements

- Multi-database support
- User authentication
- Export reports as PDF
- Voice-based querying
- Scheduled analytics reports
- Advanced dashboards

---

## Author

Akash B H

MCA | AI & Data Engineering Enthusiast
