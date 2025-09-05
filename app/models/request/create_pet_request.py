from pydantic import BaseModel

class PetPersonalities(BaseModel):
    activity: str
    humanSociability: str
    dogSociability: str
    independence: str
    trainability: str
    sensitivity: str
    playfulness: str
    protectiveness: str
    communication: str
    routine: str

class PetRequest(BaseModel):
    name: str
    age: int
    gender: str
    personalities: PetPersonalities
    tone: str