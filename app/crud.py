from app.database import database as db
from bson import ObjectId

# Add a new student into to the database
def add_student(student_data):
    result = db.students_collection.insert_one(student_data.dict())
    return str(result.inserted_id)

# Retrieve students present in the database based on query parameters
def retrieve_students(country,age):
    # Build the filter query based on parameters
    filter_query = {}
    if country:
        filter_query["address.country"] = country
    if age:
        filter_query["age"] = {"$gte": age}  # Greater than or equal to the provided age

    # Find students matching the filter criteria
    students = db.students_collection.find(filter_query)

    # Convert cursor object to a list of dictionaries
    students_list = [{"name": student['name'], "age": student['age']} for student in students]

    return students_list

# Retrieve a student with a matching ID
def retrieve_student(id):
    student = db.students_collection.find_one({"_id":ObjectId(id),},{"_id":0})
    if student:
        return student

# Update a student with a matching ID
def update_student(id, student_data):
    # Build update query using $set operator for selective updates
    update_query={"$set": {}}
    if student_data.name is not None:
        update_query["$set"]["name"] = student_data.name
    if student_data.age is not None:
        update_query["$set"]["age"] = student_data.age

    if student_data.address is not None:
        if student_data.address.city is not None:
            update_query["$set"]["address.city"] = student_data.address.city
        if student_data.address.country is not None:
            update_query["$set"]["address.country"] = student_data.address.country

    # Update the student document
    db.students_collection.update_one({"_id": ObjectId(id)}, update_query)

    return None


# Delete a student from the database
def delete_student(id):
    # Find students matching the filter criteria
    db.students_collection.delete_one({"_id":ObjectId(id)})
    
    return {}