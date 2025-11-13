Cursor Ecom Exercise

This project was built using Cursor IDE as part of the A-SDLC exercise.
It demonstrates the full workflow of:

Generating synthetic e-commerce data

Loading it into a SQLite database

Running SQL joins and analytical queries

Exporting outputs

Pushing the entire project to GitHub

📂 Project Structure
cursor-ecom-exercise/
│
├── customers.csv
├── products.csv
├── orders.csv
├── order_items.csv
├── payments.csv
│
├── load_data.py
├── run_queries.py
├── queries.sql
│
├── revenue_per_customer.csv
├── top_products.csv
├── monthly_revenue.csv
│
├── generate_data_prompt.txt
├── README.md
└── .gitignore

🧩 Step 1 — Generate Synthetic Data

Using Cursor IDE prompts, five datasets were generated:

customers.csv

products.csv

orders.csv

order_items.csv

payments.csv

These files simulate a small e-commerce system with customers, orders, items, and payments.

🗄️ Step 2 — Load Data into SQLite

The script load_data.py:

Creates ecommerce.db

Creates all tables

Loads the CSV files into the DB

Prints a summary of row counts

Run:

python load_data.py

🧮 Step 3 — SQL Queries & Joins

All SQL queries are stored in queries.sql, including:

Revenue per customer

Top products by revenue

Monthly revenue

Joins across orders, customers, items, and products

To run queries and export results:

python run_queries.py


This generates:

revenue_per_customer.csv

top_products.csv

monthly_revenue.csv

🔗 Step 4 — GitHub Integration

The full project was pushed to GitHub using:

git add .
git commit -m "Upload project"
git push origin main


A .gitignore file excludes the SQLite file:

ecommerce.db

🧪 How to Run This Project

Clone the repo:

git clone https://github.com/SanyaThangamma/cursor-ecom-exercise.git
cd cursor-ecom-exercise


Install dependencies:

pip install pandas


Load the CSV data:

python load_data.py


Run analytics:

python run_queries.py

📊 Outputs Generated
1️⃣ Revenue per Customer

Total spent by each customer

Number of orders

Sorted by highest spend

2️⃣ Top Products

Products with highest revenue

Total revenue

Units sold

3️⃣ Monthly Revenue

Revenue grouped per month

Shows sales pattern

🛠️ Tools Used

Cursor IDE

Python (pandas, sqlite3)

SQLite

Git & GitHub
