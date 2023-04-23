from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from tg_bot.infrastucture.database.models import User, Project, Category, Article


async def get_user(session: AsyncSession, *clauses):
    stmt = select(User).where(*clauses)
    result = await session.execute(stmt)
    user = result.scalars().first()
    return user


async def update_user(session: AsyncSession, *clauses, **values):
    stmt = update(User).where(*clauses).values(**values)
    await session.execute(stmt)
    await session.commit()


async def get_users(session: AsyncSession, *clauses):
    stmt = select(User).where(*clauses)
    result = await session.execute(stmt)
    await session.commit()
    users = result.scalars().all()
    return users


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


async def get_projects(session: AsyncSession, *clauses):
    stmt = select(Project).where(*clauses)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_categories(session: AsyncSession, *clauses):
    stmt = select(Category).options(selectinload(Category.project)).where(*clauses)
    result = await session.execute(stmt)
    await session.commit()
    return result.scalars().all()


async def get_articles(session: AsyncSession, *clauses):
    stmt = select(Article).options(selectinload(Article.category)).where(*clauses)
    result = await session.execute(stmt)
    await session.commit()
    return result.scalars().all()
