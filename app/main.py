# app/main.py
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Optional
from app.metrics import register_metrics 

app = FastAPI()
register_metrics(app)

# Static files and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Pydantic model for POST request
class User(BaseModel):
    name: str = Field(..., example="Alice")
    age: Optional[int] = Field(None, example=25)

# Root route
@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to FastAPI!"})

# Greet with query param
@app.get("/api/greet")
def greet(name: str = "stranger"):
    return {"greeting": f"Hello, {name}!"}

# Square a number
@app.get("/api/square/{number}")
def square(number: int):
    return {"number": number, "squared": number ** 2}

# Multiply using query parameters with validation
@app.get("/api/multiply")
def multiply(a: int, b: int):
    return {"a": a, "b": b, "product": a * b}

# POST JSON to create a user
@app.post("/api/user")
def create_user(user: User):
    return {"message": f"User {user.name} created", "age": user.age}

# Optional form handling with HTML rendering
@app.post("/submit", response_class=HTMLResponse)
async def handle_form(request: Request, name: str = Form(...), age: Optional[int] = Form(None)):
    return templates.TemplateResponse("result.html", {
        "request": request,
        "name": name,
        "age": age,
    })

# Error demo
@app.get("/api/error")
def raise_error():
    raise HTTPException(status_code=418, detail="I'm a teapot 🫖")


