import csv
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define the number of records you want to generate
num_records = 100  # You can change this to the desired number of records

# Define possible products, cities, and payment methods
products = [
    "Smartphone", "Laptop Case", "Wireless Headphones", "Portable Charger"
]
cities = [
    "New Susanland", "East Lydiaburgh", "Austinmouth", "Port Kerryside",
    "Port Tammy", "East Paul", "Brownmouth", "Gonzalezport", "Ramirezport",
    "South Sheila", "Zoestad", "Mckenziemouth", "New Mark", "North Megan",
    "Trevinoborough", "Savannahberg", "Port Sarahborough", "Harrisonchester",
    "Chungbury", "Juliebury", "West Joshuaport", "Thomasville", "Stephanieberg",
    "Janiceville", "East Benjamintown", "North Elizabethshire", "Armstrongport",
    "South Ann", "Whiteview", "North Brenda", "Rickyland", "South Kevintown"
]
payment_methods = ["Credit Card", "UPI", "COD"]

# Create a CSV file and write the header
with open('generated_ecommerce_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        "Customer ID", "Name", "Email", "Product Purchased", "Purchase Date",
        "Amount Spent ($)", "City", "Payment Method"
    ])

    # Generate fake data
    for _ in range(num_records):
        customer_id = fake.unique.random_int(min=1000, max=9999)
        name = fake.name()
        email = fake.email()
        product = random.choice(products)
        purchase_date = fake.date_between(start_date='-2y', end_date='today')
        amount_spent = round(random.uniform(20, 500), 2)  # Random amount between $20 and $500
        city = random.choice(cities)
        payment_method = random.choice(payment_methods)

        # Write the generated data to the CSV file
        writer.writerow([
            customer_id, name, email, product, purchase_date,
            amount_spent, city, payment_method
        ])

print("CSV file 'generated_ecommerce_data.csv' has been created successfully.")