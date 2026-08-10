# Data Pipeline

This folder contains a small end-to-end data pipeline that scrapes book data from Books to Scrape, cleans it, converts prices, stores the data in a SQLite database, and demonstrates basic SQL queries.

## What this pipeline does

The project has three main stages:

1. Scraping
   - The script collects book information from several categories on the Books to Scrape website.
   - It extracts fields such as title, price, star rating, stock status, and category.
   - The scraped results are saved as raw data in the data folder.

2. Cleaning and transformation
   - The cleaning script reads the raw CSV file.
   - It removes the pound sign from prices and converts them to numeric values.
   - It maps star ratings from words like "One" and "Five" to numeric values.
   - It converts the stock text into a boolean value.
   - It creates a new INR price column using an exchange rate of 105.50.
   - It removes rows with missing essential values and saves the cleaned dataset.

3. Database and SQL demonstration
   - The notebook in this folder loads the cleaned data into a SQLite database.
   - It runs sample SQL queries to show filtering, ordering, grouping, and joins.
   - The SQL statements are also saved in the data folder.

## Project structure

```text
data_pipeline/
├── cleaning.py            # Reads raw data and creates the cleaned CSV file
├── scraping.py            # Scrapes book data from the website
├── Database.ipynb         # Notebook for database loading and SQL examples
├── requirements.txt       # Python dependencies for the pipeline
├── data/                  # Input/output data files
│   ├── raw_books.csv      # Raw scraped records
│   ├── clean_books.csv    # Cleaned and transformed records
│   ├── sql_query.txt      # SQL queries used in the notebook
│   └── bookStore.db       # SQLite database file
└── README.md              # Project documentation
```

## Files and folders explained

### scraping.py

This file is the first step of the pipeline. It is used when you want to collect fresh data from the website.

What it does:
- Imports requests to send HTTP requests to the website.
- Uses BeautifulSoup to parse the HTML content.
- Visits several book categories from Books to Scrape.
- Extracts the book title, price, star rating, stock status, and category.
- Stores all the results in a list and converts them into a pandas DataFrame.
- Saves the raw output to data/raw_books.csv.

When it is used:
- Run this script before any cleaning or database work.
- Use it whenever you want to refresh the dataset from the website.

Why it is important:
- It collects the source data that the rest of the pipeline depends on.

### cleaning.py

This file is the second step of the pipeline. It is used after scraping to transform the raw data into a cleaner, more analysis-friendly dataset.

What it does:
- Reads the raw CSV file created by scraping.py.
- Removes the currency symbol from the price values.
- Converts price strings into numeric values.
- Maps star-rating text values such as One, Two, Three, Four, and Five to numbers.
- Converts the stock text into a boolean value.
- Creates a new Price_INR column by multiplying the GBP price by 105.50.
- Removes rows that have missing values in important columns.
- Saves the cleaned data to data/clean_books.csv.

When it is used:
- Run this after scraping.py has successfully created the raw CSV file.
- Use it whenever the raw data needs to be cleaned or standardized.

Why it is important:
- It prepares the data for databases, analysis, and machine learning workflows.

### Database.ipynb

This notebook is the final step of the pipeline. It is used after the cleaned CSV file is available.

What it does:
- Loads the cleaned dataset from the CSV file.
- Connects to a SQLite database.
- Stores the cleaned data in a database table.
- Runs SQL queries to demonstrate common operations such as SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, BETWEEN, and JOIN.
- Shows how SQL results can be explored in a notebook environment.

When it is used:
- Run this after the cleaning step is complete.
- Use it when you want to work with the data in SQL rather than only in pandas.

Why it is important:
- It connects the data pipeline to a database workflow and demonstrates SQL usage.

### requirements.txt

This file lists the Python packages needed to run the pipeline.

What it contains:
- requests: used in scraping.py to send HTTP requests to the website.
- beautifulsoup4: used in scraping.py to parse the HTML structure of the web page.
- pandas: used in both scraping.py and cleaning.py to create and manipulate DataFrames and CSV files.
- os: used in the scripts for file and directory management such as creating the data folder.

Why these are used:
- requests and BeautifulSoup allow the code to access and parse online content.
- pandas makes it easy to work with tabular data.
- os helps create folders and paths safely across the system.

When they are used:
- requests and BeautifulSoup are used during scraping.
- pandas is used during both scraping and cleaning.
- os is used when creating the data directory and saving files.

### data/raw_books.csv
- Raw scraped data before cleaning.

### data/clean_books.csv
- Cleaned dataset used for further analysis and database loading.

### data/sql_query.txt
- Stores SQL examples used in the notebook.

### data/bookStore.db
- SQLite database file produced from the cleaned data.

## Installation

1. Go to the project folder:
   ```bash
   cd data_pipeline
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate it:
   ```bash
   .venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the pipeline

Run the scraper first:

```bash
python scraping.py
```

Then run the cleaning script:

```bash
python cleaning.py
```

Finally, open and run the notebook:

- Database.ipynb

## Parsing and cleaning decisions

The project makes a few deliberate decisions during preprocessing:

- Price parsing
  - The price strings include a pound sign, so the script removes "£" and converts the values to numbers.

- Rating conversion
  - The website stores ratings as words like "One", "Two", etc. These are mapped to numeric values from 1 to 5.

- Stock status conversion
  - The text "In stock" is converted to a boolean value so it can be used more easily in analysis.

- Missing values
  - Missing or incomplete essential values are removed to keep the final dataset reliable.

- Currency conversion
  - Prices are converted from GBP to INR using the fixed rate 105.50.

## Notes

This pipeline is a beginner-friendly example of how data can move from a website to a structured dataset and then into a database for SQL analysis.
