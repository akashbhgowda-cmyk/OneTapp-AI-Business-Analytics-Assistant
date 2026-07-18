import sqlite3
import pandas as pd

DB_PATH = "database/sales.db"

class QueryEngine:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)

    def execute_query(self, query):
        try:
            result = pd.read_sql_query(query, self.conn)
            return result
        except Exception as e:
            print(f"SQL Error: {e}")
            return None

    def close(self):
        self.conn.close()


if __name__ == "__main__":

    engine = QueryEngine()

    sql = """
    SELECT
Category,
ROUND(SUM(Sales),2) AS TotalSales
FROM sales
GROUP BY Category
ORDER BY TotalSales DESC;
    """

    df = engine.execute_query(sql)

    print(df)

    engine.close()