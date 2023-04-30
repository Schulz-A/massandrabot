from enum import Enum

from tg_bot.infrastucture.database.models import Article, Category, Project


class Enums(Enum):
    logo_path = "logo.jpg"
    logo_for_fix_group = "fix_logo.jpg"
    question_mark = "users_photo/question_mark.jpg"


tables = {
    "projects": Project,
    "categories": Category,
    "articles": Article
}
