"""
Transforms and Loads data into the local SQLite3 database
Example:
general name,
count_products,
ingred_FPro,
avg_FPro_products,
avg_distance_root,
ingred_normalization_term,
semantic_tree_name,
semantic_tree_node # noqa: E501
"""
import sqlite3
import csv
import os
from pathlib import Path

# load the csv file and insert into a new sqlite3 database
def load(dataset="./data/GroceryDB.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    headers = ""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    for row in payload:
        headers = ", ".join(row)
        break
    dbname = Path(dataset).stem

    conn = sqlite3.connect(dbname + ".db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS " + dbname)
    c.execute("CREATE TABLE " + dbname + "(" + headers.replace(".", "_") + ")")
    # insert
    count_columns = 1
    for char in headers:
        if char == ",":
            count_columns += 1
    questions = ",".join("?" for i in range(count_columns))
    c.executemany(
        "INSERT INTO " + str(dbname) + " VALUES (" + questions + ")",
        payload,
    )
    print(
        str(count_columns) + " columns have been added to the file: " + dbname + ".db"
    )
    conn.commit()
    conn.close()
    return dbname + ".db"


# load("./data/Iris_Data.csv")
# load()
