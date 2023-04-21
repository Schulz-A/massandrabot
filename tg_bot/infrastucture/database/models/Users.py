from sqlalchemy import (TIMESTAMP, UUID, BigInteger, Boolean, Column,
                        ForeignKey, String, func)

from tg_bot.infrastucture.database.models.base import DataBaseModel


class Project(DataBaseModel):
    __tablename__ = "projects"

    id = Column(UUID, primary_key=True, unique=True)
    name = Column(String(length=255))
    abbreviation = Column(String(length=20))


class Category(DataBaseModel):
    __tablename__ = "categories"

    id = Column(UUID, primary_key=True, unique=True)
    name = Column(String(length=255))
    Project = Column(UUID, ForeignKey("projects.id", ondelete="CASCADE"))


class Article(DataBaseModel):
    __tablename__ = "articles"

    id = Column(UUID, primary_key=True, unique=True)
    name = Column(String(length=255))
    url = Column(String(length=510))
    Category = Column(UUID, ForeignKey("categories.id", ondelete="CASCADE"))


class User(DataBaseModel):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, unique=True)
    username = Column(String(length=255))
    full_name = Column(String(length=255), default=None)
    allow = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    photo_url = Column(String(length=510))
    created_date = Column(TIMESTAMP(timezone=True), default=func.now())
