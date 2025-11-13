import pandas as pd
import sqlite3
from pathlib import Path

# Database file name
DB_FILE = 'ecommerce.db'

# CSV file names
CSV_FILES = {
    'customers': 'customers.csv',
    'products': 'products.csv',
    'orders': 'orders.csv',
    'order_items': 'order_items.csv',
    'payments': 'payments.csv'
}

def create_tables(conn):
    """Create all tables with appropriate data types."""
    cursor = conn.cursor()
    
    # Drop existing tables if they exist
    tables = ['payments', 'order_items', 'orders', 'products', 'customers']
    for table in tables:
        cursor.execute(f'DROP TABLE IF EXISTS {table}')
    
    # Create customers table
    cursor.execute('''
        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            email TEXT NOT NULL,
            signup_date TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')
    
    # Create products table
    cursor.execute('''
        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Create orders table
    cursor.execute('''
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            total_amount REAL NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Create order_items table
    cursor.execute('''
        CREATE TABLE order_items (
            order_item_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    # Create payments table
    cursor.execute('''
        CREATE TABLE payments (
            payment_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            payment_date TEXT NOT NULL,
            payment_method TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
    ''')
    
    conn.commit()
    print("Tables created successfully.")

def load_csv_to_table(conn, table_name, csv_file):
    """Load CSV file into SQLite table."""
    # Check if CSV file exists
    if not Path(csv_file).exists():
        print(f"Warning: {csv_file} not found. Skipping {table_name} table.")
        return
    
    # Read CSV file
    df = pd.read_csv(csv_file)
    
    # Write to SQLite
    df.to_sql(table_name, conn, if_exists='append', index=False)
    
    # Get row count
    cursor = conn.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    count = cursor.fetchone()[0]
    print(f"Loaded {count} rows into {table_name} table from {csv_file}")

def main():
    """Main function to create database and load data."""
    print("Starting data load process...")
    print(f"Database file: {DB_FILE}")
    
    # Connect to SQLite database (creates file if it doesn't exist)
    conn = sqlite3.connect(DB_FILE)
    
    try:
        # Create tables
        create_tables(conn)
        
        # Load data from CSV files in order (respecting foreign key constraints)
        # Load customers first (no dependencies)
        load_csv_to_table(conn, 'customers', CSV_FILES['customers'])
        
        # Load products (no dependencies)
        load_csv_to_table(conn, 'products', CSV_FILES['products'])
        
        # Load orders (depends on customers)
        load_csv_to_table(conn, 'orders', CSV_FILES['orders'])
        
        # Load order_items (depends on orders and products)
        load_csv_to_table(conn, 'order_items', CSV_FILES['order_items'])
        
        # Load payments (depends on orders)
        load_csv_to_table(conn, 'payments', CSV_FILES['payments'])
        
        print("\nData load completed successfully!")
        
        # Display summary
        cursor = conn.cursor()
        print("\nDatabase Summary:")
        for table in ['customers', 'products', 'orders', 'order_items', 'payments']:
            cursor.execute(f'SELECT COUNT(*) FROM {table}')
            count = cursor.fetchone()[0]
            print(f"  {table}: {count} rows")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        raise
    finally:
        conn.close()
        print(f"\nDatabase connection closed. Database saved to {DB_FILE}")

if __name__ == '__main__':
    main()