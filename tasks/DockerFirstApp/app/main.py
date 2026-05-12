from __future__ import annotations

import asyncio

from bot import create_bot
from dp import create_dispatcher


async def __main__() -> None:
    dp = create_dispatcher()
    bot = create_bot()

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


def main() -> None:
    asyncio.run(__main__())


if __name__ == "__main__":
    main()
