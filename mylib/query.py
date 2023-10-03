"""Query the database"""

import sqlite3


def query(db="GroceryDB.db"):
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB LIMIT 5")
    print("Top 5 rows of the GroceryDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


# query()
