import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine
from api.schemas import hotel_schema
from api.core.configs import settings


logger = logging.getLogger()


async def migrate_tables() -> None:
    logger.info("Creating tables")
    engine = create_async_engine(settings.DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(hotel_schema.Base.metadata.drop_all)
        await conn.run_sync(hotel_schema.Base.metadata.create_all)

    logger.info('Tabelas criadas com sucesso!')


if __name__ == "__main__":
    asyncio.run(migrate_tables())

