from __future__ import annotations

from aiogram import Router

from .help import router as help_router
from .openrouter import router as openrouter_router
from .start import router as start_router


def setup() -> Router:
    router = Router()
    router.include_routers(help_router, start_router, openrouter_router)

    return router
