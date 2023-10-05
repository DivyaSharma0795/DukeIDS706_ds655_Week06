## SQLite Lab

Status badge for 3 versions of Python : 3.7, 3.8, and 3.9: [![CI](https://github.com/nogibjj/DukeIDS706_ds655_Week05_sqlite/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_Week05_sqlite/actions/workflows/cicd.yml)

![image](https://github.com/nogibjj/DukeIDS706_ds655_Week05_sqlite/blob/main/data/Repo_Architecture.drawio.png)



### Lab:

* Use an AI Assistant, but use a different one then you used from a previous lab (Anthropic's Claud, Bard, Copilot, CodeWhisperer, Colab AI, etc)
    * Using Github Copilot
* ETL-Query:  [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query
For the ETL-Query lab:
* [E] Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well.
    * Using a csv copy of the Iris Dataset from Github
* [T] Transform the data by cleaning, filtering, enriching, etc to get it ready for analysis.
    * 
* [L] Load the transformed data into a SQLite database table using Python's sqlite3 module.
    * Loaded in `transform-load.py`
* [Q] Write and execute SQL queries on the SQLite database to analyze and retrieve insights from the data.
    * Query in `query.py`

#### Tasks:

* Fork this project and get it to run
* Make the query more useful and not a giant mess that prints to screen
    * -> Modified query to publish top 5 rows of the dataset

* Convert the main.py into a command-line tool that lets you run each step independantly

    * -> python main.py --step 1 to extract data
    * -> python main.py --step 2 to load data
    * -> python main.py --step 3 to query data

* Fork this project and do the same thing for a new dataset you choose

    * -> Added [Iris dataset](https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv) to the project
    * -> the `test_main.py` file has been updated to test the new dataset

* Make sure your project passes lint/tests and has a built badge
    * -> Added a status badge for the workflow to test on 3 versions of Python : 3.7, 3.8, and 3.9

* Include an architectural diagram showing how the project works
    * -> Added

#### Reflection Questions

* What challenges did you face when extracting, transforming, and loading the data? How did you overcome them?
    * Each csv file has a different format, so I had to make sure that the code was flexible enough to handle different formats, for example the GroceryDB file did not have an 'ID' as the first column name, so I had to include the code to add that based on conditions
* What insights or new knowledge did you gain from querying the SQLite database?
    * For datasets that cannot be opened in excel and are too large to be opened in a text editor, SQLite is a great tool to query the data and get a quick look at the data 
* How can SQLite and SQL help make data analysis more efficient? What are the limitations?
    * SQLite and SQL can help make data analysis more efficient by allowing the user to query the data and get a quick look at the data without having to open the entire dataset in a text editor or excel. The limitations are that SQLite is not as powerful as other databases and cannot handle large datasets
* What AI assistant did you use and how did it compare to others you've tried? What are its strengths and weaknesses?
    * I used Github Copilot, it is very good at predicting the next line of code, but it is not very good at predicting the next few lines of code. It is also not very good at predicting the correct variable names, however it is very good at predicting the correct function names
* If you could enhance this lab, what would you add or change? What other data would be interesting to load and query?
    * I wanted to add more analyses to this lab, however I'm not sure how to implement such generic, one-fit-for-all analyses in SQL. With each table there are different column names and data types and there is no easy way to perform a generic EDA without manual intervention

##### Challenge Exercises

* Add more transformations to the data before loading it into SQLite. Ideas: join with another dataset, aggregate by categories, normalize columns.
* Write a query to find correlated fields in the data. Print the query results nicely formatted.
* Create a second table in the SQLite database and write a join query with the two tables.
* Build a simple Flask web app that runs queries on demand and displays results.
* Containerize the application using Docker so the database and queries can be portable


