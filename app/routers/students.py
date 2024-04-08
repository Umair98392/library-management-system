from fastapi import APIRouter, Query, Path
from app.models import StudentId, StudentSchema, StudentUpdate, ArraySchema
from app.crud import add_student, retrieve_students, retrieve_student, update_student, delete_student

router = APIRouter()

# Endpoint to create a new student
@router.post(
        "/students", 
        summary="Create Students", 
        status_code=201,
        description="API to create a student in the system. All fields are mandatory and required while creating the student in the system.",
        response_model=StudentId, 
        response_description="A JSON response sending back the ID of the newly created student record."
)
def add_student_data(student_data: StudentSchema|None=None):

    return {"id": add_student(student_data)}

# Endpoint to list students with optional filters
@router.get(
        "/students", 
        summary="List students", 
        status_code=200,
        description="An API to find a list of students. You can apply filters on this API by passing the query parameters as listed below.",
        response_model = ArraySchema,
        response_description="sample response"
)
def get_students(
    country: str = Query(None, description=" To apply filter of country. If not given or empty, this filter should be applied."),
    age: int = Query(None, description="Only records which have age greater than equal to the provided age should be present in the result. If not given or empty, this filter should be applied.")):
    
    return {"data": retrieve_students(country,age)}

# Endpoint to fetch a specific student by ID
@router.get(
        "/students/{id}", 
        summary="Fetch student", 
        status_code=200,
        response_model = StudentSchema,
        response_description="sample response"
)
def get_student_data(id: str = Path(description="The ID of the student previously created.")):
    
    return retrieve_student(id)

# Endpoint to update student information
@router.patch(
    "/students/{id}",
    summary="Update student",
    description="API to update the student's properties based on information provided. Not mandatory that all information would be sent in PATCH, only what fields are sent should be updated in the Database.",
    status_code=204,
    response_description= "No content"
)
def update_student_data(id: str = Path(), student_data: StudentUpdate|None=None):

    return update_student(id, student_data)


# Endpoint to delete a student by ID
@router.delete(
        "/students/{id}", 
        summary="Delete student", 
        status_code=200,
        response_model = dict,
        response_description="sample response"
)
def delete_student_data(id: str = Path()):

    return delete_student(id)