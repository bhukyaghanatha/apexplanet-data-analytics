import sqlite3

def get_connection():
    conn = sqlite3.connect("ecommerce_sales.db")
    return conn
