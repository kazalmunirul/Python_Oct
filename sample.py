from faker import Faker
fake = Faker()  # Create a Faker generator
print(f"Fake Name: {fake.name()}")
print(f"Fake Address: {fake.address()}")
print(f"Fake Text: {fake.text()}")
