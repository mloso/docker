from __future__ import annotations

from aiogram import Dispatcher
from aiohttp import ClientSession
from handlers import setup as setup_handlers


def create_dispatcher() -> Dispatcher:
    openrouter_session = ClientSession()
    dispatcher = Dispatcher(openrouter_session=openrouter_session)

    @dispatcher.shutdown()
    async def shutdown() -> None:
        if not openrouter_session.closed:
            await openrouter_session.close()

    handlers_router = setup_handlers()
    dispatcher.include_router(handlers_router)

    return dispatcher
