from fastapi import FastAPI

from app.api.pet_chat import llm_api
from app.api.pet import pet_api
from app.db.db import engine, Base
from app.models.entity.pet import Pet

app = FastAPI(
    docs_url = "/api/docs",
    openapi_url = "/api/openapi.json",
)

Base.metadata.create_all(bind=engine)

app.include_router(llm_api, prefix = "/api/v1/pet-chat")
app.include_router(pet_api, prefix = "/api/v1/pets")