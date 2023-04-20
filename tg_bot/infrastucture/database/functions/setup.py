from typing import AsyncContextManager, Callable

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from tg_bot.config import DBConfig
from tg_bot.infrastucture.database.models.base import DataBaseModel


async def create_session_pool(db: DBConfig, echo=False) -> Callable[[], AsyncContextManager[AsyncSession]]:
    engine = create_async_engine(
        db.get_db_uri(),
        query_cache_size=1200,
        pool_size=10,
        max_overflow=200,
        future=True,
        echo=echo
    )

    async with engine.begin() as conn:
        await conn.run_sync(DataBaseModel.metadata.create_all)

    session_pool = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    return session_pool
