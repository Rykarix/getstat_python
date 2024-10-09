# getstat/apis/projects/schemas/update.py
"""Schemas for the projects.update() method."""

from __future__ import annotations

from pydantic import BaseModel, Field

from .base import Result


class UpdateRequest(BaseModel):
    """Schema for the request parameters of projects.update()."""

    # TODO


class Response(BaseModel):
    """Schema for the 'Response' key in projects.update()."""

    response_code: int = Field(..., alias="responsecode")
    result: list[Result] = Field(..., alias="Result")


class UpdateResponse(BaseModel):
    """Top-level schema for projects.update() response."""

    response: Response = Field(..., alias="Response")
