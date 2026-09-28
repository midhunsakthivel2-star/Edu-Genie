import os

from dataclasses import dataclass

from dotenv import load_dotenv


# Load .env file
load_dotenv()


@dataclass(frozen=True)
class Settings:

    gemini_api_key: str = os.getenv(
        "GEMINI_API_KEY",
        ""
    ).strip()

    gemini_model: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.8-flash"
    ).strip()

    local_explainer: bool = (
        os.getenv(
            "USE_LOCAL_EXPLAINER",
            "false"
        ).lower()
        == "true"
    )

    local_model: str = os.getenv(
        "LOCAL_EXPLAINER_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M"
    ).strip()


settings = Settings()