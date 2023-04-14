from typing import Callable, AsyncContextManager

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from massandrabot.config import DBConfig
from massandrabot.infrastucture.database.models.base import BaseModel


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
        await conn.run_sync(BaseModel.metadata.create_all)

    session_pool = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    return session_pool
