# getstat/apis/sov/schemas/sites.py
"""Schemas for the sov.sites() API method.

https://help.getstat.com/knowledgebase/requests-and-responses/#sovsites
SoV: Sites - This request returns the SoV score for each competitor domain that appears on the SERP for a specified site.

"""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, Field, StringConstraints, model_validator
from typing_extensions import Annotated

DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"
DateField = Annotated[str, StringConstraints(pattern=DATE_PATTERN)]


class SOVRequest(BaseModel):
    """Schema to validate the params parsed to sov.tags()."""

    id: int
    from_date: DateField
    to_date: DateField
    results: Annotated[
        int,
        Field(default=100, strict=True, le=5000, description="The number of results per page."),
    ]
    start: int | None

    @model_validator(mode="before")
    @classmethod
    def validate_dates(cls, values: dict) -> dict:
        """Check that from_date is before to_date."""

        api_limit_days = 30

        from_date_obj = date.fromisoformat(values["from_date"])
        to_date_obj = date.fromisoformat(values["to_date"])

        # to_date must be greater than from_date
        if from_date_obj > to_date_obj:
            errmsg = "from_date must be before to_date"
            raise ValueError(errmsg)

        # the timedelta has to be less than 31 days
        if (to_date_obj - from_date_obj).days > api_limit_days:
            errmsg = "The difference between from_date and to_date must be less than 31 days"
            raise ValueError(errmsg)
        return values


class Site(BaseModel):
    """Schema for the 'Site' key in sov.tags()."""

    domain: str = Field(..., alias="Domain")
    share: float = Field(..., alias="Share")
    pinned: bool = Field(..., alias="Pinned")


class ShareOfVoice(BaseModel):
    """Schema for the 'ShareOfVoice' key in sov.tags()."""

    date: datetime
    site: list[Site] = Field(..., alias="Site")


class Response(BaseModel):
    """Schema for the 'Response' key in sov.tags()."""

    response_code: int = Field(..., alias="responsecode")
    results_returned: int = Field(..., alias="resultsreturned")
    total_results: int = Field(..., alias="totalresults")
    nextpage: str | None = Field(None, alias="nextpage")
    share_of_voice: list[ShareOfVoice] = Field(..., alias="ShareOfVoice")


class SOVResponse(BaseModel):
    """Top-level schema for sov.tags() response."""

    response: Response = Field(..., alias="Response")
