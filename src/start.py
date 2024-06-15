from src.env_settings import settings
from orm import AsyncORM
import asyncio

asyncORM = AsyncORM()

async def create_db():
    await asyncORM.create_tables()

if settings.CREATE_DB:
    asyncio.run(create_db())
