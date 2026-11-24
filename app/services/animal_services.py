from app.models.schema.animal_schema import Animal as AnimalSchema
from app.models.postgres.animal_postgres import Animal as AnimalModel

from sqlalchemy.orm import Session
from app.repositories import animal_repository

def register_animal(animal_data: AnimalSchema, db: Session):
    new_animal = AnimalModel(
        name=animal_data.name,
        type=animal_data.type,
        age=animal_data.age
    )
    
    return animal_repository.register_animal(new_animal, db)

def get_animals(db: Session):
    return animal_repository.get_animals(db)
    