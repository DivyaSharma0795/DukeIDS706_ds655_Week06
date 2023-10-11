"""Query the database"""

import sqlite3
from prettytable import PrettyTable  # For formatting


def Iris_query(db="Iris_Data.db"):
    """Query the database for the top 5 rows of the db table"""
    tablename = db.split(".")[0]
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    # Getting top 5 rows of the table
    cursor.execute("SELECT \
            variety, \
            avg(sepal_length) as avg_sepal_length, \
            avg(sepal_width) as avg_sepal_width \
        FROM " + tablename + " GROUP BY 1")
    # print("Top 5 rows of the " + tablename + " table:")
    r_all = cursor.fetchall()
    x = PrettyTable()
    x.field_names = [i[0] for i in cursor.description]
    for r in r_all:
        x.add_row(r)
    print(x)
    conn.close()
    return "Success"


if __name__ == "__main__":
    Iris_query()
