# AI Business Analytics Assistant

An AI-powered Business Analytics Assistant that allows users to ask business questions in natural language. The application uses Google's Gemini AI to convert natural-language questions into SQL queries, executes the generated queries against a SQLite database, and presents the results through an interactive Streamlit dashboard.

The goal of the project is to enable business users to retrieve data-driven insights without requiring knowledge of SQL or complex analytics tools.

---

## Features

- Natural Language to SQL using Google Gemini AI
- SQLite database integration
- Interactive Streamlit dashboard
- Business KPI cards
- Natural-language business question input
- AI-generated SQL queries
- Query result visualization
- Interactive data visualization
- Query history
- Download query results as CSV
- Business insights generated from query results
- Gemini API quota error handling

---

## Project Structure

```text
OneTapp_AI_Assistant/
│
├── app.py
├── ai_engine.py
├── database.py
├── query_engine.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── style.css
│
├── data/
│   └── SampleSuperstore.csv
│
└── database/
    └── sales.db
```

### File Description

- `app.py` - Main Streamlit application and user interface.
- `ai_engine.py` - Handles Gemini AI integration and natural-language-to-SQL generation.
- `query_engine.py` - Executes SQL queries against the SQLite database.
- `database.py` - Creates the SQLite database and imports the CSV dataset.
- `requirements.txt` - Contains the Python dependencies required to run the project.
- `assets/style.css` - Contains custom styling for the Streamlit dashboard.
- `data/SampleSuperstore.csv` - Dataset used by the application.
- `database/sales.db` - SQLite database containing the sales data.

---

## Technologies Used

- Python 3.10+
- Streamlit
- SQLite
- Pandas
- Google Gemini API
- Google Gen AI Python SDK
- Python Dotenv

---

## Dataset

The project uses the Sample Superstore dataset containing sales transaction information.

The dataset contains the following columns:

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

The CSV dataset is imported into a SQLite database and stored in a table named `sales`.

---

## How It Works

The application follows this workflow:

```text
User Business Question
        │
        ▼
Google Gemini AI
        │
        ▼
Natural Language to SQL
        │
        ▼
Generated SQL Query
        │
        ▼
SQLite Database
        │
        ▼
Query Execution
        │
        ▼
Pandas DataFrame
        │
        ▼
Dashboard Results
        │
        ├── Data Table
        ├── Visualization
        ├── Business Insight
        └── CSV Download
```

Gemini AI is used to understand the user's natural-language question and generate an appropriate SQLite query. The SQL query is then executed against the database, which remains the source of truth for numerical results.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/akashbhgowda-cmyk/OneTapp-AI-Business-Analytics-Assistant.git
```

Move into the project directory:

```bash
cd OneTapp-AI-Business-Analytics-Assistant
```

---

### 2. Install Dependencies

Run:

```bash
python -m pip install -r requirements.txt
```

---

## Configure Gemini API

The application requires a Google Gemini API key.

Create a file named `.env` in the root directory of the project.

Add your API key:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your own API key.

For security reasons, the `.env` file is excluded from the GitHub repository and should not be committed.

---

## Create the Database

The repository already contains the SQLite database. If you want to recreate it from the CSV dataset, run:

```bash
python database.py
```

This reads:

```text
data/SampleSuperstore.csv
```

and creates:

```text
database/sales.db
```

---

## Run the Application

Run the following command from the project directory:

```bash
python -m streamlit run app.py
```

The application will start and display a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your web browser to access the dashboard.

---

## Example Business Questions

Users can ask questions such as:

- Which region has the highest sales?
- Show total sales by category.
- Top 10 cities by sales.
- Profit by state.
- Average discount by category.
- Top 5 profitable cities.
- Which state generated the highest profit?
- Which segment has the highest profit?
- What is the total quantity sold?
- Which category generated the lowest profit?

---

## Dashboard

The dashboard displays key business metrics including:

- Total Sales
- Total Profit
- Total Records
- Number of Regions
- Number of Cities
- Number of Categories

Users can enter a business question and click **Analyze**. The application then:

1. Sends the question to Gemini AI.
2. Generates an SQLite query.
3. Executes the query against the sales database.
4. Displays the query results.
5. Generates a visualization when applicable.
6. Provides a business insight based on the results.
7. Allows the user to download the results as a CSV file.

---

## API Quota Handling

The application includes error handling for Gemini API quota limitations.

If the Gemini API free-tier quota is reached, the application displays a user-friendly message instead of exposing a technical error stack trace.

---

## Security

The Gemini API key is stored using environment variables.

The `.env` file should never be uploaded to GitHub.

Make sure `.gitignore` contains:

```text
.env
__pycache__/
*.pyc
.venv/
venv/
```

---

## Limitations

- The application currently supports a single SQLite sales database.
- The accuracy of generated SQL depends on the natural-language question and Gemini AI.
- Gemini API free-tier usage is subject to quota limits.
- The current dataset focuses primarily on sales-related analytics.
- Advanced authentication and role-based access control are not implemented in this prototype.

---

## Future Enhancements

- Support for multiple databases and datasets
- Role-based user authentication
- SQL query validation and security restrictions
- Advanced interactive visualizations
- PDF report generation
- Voice-based business questions
- Conversation-based follow-up questions
- Query caching
- Scheduled analytics reports
- Deployment to a cloud platform

---

## Author

**Akash B H**

MCA  
AI Engineering Assessment – Round 1

---

## Project Purpose

This project was developed as part of an AI Engineering assessment to demonstrate the integration of Generative AI with structured business data. It shows how natural-language interfaces can simplify business analytics by allowing users to interact with databases without directly writing SQL queries.
## Application Screenshots

### Dashboard

![AI Business Analytics Dashboard](screenshots/dashboard.png)

### Query Result

![Query Result](screenshots/query_result.png)

### Data Visualization

![Data Visualization](screenshots/visualization.png)