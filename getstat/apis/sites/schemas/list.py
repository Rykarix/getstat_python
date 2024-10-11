# getstat/apis/sites/schemas/list.py
"""Schemas for the sites.list() API method.

https://help.getstat.com/knowledgebase/requests-and-responses/#siteslist
Sites: List - This request returns all sites saved under the specified project id.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .base import ListResult


class ListRequest(BaseModel):
    """Schema to validate the params parsed to sites.list()."""

    project_id: int = Field(
        ...,
        description="The ID of the project to list sites for.",
        example=123,
    )


from ...global_schemas import BaseResponseModel


class Response(BaseResponseModel):
    """Schema for the 'Response' key in sites.list()."""

    response_code: int = Field(..., alias="responsecode")
    result: list[ListResult] = Field(..., alias="Result")


class ListResponse(BaseModel):
    """Top-level schema for sites.list() response."""

    response: Response = Field(..., alias="Response")
