import pandas as pd
books=pd.read_csv('data/raw_books.csv')
print(books.head())
print(books.dtypes)
print(books.isnull().sum())
books["Price_GBP"] = pd.to_numeric(
    books["Price_GBP"].str.replace("£", "", regex=False),
    errors="coerce"
)
books['Star_rating']=books['Star_rating'].map({"One":1,"Two":2,"Three":3,"Four":4,"Five":5})
books['In_stock']=books['In_stock'].str.contains("In stock",case=False)
books["Price_GBP"] = books["Price_GBP"].fillna(books["Price_GBP"].median())
books["Star_rating"] = books["Star_rating"].fillna(books["Star_rating"].median())
books["Star_rating"] = books["Star_rating"].astype(int)
books['Price_INR']=books['Price_GBP']*105.50
books.dropna(subset=["Title", "Category"],inplace=True)
cleaned_books=books[['Title','Price_GBP','Price_INR','Star_rating','In_stock','Category']].copy()
cleaned_books.to_csv('data/clean_books.csv',index=False)
print(cleaned_books.head())
cleaned_books.info()