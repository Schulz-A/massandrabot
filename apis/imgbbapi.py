from datetime import timedelta
from typing import Union

import aiohttp
from aiogram import Bot
from aiogram.types import PhotoSize

from apis.base import BaseClient


class IMGBBClient(BaseClient):
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.base_url = "https://api.imgbb.com"
        self.user_default_img = "https://i.ibb.co/3zcw7H7/1200px-Question-mark.jpg"
        super().__init__(base_url=self.base_url)

    async def upload_photo(self, photo: Union[PhotoSize, str], bot: Bot, expiration=0, name="photo") -> str:
        exp_in_seconds = int(timedelta(days=expiration).total_seconds())

        form = aiohttp.FormData(quote_fields=False)
        downloaded_photo = await bot.download(photo)
        form.add_field("image", downloaded_photo)
        response = await self._make_request(
            method="post",
            url="/1/upload",
            params={"key": self.api_key, "expiration": exp_in_seconds, "name": name},
            data=form
        )
        result = response[1]["data"]["url"]
        return result
