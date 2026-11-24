from fastapi import FastAPI
from app.routes.animal_routes import animal_routes
from app.database import Base, engine
from app.models.postgres.animal_postgres import Animal

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(animal_routes)

@app.get("/")
def health_check():
    return {"message": "Server Online"}