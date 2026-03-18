import sqlite3
import os

db_path = r"d:\Taiwan-Health-MCP\data\health_foods.db"
if not os.path.exists(db_path):
    print(f"Error: Database not found at {db_path}")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("--- Searching for '鈣片' ---")
cursor.execute("SELECT name_zh FROM health_foods WHERE name_zh LIKE ? LIMIT 5", ("%鈣片%",))
rows = cursor.fetchall()
if not rows:
    print("No results found for '鈣片'")
else:
    for row in rows:
        print(row[0])

print("\n--- Searching for '鈣' ---")
cursor.execute("SELECT name_zh FROM health_foods WHERE name_zh LIKE ? LIMIT 5", ("%鈣%",))
rows = cursor.fetchall()
for row in rows:
    print(row[0])

conn.close()
