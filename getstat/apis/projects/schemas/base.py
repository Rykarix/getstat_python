# getstat/apis/projects/schemas/base.py
"""Base schema for project data."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Result(BaseModel):
    """Schema for individual project data."""

    id: int = Field(..., alias="Id")
    name: str = Field(..., alias="Name")
    created_at: datetime = Field(..., alias="CreatedAt")
    updated_at: datetime = Field(..., alias="UpdatedAt")
    request_url: str = Field(..., alias="RequestUrl")
    total_sites: int | None = Field(None, alias="TotalSites")
