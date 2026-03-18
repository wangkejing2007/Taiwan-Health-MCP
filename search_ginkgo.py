import sqlite3

db_path = r"d:\Taiwan-Health-MCP\data\health_foods.db"

def search_all_ginkgo():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Correct field name: name_zh
    # We also check health_benefit and health_claim
    query = """
        SELECT name_zh, health_benefit, license_number FROM health_foods 
        WHERE name_zh LIKE '%銀杏%' 
           OR health_benefit LIKE '%銀杏%' 
           OR health_claim LIKE '%銀杏%' 
           OR functional_components LIKE '%銀杏%'
    """
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        
        print(f"Found {len(rows)} items related to Ginkgo:")
        for i, row in enumerate(rows):
            print(f"{i+1}. {row[0]} (License: {row[2]})")
            print(f"   Benefit: {row[1]}")
            
        if not rows:
            print("\nNo items found with keyword '銀杏'.")
            print("Listing some samples to see naming pattern:")
            cursor.execute("SELECT name_zh FROM health_foods LIMIT 10")
            for row in cursor.fetchall():
                print(f" - {row[0]}")
    except Exception as e:
        print(f"Error during search: {e}")
            
    conn.close()

if __name__ == "__main__":
    search_all_ginkgo()
