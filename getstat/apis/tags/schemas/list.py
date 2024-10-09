# getstat/apis/tags/schema/list.py

"""Schemas for the tags.list() method.

https://help.getstat.com/knowledgebase/requests-and-responses/#tagslist
Tags: List - This request returns all tags saved under the specified site.

"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator


class ListRequest(BaseModel):
    """Schema to validate the params parsed to tags.list()."""

    site_id: int
    start: int | None
    results: int | None


class BaseConfigModel(BaseModel):
    """Base model with shared configuration."""

    model_config = {
        "populate_by_name": True,
    }


class Keywords(BaseConfigModel):
    """Schema for the 'Keywords' field in a tags.list()."""

    id_list: list[int] = Field(..., alias="Id")


class Result(BaseConfigModel):
    """Schema For the 'Result' key in tags.list()."""

    id: int = Field(..., alias="Id")
    tag: str = Field(..., alias="Tag")
    type: str = Field(..., alias="Type")
    keywords: Keywords | None = Field(None, alias="Keywords")

    @field_validator("keywords", mode="before")
    @classmethod
    def parse_keywords(cls, value: Keywords | None) -> Keywords | None:
        """Convert 'Keywords' field to None if 'none'."""
        if value == "none":
            return None
        return value


class Response(BaseConfigModel):
    """Schema for the 'Response' key in tags.list()."""

    response_code: int = Field(..., alias="responsecode")
    results_returned: int = Field(..., alias="resultsreturned")
    total_results: int = Field(..., alias="totalresults")
    result: list[Result] = Field(..., alias="Result")
    next_page: str | None = Field(None, alias="nextpage")


class ListResponse(BaseConfigModel):
    """Top-level schema for tags.list() response."""

    response: Response = Field(..., alias="Response")
