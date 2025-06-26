# The Database Forge 

A simple Python + SQLite3 project that uses SQLAlchemy to build and query a product-category database.

##  Technologies Used
- Python
- SQLite3
- SQLAlchemy

##  Tables Created
- `Category`: Contains category_id and category_name
- `Product`: Contains product_id, product_name, price, and linked category_id

##  Features
- One-to-many relationship between Category and Product
- Adds 13 products across 7 categories
- Prints each product with its category and price

##  How to Run

1. Clone or download the repo.
2. Run:

```bash
pip install SQLAlchemy
python main.py
