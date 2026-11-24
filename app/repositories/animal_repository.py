from app.models.postgres.animal_postgres import Animal
from sqlalchemy.orm import Session

def register_animal(animal: Animal, db: Session) -> Animal:
    db.add(animal)
    db.commit()
    db.refresh(animal)
    
    return animal

def get_animals(db: Session) -> list[Animal]:
    return db.query(Animal).all()