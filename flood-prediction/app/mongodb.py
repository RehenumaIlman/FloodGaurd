import pymongo
from pymongo import MongoClient

# Replace <username> and <password> with your MongoDB Atlas credentials
# Replace <cluster_url> with your MongoDB Atlas cluster URL (cluster0.mongodb.net for example)
connection_string = "mongodb+srv://<tushi>:<towshin055>@cluster0.w4gv9.mongodb.net/flood?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB Atlas
client = MongoClient(connection_string)
db = client.flood
subscriptions_collection = db["subscriptions"]

# Function to save subscription
def save_subscription(email, location):
    subscription = {
        "email": email,
        "location": location
    }
    subscriptions_collection.insert_one(subscription)
# from pymongo import MongoClient

# # Replace with your actual connection string
# connection_string = "mongodb+srv://<tushi>:<towshin055>@cluster0.w4gv9.mongodb.net/flood?retryWrites=true&w=majority&appName=Cluster0"

# try:
#     client = MongoClient(connection_string)
#     db = client.flood # Replace 'mydatabase' with your actual database name
#     print("Connected to the database successfully!")
# except Exception as e:
#     print(f"An error occurred: {e}")
