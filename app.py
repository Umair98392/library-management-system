from fastapi import FastAPI
from routers import students
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve the 'static' folder for static content like HTML files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
def get_homepage():
    # Serve the HTML file located in the static folder
    return FileResponse('static/index.html')

# Include routers
app.include_router(students.router)
