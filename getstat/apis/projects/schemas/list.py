# getstat/apis/projects/schemas/list.py
"""Schemas for the projects.list() method."""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator

from .base import Result


class ListRequest(BaseModel):
    """Schema for the request parameters of projects.list()."""


from ...global_schemas import BaseResponseModel


class Response(BaseResponseModel):
    """Schema for the 'Response' key in projects.list()."""

    response_code: int = Field(..., alias="responsecode")
    result: list[Result] = Field(..., alias="Result")
    results_returned: int = Field(..., alias="resultsreturned")

    @field_validator("results_returned", mode="before")
    @classmethod
    def coerce_results_returned(cls, v: int | str) -> int:
        """Attempt to coerce the 'results_returned' field to an integer."""
        if isinstance(v, str):
            try:
                return int(v)
            except ValueError as e:
                errmsg = f"Unable to convert {v} to an integer."
                raise ValueError(errmsg) from e
        return v


class ListResponse(BaseModel):
    """Top-level schema for projects.list() response."""

    response: Response = Field(..., alias="Response")
