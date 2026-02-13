from fastapi import FastAPI
from app.routers import student_router

app = FastAPI(title="Student API", description="Fast API CRUD for student data", version="1.0.0", docs_url="/docs", redoc_url="/redoc")

app.include_router(student_router.router)

@app.get("/")
async def root():
    return{
        "message":"Student API is Live!",
        "docs":"/docs",
        "version":"1.0.0",
        "student_count":len(student_router.router.routes)
    }
    