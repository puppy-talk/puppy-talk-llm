from app.db.db import connect_database
from app.models.entity.pet import Pet
from app.models.request.create_pet_request import CreatePetRequest

class PetCrud:
    def create_pet(pet: CreatePetRequest):
        pet = Pet(
            owner_id=1,
            name=pet.name,
            age=pet.age,
            gender=pet.gender,
            personalities=pet.personalities,
            tone=pet.tone
        )

        with connect_database() as db:
            db.add(pet)
            db.commit()
            db.refresh(pet)

        return pet.id