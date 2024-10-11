# getstat/apis/sites/schemas/all.py
"""Schemas for the sites.all() API method.

https://help.getstat.com/knowledgebase/requests-and-responses/#sitesall
Sites: All - This request returns all sites saved under your account.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .base import AllResult


class AllRequest(BaseModel):
    """Schema to validate the params parsed to sites.all()."""

    start: int = Field(
        ...,
        description="The index of the first result to return.",
        example=0,
        alias="start",
    )
    results: int = Field(
        ...,
        description="The number of results to return.",
        example=100,
        alias="results",
    )


from ...global_schemas import BaseResponseModel


class Response(BaseResponseModel):
    """Schema for the 'Response' key in sites.all()."""

    response_code: int = Field(..., alias="responsecode")
    results_returned: int = Field(..., alias="resultsreturned")
    total_results: int = Field(..., alias="totalresults")
    result: list[AllResult] = Field(..., alias="Result")
    next_page: str | None = Field(None, alias="nextpage")


class AllResponse(BaseModel):
    """Top-level schema for sites.all() response."""

    response: Response = Field(..., alias="Response")
