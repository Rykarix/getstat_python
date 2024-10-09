# getstat/apis/tags/schemas/base.py
"""Base schema for tag data."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, field_validator


class TagType(str, Enum):
    """Enumeration for the 'Type' field in a tag."""

    Standard = "Standard"
    Dynamic = "Dynamic"


class Keywords(BaseModel):
    """Schema for the 'Keywords' field in a tag."""

    Id: list[int]

    @field_validator("Id", mode="before")
    @classmethod
    def convert_id_list(cls, v: list) -> list[int]:
        """Convert list of keyword IDs from strings to integers."""
        if isinstance(v, list):
            return [int(i) for i in v]
        else:
            errmsg = "Invalid format for Keywords.Id; expected a list of IDs."
            raise TypeError(errmsg)


class BaseTag(BaseModel):
    """Schema for individual tag data."""

    Id: int
    Tag: str
    Type: TagType
    Keywords: Optional[Keywords] = None

    @field_validator("Id", mode="before")
    @classmethod
    def parse_id(cls, v: int) -> int:
        """Convert 'Id' field to integer if necessary."""
        return int(v)

    @field_validator("Keywords", mode="before")
    @classmethod
    def validate_keywords(cls, v: dict | None) -> dict | None:
        """Handle the 'Keywords' field, which can be 'none' or a dict."""
        if v == "none":
            return None
        elif isinstance(v, dict):
            return v
        else:
            errmsg = "Invalid format for Keywords; expected 'none' or a dictionary."
            raise ValueError(errmsg)
