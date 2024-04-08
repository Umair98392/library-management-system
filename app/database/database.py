import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# MongoDB connection URL
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

# Database Access 
database = client.Library_db

# Collection in Database
students_collection = database.students

