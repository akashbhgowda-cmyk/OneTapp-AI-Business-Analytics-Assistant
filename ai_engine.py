import os
from dotenv import load_dotenv
from google import genai
from query_engine import QueryEngine

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Database Schema
SCHEMA = """
Table Name: sales

Columns:
Ship Mode
Segment
Country
City
State
Postal Code
Region
Category
Sub-Category
Sales
Quantity
Discount
Profit
"""


# Generate SQL from Natural Language
def generate_sql(question):

    prompt = f"""
You are an expert SQLite developer.

Generate ONLY a valid SQLite SQL query.

Database Schema:

{SCHEMA}

Rules:
1. Return ONLY SQL.
2. Do NOT explain anything.
3. Do NOT use markdown.
4. Table name is sales.

User Question:
{question}
"""

    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        )

    except Exception as e:
        raise RuntimeError(f"Gemini API Error: {e}")     

    sql = response.text.strip()

    # Remove markdown if Gemini returns it
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql


# Explain SQL Results
def explain_results(question, df):

    if df is None or df.empty:
        return "No matching records were found for your question."

    rows = len(df)
    cols = len(df.columns)

    summary = f"The query returned {rows} record(s) with {cols} column(s). "

    if cols == 1:
        value = df.iloc[0, 0]
        summary += f"The result is **{value}**."

    elif cols == 2:

        first = df.columns[0]
        second = df.columns[1]

        top = df.iloc[0]

        summary += (
            f"The highest value is "
            f"'{top[first]}' "
            f"with {top[second]}."
        )

    else:

        summary += (
            "Review the table above for detailed analysis."
        )

    return summary


# Test the AI Engine
if __name__ == "__main__":

    engine = QueryEngine()

    question = input("Ask your question: ")

    sql = generate_sql(question)

    print("\nGenerated SQL:\n")
    print(sql)

    df = engine.execute_query(sql)

    print("\nQuery Result:\n")
    print(df)

    summary = explain_results(
        question,
        df.to_string(index=False)
    )

    print("\nBusiness Insight:\n")
    print(summary)

    engine.close()