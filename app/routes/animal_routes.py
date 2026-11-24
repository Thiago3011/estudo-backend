from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.schema.animal_schema import Animal
from app.database import get_db
from app.services import animal_services

animal_routes = APIRouter(
    prefix="/animal",
    tags=["animal"]
)

@animal_routes.get("/")
def get_animals(db: Session = Depends(get_db)):
    return animal_services.get_animals(db) 

@animal_routes.post("/")
def register_animal(animal_data: Animal, db: Session = Depends(get_db)):
    return animal_services.register_animal(animal_data, db)
