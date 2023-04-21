from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from tg_bot.infrastucture.database.models import User


async def get_user(session: AsyncSession, *clauses):
    stmt = select(User).where(*clauses)
    result = await session.execute(stmt)
    user = result.scalars().first()
    return user


async def add_user(session: AsyncSession, user_id, username, full_name, photo_path):
    stmt = insert(User).values(
        id=user_id,
        username=username,
        full_name=full_name,
        photo_path=photo_path
    ).on_conflict_do_nothing()

    await session.execute(stmt)
    await session.commit()



async def fetch_users_with_params(session: AsyncSession, *clauses):
    stmt = select(User).where(*clauses)
    result = await session.execute(stmt)
    users = result.scalars().all()
    return users

