"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_etl():
    assert (query(load(extract()))) == "Success"
