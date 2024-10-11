# getstat/apis/global/schemas/response.py

"""Response related base models."""

from __future__ import annotations

from pydantic import BaseModel, model_validator


class BaseResponseModel(BaseModel):
    """Base model to ensure 'Result' is always a list."""

    @model_validator(mode="before")
    @classmethod
    def ensure_list(cls, values: dict) -> dict:
        """Ensure 'Result' is always a list."""
        result = values.get("Result")
        if isinstance(result, dict):
            values["Result"] = [result]
        return values
