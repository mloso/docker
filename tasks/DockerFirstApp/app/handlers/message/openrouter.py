from __future__ import annotations

from aiogram import Router
from aiogram.types import Message
from aiogram.utils.formatting import Text
from aiohttp import ClientSession
from core.settings import openrouter_settings

router = Router()


async def get_openrouter_response(session: ClientSession, prompt: str) -> str | None:
    try:
        headers = {
            "Authorization": f"Bearer {openrouter_settings.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "google/gemma-4-31b-it:free",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 5000,
        }
        async with session.post(
            url=openrouter_settings.OPENROUTER_URL, json=payload, headers=headers
        ) as response:
            if response.status == 200:
                data = await response.json()
                return data["choices"][0]["message"]["content"].strip()
            return None
    except Exception:  # noqa
        return None


@router.message()
async def message_handler(message: Message, openrouter_session: ClientSession) -> None:
    response = await get_openrouter_response(
        session=openrouter_session, prompt=message.text
    )
    if not response:
        response = "❌ Извините, AI временно недоступен. Попробуйте позже."

    await message.answer(**Text(response).as_kwargs())
