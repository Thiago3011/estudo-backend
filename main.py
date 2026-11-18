from fastapi import FastAPI
from app.routes.animal_routes import animal_routes

app = FastAPI()

app.include_router(animal_routes)

@app.get("/")
def health_check():
    return {"message": "Server Online"}