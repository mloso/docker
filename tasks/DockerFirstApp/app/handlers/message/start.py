from __future__ import annotations

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.formatting import Bold

router = Router()


@router.message(CommandStart(deep_link=False))
async def start_handler(message: Message) -> None:
    await message.answer(
        **Bold("Привет, я бот с нейронкой, пиши свои сообщения").as_kwargs(),
    )
