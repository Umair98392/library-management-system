from fastapi import FastAPI
from app.routers import students

app = FastAPI()

# Home page route
@app.get("/")
async def home():
    return "Welcome  to Library Management System Apis."

# Include routers
app.include_router(students.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)