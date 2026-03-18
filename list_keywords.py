import sqlite3

db_path = r"d:\Taiwan-Health-MCP\data\health_foods.db"

def list_top_keywords():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Common health food keywords in Taiwan
    keywords = ["魚油", "益生菌", "大豆", "納豆", "紅麴", "葡萄糖胺", "鈣", "維生素", "膠原蛋白"]
    
    print("Checking availability of common keywords:")
    for kw in keywords:
        query = "SELECT COUNT(*) FROM health_foods WHERE name_zh LIKE ? OR functional_components LIKE ?"
        cursor.execute(query, (f"%{kw}%", f"%{kw}%"))
        count = cursor.fetchone()[0]
        print(f" - {kw}: {count} items found")
        
    print("\nListing some specific items for Fish Oil (廣為人知的交互作用測試):")
    cursor.execute("SELECT name_zh FROM health_foods WHERE name_zh LIKE '%魚油%' LIMIT 3")
    for row in cursor.fetchall():
        print(f"   -> {row[0]}")
            
    conn.close()

if __name__ == "__main__":
    list_top_keywords()
