import sqlite3

# Create a connection to the database (or create it if it doesn't exist)
conn = sqlite3.connect('scraped_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store the scraped data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price REAL,
        rating REAL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to scrape and insert data into the database
def scrape_and_insert():
    # Send an HTTP GET request to the website
    url = 'https://example.com'
    response = requests.get(url)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the webpage (modify as per your project)
    product_title = soup.find('h1', class_='product-title').text
    product_price = float(soup.find('span', class_='product-price').text.strip('$'))
    product_rating = float(soup.find('span', class_='product-rating').text)

    # Insert the data into the database
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO products (title, price, rating) 
        VALUES (?, ?, ?)
    ''', (product_title, product_price, product_rating))

    conn.commit()
    conn.close()

# Call the function to scrape and insert data
scrape_and_insert()
