from fastapi.routing import APIRouter

animal_routes = APIRouter(
    prefix="/animal",
    tags=["animal"]
)

animals = ["gato", "cachorro", "galinha"]

@animal_routes.get("/")
def get_animals():
    return animals