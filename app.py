import os
import streamlit as st
import pandas as pd

from ai_engine import generate_sql, explain_results
from query_engine import QueryEngine

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Business Analytics Assistant",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

def load_css():
    css_file = os.path.join("assets", "style.css")

    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ---------------- DATABASE ---------------- #

engine = QueryEngine()

# ---------------- QUERY HISTORY ---------------- #

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- HELPER FUNCTIONS ---------------- #

def format_currency(value):

    if value >= 1_000_000:
        return f"${value/1_000_000:.2f} M"

    if value >= 1_000:
        return f"${value/1000:.0f} K"

    return f"${value:.2f}"


def get_metric(sql):
    return engine.execute_query(sql).iloc[0, 0]

# ---------------- DASHBOARD METRICS ---------------- #

total_sales = get_metric(
    "SELECT SUM(Sales) FROM sales"
)

total_profit = get_metric(
    "SELECT SUM(Profit) FROM sales"
)

total_records = get_metric(
    "SELECT COUNT(*) FROM sales"
)

total_regions = get_metric(
    "SELECT COUNT(DISTINCT Region) FROM sales"
)

total_cities = get_metric(
    "SELECT COUNT(DISTINCT City) FROM sales"
)

total_categories = get_metric(
    "SELECT COUNT(DISTINCT Category) FROM sales"
)
# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🤖 AI Analytics")

st.sidebar.markdown("### Quick Questions")

examples = [
    "Which region has the highest sales?",
    "Show total sales by category",
    "Top 10 cities by sales",
    "Profit by state",
    "Average discount by category",
    "Top 5 profitable cities"
]

for q in examples:
    st.sidebar.write("• " + q)

st.sidebar.divider()

if st.session_state.history:

    st.sidebar.markdown("### Recent Questions")

    for item in st.session_state.history[-5:][::-1]:
        st.sidebar.write("✅ " + item)

st.sidebar.divider()

st.sidebar.caption(
    "Powered by Gemini AI + SQLite"
)
# ---------------- HEADER ---------------- #

st.markdown("""
<h1 style='font-size:42px'>
📊 AI Business Analytics Assistant
</h1>
""", unsafe_allow_html=True)

st.markdown("""
AI-powered business intelligence dashboard built using
**Gemini AI • SQLite • Streamlit • Python**
""")

st.divider()
# ---------------- KPI CARDS ---------------- #

row1 = st.columns(3)
row2 = st.columns(3)

metrics = [

    ("💰 Total Sales", format_currency(total_sales)),
    ("📈 Total Profit", format_currency(total_profit)),
    ("📦 Records", f"{int(total_records):,}"),

    ("🌍 Regions", int(total_regions)),
    ("🏙 Cities", int(total_cities)),
    ("📂 Categories", int(total_categories))

]

for column, (title, value) in zip(row1 + row2, metrics):

    with column:

        st.markdown(f"""
<div class="metric-card">

<h4>{title}</h4>

<h2>{value}</h2>

</div>
""", unsafe_allow_html=True)

st.divider()
st.divider()
# ---------------- ASK QUESTION ---------------- #

st.subheader("💬 Ask Your Business Question")

question = st.text_input(
    "",
    placeholder="Example: Which region has the highest sales?"
)

analyze = st.button("🚀 Analyze", use_container_width=True)

if analyze:

    if question.strip() == "":

        st.warning("Please enter a business question.")

    else:

        try:

            if question not in st.session_state.history:
                st.session_state.history.append(question)

            with st.spinner("🤖 Gemini AI is generating SQL..."):

                sql = generate_sql(question)

            with st.expander("📝 Generated SQL"):

                st.code(sql, language="sql")

            df = engine.execute_query(sql)

            st.subheader("📋 Query Result")

            st.dataframe(
                df,
                use_container_width=True
            )

            st.download_button(
                label="⬇ Download Result as CSV",
                data=df.to_csv(index=False),
                file_name="query_result.csv",
                mime="text/csv"
            )

            # ---------------- CHART ---------------- #

            if len(df.columns) == 2 and len(df) > 1:

                st.subheader("📊 Visualization")

                first = df.columns[0]

                st.bar_chart(
                    df.set_index(first)
                )

            # ---------------- AI INSIGHT ---------------- #

            summary = explain_results(
    question,
    df
)

            st.subheader("💡 AI Business Insight")

            st.info(summary)

        except Exception as e:

            if "429" in str(e):

                 st.warning(
            """
### Gemini API quota reached

The application has reached the current Gemini API free-tier limit.

The database, query engine, and dashboard are working correctly.

Please try again after the quota resets or use another API key/project.
"""
        )

            else:

                 st.error(str(e))
            st.divider()

st.markdown(
"""
<div class="footer">

<h4>AI Business Analytics Assistant</h4>

Developed by <b>Akash B H</b>

Powered by <b>Python • SQLite • Streamlit • Gemini AI</b>

</div>
""",
unsafe_allow_html=True
)