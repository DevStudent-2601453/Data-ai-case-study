import requests as req
from bs4 import BeautifulSoup
import pandas as pd
import os

# List to store all books
all_books = []

# Categories to scrape
categories = [
    "travel_2",
    "science-fiction_16",
    "sports-and-games_17",
    "science_22",
    "psychology_26",
    "business_35",
    "suspense_44"
]

try:
    for cat in categories:
        url = f"https://books.toscrape.com/catalogue/category/books/{cat}/index.html"

        # Send request
        response = req.get(url)
        response.raise_for_status()
        response.encoding = "utf-8"

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all books
        books = soup.find_all("article", class_="product_pod")

        # Extract book details
        for book in books:
            title = book.find("h3").find("a")["title"]
            price = book.find("p", class_="price_color").text
            rating = book.find("p", class_="star-rating")["class"][1]
            availability = book.find("p", class_="instock availability").text.strip()

            all_books.append({
                "Title": title,
                "Price_GBP": price,
                "Star_rating": rating,
                "In_stock": availability,
                "Category": cat
            })

except Exception as e:
    print(f"Error while scraping category '{cat}': {e}")

# Create DataFrame
books = pd.DataFrame(all_books)

# Create Data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save the raw data
books.to_csv("data/raw_books.csv", index=False)

# Display summary
print(f"\nTotal books scraped: {len(books)}")
print("Raw data saved successfully to: Data/raw_books.csv")

# Display first few rows
print("\nPreview:")
print(books.head())