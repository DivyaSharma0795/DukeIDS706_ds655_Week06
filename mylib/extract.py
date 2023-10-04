"""
Extract a dataset from a URL 
like Kaggle or data.gov. 
JSON or CSV formats tend to work well # noqa: E501
food dataset
"""
import requests


def extract(
    url="https://raw.githubusercontent.com/Barabasi-Lab/GroceryDB/main/data/GroceryDB_IgFPro.csv",  # noqa: E501
    file_path="data/GroceryDB.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        # print(r.content[0])
        # print(type(r.content))
        # print(r.content.decode("utf-8")[0])
        with open(file_path, "wb") as f:
            if r.content.decode("utf-8")[0] == ",":
                f.write(b"id")
            # print(r.content)
            f.write(r.content)
    return file_path


extract()
# extract(
#     "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv",  # noqa: E501
#     "data/Iris_Data.csv",
# )
