# The Database Forge

A beginner-friendly Python + SQLite3 project that uses SQLAlchemy to build and query a product-category database.

---

## Technologies Used

- Python 3.10+
- SQLite3 (comes built-in with Python)
- SQLAlchemy (Python ORM)

---

## Database Tables

### Category table

- `category_id`: Integer, Primary Key
- `category_name`: String

### Product table

- `product_id`: Integer, Primary Key
- `product_name`: String
- `price`: Float
- `category_id`: Integer, Foreign Key (linked to Category)

---

## Features

- One-to-many relationship: Each category can have many products
- Inserts 13 products under 7 categories
- Prints product name, price, and associated category
- Uses SQLAlchemy ORM for clean and readable database operations

---

## How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/Suzain123cbit/database-forge
cd database-forge
