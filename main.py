"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
from mylib.Advanced_Query import Iris_query
import argparse


def main():
    # print("Step number to run (1 - Extract, 2 - Load, 3 - Query, 4 - Group by)")
    # print("Enter your argument as:\n python main.py --step <step number>")
    parser = argparse.ArgumentParser(description="Extract, Transform, or Load data")
    parser.add_argument(
        "--step", type=int, help="Step number to run (1 - Extract, 2 - Load, 3 - Query, 4 - Group by)"
    )
    args = parser.parse_args()
    # Extract
    if args.step == 1:
        print("Extracting data...")
        extract()

    # Transform and load
    elif args.step == 2:
        print("Transforming data...")
        load()

    # Query
    elif args.step == 3:
        print("Querying data...")
        query()

    # Query
    elif args.step == 4:
        print("Running Group by...")
        Iris_query()

    else:
        print("Invalid step number")

if __name__ == "__main__":
    main()