# getstat/apis/keywords/schemas/create.py
"""Schemas for the keywords.create() method."""

from __future__ import annotations

from pydantic import BaseModel, Field

from .base import Result


class CreateRequest(BaseModel):
    """Schema for request parameters of keywords.create()."""


class Response(BaseModel):
    """Schema for the entire response of keywords.create()."""

    response_code: int = Field(..., alias="responsecode")
    result: list[Result] = Field(..., alias="Result")


class CreateResponse(BaseModel):
    """Top-level schema for keywords.create() response."""

    response: Response = Field(..., alias="Response")
