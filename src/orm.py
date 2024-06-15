from sqlalchemy import select, text, insert, func, cast
import asyncio
from src.database import sync_engine, async_engine, session_factory, async_session_factory, Base
from db_models import Roles, Users

class SyncORM():
    def __init__(self):
        pass

    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        sync_engine.echo = True
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_data_into_Users():
        with session_factory() as session:
            # item1 = Users()
            session.commit()

    @staticmethod
    def select_UsersItems():
        with async_session_factory() as session:
            query = (
                # select(Users)
            )
            results = session.execute(query).all()
            return results

class AsyncORM():
    def __init__(self):
        pass

    @staticmethod
    async def create_tables():
        async_engine.echo = True
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        async_engine.echo = False

    @staticmethod
    async def insert_data_into_Users():
        async with async_session_factory() as session:
            item1 = Roles()
            session.add_all([item1])
            await session.commit()

    @staticmethod
    async def select_Users_items():
        async_engine.echo = False
        async with async_session_factory() as session:
            query = (
                # select(DATABASENAME)
            )
            results = await session.execute(query)
            return results.all()

    @staticmethod
    async def update_Users_items():
        async_engine.echo = True
        async with async_session_factory() as session:
            # item = await session.get(DATABASENAME, item_id)
            # item.name = new_name
            # item.price = new_price
            # item.image = new_image
            await session.commit()
