 
from fastapi import FastAPI

app = FastAPI(title="Aitegin Project 1")

@app.get("/hello")
def say_hello():
    return {
        "status": "success",
        "message": "Hello from Python FastAPI!",
        "framework_comparison": "It's like Spring Boot, but faster to write."
    }