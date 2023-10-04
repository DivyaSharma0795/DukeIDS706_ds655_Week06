"""Query the database"""

import sqlite3


def query(db="GroceryDB.db"):
    """Query the database for the top 5 rows of the GroceryDB table"""
    tablename = db.split(".")[0]
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + tablename + " LIMIT 5")
    print("Top 5 rows of the " + tablename + " table:")
    print([i[0] for i in cursor.description])  # Printing Headers
    print(cursor.fetchall())  # Printing query output
    conn.close()
    return "Success"


query()
query("Iris_Data.db")
