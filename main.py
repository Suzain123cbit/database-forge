from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Set up SQLite DB
engine = create_engine('sqlite:///store.db', echo=True)
Base = declarative_base()

# Define Tables
class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.category_id'))

    category = relationship("Category", back_populates="products")

# Create tables
Base.metadata.create_all(engine)

# Insert data
Session = sessionmaker(bind=engine)
session = Session()

# Create categories
electronics = Category(category_name="Electronics")
books = Category(category_name="Books")
clothing = Category(category_name="Clothing")
candles = Category(category_name="Candles")
vehicles = Category(category_name="Vehicles")

# Create products (2 per category)
products = [
    Product(product_name="Smartphone", price=699.99, category=electronics),
    Product(product_name="Laptop", price=999.99, category=electronics),

    Product(product_name="Python Book", price=29.99, category=books),
    Product(product_name="Data Science Guide", price=34.99, category=books),

    Product(product_name="Jeans", price=49.99, category=clothing),
    Product(product_name="T-Shirt", price=19.99, category=clothing),

    Product(product_name="Scented Candle", price=9.99, category=candles),
    Product(product_name="Jar Candle", price=14.99, category=candles),

    Product(product_name="Electric Car", price=15000.00, category=vehicles),
    Product(product_name="Bicycle", price=300.00, category=vehicles),
]

# Add and commit
session.add_all([electronics, books, clothing, candles, vehicles] + products)
session.commit()

# Fetch and display
all_products = session.query(Product).all()
for p in all_products:
    print(f"{p.product_name} - ₹{p.price} - Category: {p.category.category_name}")
