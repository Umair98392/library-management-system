from pymongo import MongoClient

# MongoDB connection URL
MONGO_URI = "mongodb+srv://user_12:BxE0Lsr4ZOfIpvU4@cluster0.oavbqcz.mongodb.net/"

client = MongoClient(MONGO_URI)

# Database Access 
database = client.umair_db

# Collection in Database
students_collection = database.students

