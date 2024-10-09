# getstat/apis/projects/schemas/delete.py
"""Schemas for the projects.delete() method."""

from __future__ import annotations

from pydantic import BaseModel, Field, model_validator


class DeleteRequest(BaseModel):
    """Schema to validate the params parsed to projects.delete()."""

    project_id: int = Field(
        ...,
        description="The ID of the project to delete.",
        example=123,
        alias="ProjectId",
    )


class Result(BaseModel):
    """Schema for project deletion result."""

    id: int = Field(..., alias="Id")

    @model_validator(mode="before")
    @classmethod
    def convert_fields(cls, values: dict) -> dict:
        """Convert fields to correct types."""
        if isinstance(values.get("Id"), str):
            values["Id"] = int(values["Id"])
        return values


class Response(BaseModel):
    """Schema for the 'Response' key in projects.delete()."""

    response_code: int = Field(..., alias="responsecode")
    result: list[Result] = Field(..., alias="Result")


class DeleteResponse(BaseModel):
    """Top-level schema for projects.delete() response."""

    response: Response = Field(..., alias="Response")
