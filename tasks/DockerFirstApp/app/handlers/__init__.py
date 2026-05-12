from __future__ import annotations

from aiogram import Router

from .message import setup as setup_message


def setup() -> Router:
    router = Router()

    message_router = setup_message()
    router.include_routers(message_router)

    return router
