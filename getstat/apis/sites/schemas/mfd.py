# getstat/apis/sites/schemas/mfd.py
"""Schemas for the sites.mfd() API method.

https://help.getstat.com/knowledgebase/requests-and-responses/#frequentsites
Most Frequent Domains: Sites - This request returns the competitor domains most frequently in the top 10 for the site specified for the engine specified.


"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Site(BaseModel):
    """Schema for the 'Site' key in mfd.sites() & mfd.tags()."""

    domain: str = Field(..., alias="Domain")
    top_ten_results: int = Field(..., alias="TopTenResults")
    results_analyzed: int = Field(..., alias="ResultsAnalyzed")
    coverage: float = Field(..., alias="Coverage")
    analyzed_on: datetime = Field(..., alias="AnalyzedOn")


from ...global_schemas import BaseResponseModel


class Response(BaseResponseModel):
    """Schema for the 'Response' key in mfd.sites() & mfd.tags()."""

    response_code: int = Field(..., alias="responsecode")
    site: list[Site] = Field(..., alias="Site")


class MFDRequest(BaseModel):
    """Schema to validate the params parsed to mfd.sites()."""

    id: int
    engine: str


class MFDResponse(BaseModel):
    """Top-level schema for mfd.sites() response."""

    response: Response = Field(..., alias="Response")
