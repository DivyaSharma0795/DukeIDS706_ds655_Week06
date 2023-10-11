"""Query the database"""

import sqlite3
from prettytable import PrettyTable  # For formatting


def Iris_query(db="Iris_Data.db"):
    """Query the database for the top 5 rows of the db table"""
    tablename = db.split(".")[0]
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    # Getting top 5 rows of the table
    print("Querying the database...")
    cursor.execute("SELECT \
            variety, \
            avg(sepal_length) as avg_sepal_length, \
            avg(sepal_width) as avg_sepal_width, \
            avg(petal_length) as avg_petal_length, \
            avg(petal_width) as avg_petal_width, \
            count(*) as count \
        FROM " + tablename + " GROUP BY 1")
    r_all = cursor.fetchall()
    x = PrettyTable()
    x.field_names = [i[0] for i in cursor.description]
    for r in r_all:
        x.add_row(r)
    print(x)
    conn.close()
    print("We can see the counts and average sepal and petal metrics for each variety of Iris flower, instead of a data dump of the entire table.")
    print("This is done using the group by functionality in SQL to aggregate the data and view the relevant columns")
    return "Success"


if __name__ == "__main__":
    Iris_query()
