import uuid

from sqlalchemy import (TIMESTAMP, UUID, BigInteger, Boolean, Column,
                        ForeignKey, String, func)
from sqlalchemy.orm import relationship

from tg_bot.infrastucture.database.models.base import DataBaseModel


class Project(DataBaseModel):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    name = Column(String(length=255))
    abbreviation = Column(String(length=20))
    categories = relationship("Category", back_populates="project")


class Category(DataBaseModel):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    name = Column(String(length=255))
    project_id = Column(UUID, ForeignKey("projects.id", ondelete="CASCADE"))
    project = relationship("Project", back_populates="categories")
    articles = relationship("Article", back_populates="category")


class Article(DataBaseModel):
    __tablename__ = "articles"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    name = Column(String(length=255))
    url = Column(String(length=510))
    category_id = Column(UUID, ForeignKey("categories.id", ondelete="CASCADE"))
    project_id = Column(UUID, ForeignKey("projects.id", ondelete="CASCADE"))
    category = relationship("Category", back_populates="articles")
    project = relationship("Project")


class User(DataBaseModel):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, unique=True)
    username = Column(String(length=255))
    full_name = Column(String(length=255), default=None)
    allow = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    photo_path = Column(String(length=510))
    created_date = Column(TIMESTAMP(timezone=True), default=func.now())
