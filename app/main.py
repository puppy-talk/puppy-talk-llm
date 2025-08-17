from fastapi import FastAPI

from app.api.pet_chat import llm_api

app = FastAPI(
    docs_url = "/api/docs",
    openapi_url = "/api/openapi.json",
)

app.include_router(llm_api, prefix = "/api/v1")