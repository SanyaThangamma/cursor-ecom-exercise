# 📦 Cursor Ecom Exercise

This project was built using **Cursor IDE** as part of the A-SDLC exercise.

It demonstrates the full workflow of:

- Generating synthetic e-commerce data  
- Loading it into a SQLite database  
- Running SQL joins and analytical queries  
- Exporting outputs  
- Pushing the entire project to GitHub  

---

## 📂 Project Structure

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

yaml
Copy code

---

## 🧩 Step 1 — Generate Synthetic Data

Using Cursor IDE prompts, five datasets were created:

- `customers.csv` – customer details  
- `products.csv` – product catalog  
- `orders.csv` – customer orders  
- `order_items.csv` – individual order items  
- `payments.csv` – payment transactions  

These simulate a small e-commerce system with customers, orders, items and payments.

---

## 🗄️ Step 2 — Load Data into SQLite

The script `load_data.py`:

- Creates `ecommerce.db`  
- Creates all tables  
- Loads all CSV data into SQLite  
- Prints a summary of row counts  

Run:

```bash
python load_data.py


🧮 Step 3 — SQL Queries & Joins

All analytical queries are in queries.sql, including:

Revenue per customer

Top products by revenue

Monthly revenue

Joins across customers, products, orders, items, and payments

To execute queries and export results:

python run_queries.py


This generates:

revenue_per_customer.csv

top_products.csv

monthly_revenue.csv

🔗 Step 4 — GitHub Integration

The project was pushed to GitHub using:

git add .
git commit -m "Upload project"
git push origin main


A .gitignore entry is used to exclude the SQLite database file:

ecommerce.db

🧪 How to Run This Project

Clone the repo:

git clone https://github.com/SanyaThangamma/cursor-ecom-exercise.git
cd cursor-ecom-exercise


Install dependencies:

pip install pandas


Load the data:

python load_data.py


Run queries:

python run_queries.py

📊 Outputs Generated
1️⃣ Revenue per Customer

Total spent

Number of orders

Sorted by highest spender

2️⃣ Top Products

Highest revenue products

Total revenue

Units sold

3️⃣ Monthly Revenue

Revenue grouped by month

Shows monthly performance trends

🛠️ Tools Used

Cursor IDE

SQLite

Python (pandas, sqlite3)

Git & GitHub
