from typing import List
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str

class AddressNullable(BaseModel):
    city: str|None=None
    country: str|None=None
    

class StudentSchema(BaseModel):
    name: str
    age: int
    address: Address


class StudentId(BaseModel):
    id: str

class StudentUpdate(BaseModel):
    name: str|None=None
    age: int|None=None
    address: AddressNullable=None


class Student(BaseModel):
    id:str
    name: str
    age: int

class ArraySchema(BaseModel):
    data: List[Student]
