# getstat/apis/sites/schemas/update.py
"""Schemas for the sites.update() method.

https://help.getstat.com/knowledgebase/requests-and-responses/#sitesupdate
Sites: Update - This request updates a site under the specified id.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, HttpUrl

from .base import CreateOrUpdateResult


class UpdateRequest(BaseModel):
    """Schema to validate the params parsed to sites.update()."""

    id: int
    url: HttpUrl | None
    title: str | None
    drop_www_prefix: bool | None
    drop_directories: bool | None


from ...global_schemas import BaseResponseModel


class Response(BaseResponseModel):
    """Schema for the entire response of sites.update()."""

    response_code: int = Field(..., alias="responsecode")
    result: list[CreateOrUpdateResult] = Field(..., alias="Result")


class UpdateResponse(BaseModel):
    """Top-level schema for sites.update() response."""

    response: Response = Field(..., alias="Response")
