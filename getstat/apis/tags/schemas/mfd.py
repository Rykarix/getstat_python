# getstat/apis/tags/schemas/mfd.py
"""Schema for the tags.mfd() API method.

https://help.getstat.com/knowledgebase/requests-and-responses/#frequenttags
Most Frequent Domains: Tags This request returns the competitor domains most frequently in the top 10 for the tag specified for the engine specified.

"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Site(BaseModel):
    """Schema for the 'Site' key in tags.mfd()."""

    domain: str = Field(..., alias="Domain")
    top_ten_results: int = Field(..., alias="TopTenResults")
    results_analyzed: int = Field(..., alias="ResultsAnalyzed")
    coverage: float = Field(..., alias="Coverage")
    analyzed_on: datetime = Field(..., alias="AnalyzedOn")


class Response(BaseModel):
    """Schema for the 'Response' key in tags.mfd()."""

    response_code: int = Field(..., alias="responsecode")
    site: list[Site] = Field(..., alias="Site")


class MFDRequest(BaseModel):
    """Schema to validate the params parsed to tags.mfd()."""

    id: int
    engine: str


class MFDResponse(BaseModel):
    """Top-level schema for tags.mfd() response."""

    response: Response = Field(..., alias="Response")
