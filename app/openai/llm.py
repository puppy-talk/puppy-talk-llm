from openai import AsyncOpenAI

from app.core.config import env_config

client = AsyncOpenAI(api_key=env_config.secret_key)

async def get_response_from_llm(system_prompt: str, user_prompt: str):
    return await client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": user_prompt
            },
        ] 
    )