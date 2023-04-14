from dataclasses import dataclass

from environs import Env
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
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db_config: DBConfig
    miscellaneous: Miscellaneous


def get_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

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
        miscellaneous=Miscellaneous()
    )
