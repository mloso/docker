from __future__ import annotations

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class BotSettings(BaseSettings):
    BOT_TOKEN: str


bot_settings = BotSettings()


class OpenrouterSettings(BaseSettings):
    OPENROUTER_API_KEY: str
    OPENROUTER_URL: str


openrouter_settings = OpenrouterSettings()
