from __future__ import annotations

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.formatting import Bold

router = Router()


@router.message(Command("help"))
async def start_handler(message: Message) -> None:
    await message.answer(
        **Bold("Я бот с нейронкой, просто напиши мне сообщение").as_kwargs(),
    )
