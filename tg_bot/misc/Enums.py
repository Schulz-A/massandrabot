from enum import Enum

from tg_bot.infrastucture.database.models import Project, Category, Article


class Enums(Enum):
    logo_path = "logo.jpg"
    question_mark = "users_photo/question_mark.jpg"


tables = {
    "projects": Project,
    "categories": Category,
    "articles": Article
}
