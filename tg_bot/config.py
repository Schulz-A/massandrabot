from dataclasses import dataclass
from typing import Any

from environs import Env
from google.oauth2.service_account import Credentials
from sqlalchemy import URL


@dataclass
class TgBot:
    token: str
    admins: list[int]


@dataclass
class DBConfig:
    host: str
    port: int
    password: str
    user: str
    database: str

    def get_db_uri(self):
        return URL.create(
            drivername='postgresql+asyncpg',
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database
        )


@dataclass
class Miscellaneous:
    photo_host: str
    scoped_credentials: Any = None
    google_scopes: list = None


@dataclass
class Config:
    tg_bot: TgBot
    db_config: DBConfig
    miscellaneous: Miscellaneous


def get_scoped_credentials(credentials, scopes):
    def prepare_credentials():
        return credentials.with_scopes(scopes)
    return prepare_credentials


def get_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    scopes = [
        "https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"
    ]

    google_credentials = Credentials.from_service_account_file("tg_bot/config-google.json")
    scoped_credentials = get_scoped_credentials(google_credentials, scopes)

    return Config(
        tg_bot=TgBot(
            token=env.str('BOT_TOKEN'),
            admins=list(map(int, env.list('ADMINS')))
        ),
        db_config=DBConfig(
            host=env.str('DB_HOST'),
            port=env.str('DB_PORT'),
            password=env.str('DB_PASSWORD'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME'),
        ),
        miscellaneous=Miscellaneous(
            photo_host=env.str('PHOTO_HOST_API'),
            scoped_credentials=scoped_credentials
        )
    )
