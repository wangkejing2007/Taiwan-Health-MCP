import sqlite3
import os

db_path = r"d:\Taiwan-Health-MCP\data\health_foods.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

keywords = ["鈣片", "鈣", "益生菌", "乳酸菌", "魚油", "銀杏", "紅麴", "葉黃素"]

for kw in keywords:
    print(f"--- Searching for '{kw}' ---")
    cursor.execute("SELECT name_zh FROM health_foods WHERE name_zh LIKE ? OR health_benefit LIKE ? LIMIT 3", (f"%{kw}%", f"%{kw}%"))
    rows = cursor.fetchall()
    if not rows:
        print(f"No results found for '{kw}'")
    else:
        for row in rows:
            print(f"  {row[0]}")
    print()

conn.close()
