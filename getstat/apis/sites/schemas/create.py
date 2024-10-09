# getstat/apis/sites/schemas/create.py
"""Schemas for the sites.create() method.

https://help.getstat.com/knowledgebase/requests-and-responses/#sitescreate
Sites: Create - This request creates a new site under the specified project id. When a site is created, it is automatically placed within a folder called “api” within your chosen project.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, HttpUrl

from .base import CreateOrUpdateResult


class CreateRequest(BaseModel):
    """Schema to validate the params parsed to sites.create()."""

    project_id: int
    url: HttpUrl
    drop_www_prefix: bool
    drop_directories: bool


class Response(BaseModel):
    """Schema for the 'Response' key in sites.create()."""

    responsecode: str
    result: list[CreateOrUpdateResult] = Field(..., alias="Result")


class CreateResponse(BaseModel):
    """Top-level schema for sites.create() response."""

    response: Response = Field(..., alias="Response")
