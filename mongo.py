from pymongo import MongoClient

# Connect to the MongoDB server running on localhost
client = MongoClient('localhost', 27017)

# Select or create a database
db = client['example_database']

# Select or create a collection (similar to a table in relational databases)
collection = db['example_collection']

# Insert a document
document = {"name": "John Doe", "age": 30, "city": "Example City"}
result = collection.insert_one(document)
print(f"Inserted document with ID: {result.inserted_id}")

# Query documents
query = {"name": "John Doe"}
result = collection.find_one(query)
print("Query Result:", result)

# Update a document
update_query = {"name": "John Doe"}
update_data = {"$set": {"age": 31}}
collection.update_one(update_query, update_data)
print("Document updated.")

# Query documents after the update
result_after_update = collection.find_one(query)
print("Query Result after Update:", result_after_update)
