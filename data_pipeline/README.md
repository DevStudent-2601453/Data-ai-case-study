Module 1 — Data Pipeline
Overview

This module implements an end-to-end data pipeline using book data from Books to Scrape, a public website created for web scraping practice.

The pipeline performs the following tasks:

Scrapes book information using Requests and BeautifulSoup.
Stores the raw data in data/raw_books.csv.
Cleans and transforms the data using Pandas.
Converts book prices from GBP to INR using the project-defined exchange rate of 1 GBP = ₹105.50.
Stores the cleaned dataset in data/clean_books.csv.
Loads the cleaned data into a normalized SQLite database.
Executes SQL queries demonstrating the required SQL operations.
Reads SQL query results into Pandas DataFrames.
Reproduces the SQL JOIN using pd.merge() and verifies that both approaches produce identical results.

The final dataset contains 66 books across 7 categories.

Repository Structure
![alt text](image.png)

Files
![alt text](image-1.png)

Setup

Navigate to the module:
![alt text](image-2.png)

Create a virtual environment:
![alt text](image-3.png)
Activate it

Windows
![alt text](image-4.png)

Install the required packages:
![alt text](image-5.png)

Dependencies
    requests
    beautifulsoup4
    pandas
    sqlite3 (Python Standard Library)

Running the Pipeline

Step 1 — Scrape the Data
![alt text](image-6.png)

Step 2 — Clean the Data
![alt text](image-7.png)

Step 3 — Build the Database
![alt text](image-8.png)

Pipeline Flow
![alt text](image-9.png)

Web Scraping

The scraper collects data from the following categories:

Travel
Music
Art
Horror
History
Health
Food and Drink

The collected fields include:

Title
Price
Star Rating
Availability
Category

SQL Queries

The notebook demonstrates:

SELECT
WHERE
ORDER BY
LIMIT
DISTINCT
BETWEEN
LEFT JOIN

All SQL queries and their outputs are saved in
![alt text](image-14.png)
![alt text](image-12.png)
![alt text](image-13.png)
![alt text](image-11.png)
![alt text](image-10.png)

Summary

The Data Pipeline module:

Scrapes 66 books from 7 categories.
Cleans and transforms the data using Pandas.
Converts prices from GBP to INR.
Stores the processed data in a normalized SQLite database.
Executes SQL queries demonstrating key SQL operations.
Loads SQL results into Pandas.
Verifies SQL JOIN results using pd.merge().
Produces all required datasets, database files, and SQL outputs for the project.

This version is consistent with your repository (Data-ai-case-study), uses your actual file names (scraping.py, cleaning.py, Database.ipynb, bookStore.db, sql_query.txt), and removes the conflicting references that were present in the original README.