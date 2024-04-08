from fastapi import FastAPI
from app.routers import students

app = FastAPI()

# Include routers
app.include_router(students.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)