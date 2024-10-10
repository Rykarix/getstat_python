# getstat/apis/projects/schemas/create.py
"""Schemas for the projects.create() method."""

from __future__ import annotations

from pydantic import BaseModel, Field, StringConstraints
from typing_extensions import Annotated

from .base import Result


class CreateRequest(BaseModel):
    """Schema for request parameters of projects.create()."""

    name: Annotated[str | None, StringConstraints(strip_whitespace=True)] = Field(
        ...,
        description="The name of the project.",
        example="New Project",
    )


class Response(BaseModel):
    """Schema for the entire response of projects.create()."""

    response_code: int = Field(..., alias="responsecode")
    result: list[Result] = Field(..., alias="Result")


class CreateResponse(BaseModel):
    """Top-level schema for projects.create() response."""

    response: Response = Field(..., alias="Response")
