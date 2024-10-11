# getstat/apis/sites/schemas/ranking_distributions.py
"""Schema for the sites.ranking_distributions() API method.

https://help.getstat.com/knowledgebase/requests-and-responses/#sitesranking
Sites: Ranking Distributions - This request returns all ranking distribution records for Google for a site with the specified id.
"""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, Field, StringConstraints, model_validator
from typing_extensions import Annotated

DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"
DateField = Annotated[str, StringConstraints(pattern=DATE_PATTERN)]


class RankingDistributionsRequest(BaseModel):
    """Schema to validate the params parsed to sites.ranking_distributions()."""

    id: int
    from_date: DateField
    to_date: DateField

    @model_validator(mode="before")
    @classmethod
    def validate_dates(cls, values: dict) -> dict:
        """Check that from_date is before to_date."""

        from_date_obj = date.fromisoformat(values["from_date"])
        to_date_obj = date.fromisoformat(values["to_date"])
        if from_date_obj > to_date_obj:
            errmsg = "from_date must be before to_date"
            raise ValueError(errmsg)
        return values


class RankingCounts(BaseModel):
    """Schema for the ranking counts within "Google" and "GoogleBaseRank" keys of sites.ranking_distributions()."""

    one: int = Field(..., alias="One")
    two: int = Field(..., alias="Two")
    three: int = Field(..., alias="Three")
    four: int = Field(..., alias="Four")
    five: int = Field(..., alias="Five")
    six_to_ten: int = Field(..., alias="SixToTen")
    eleven_to_twenty: int = Field(..., alias="ElevenToTwenty")
    twenty_one_to_thirty: int = Field(..., alias="TwentyOneToThirty")
    thirty_one_to_forty: int = Field(..., alias="ThirtyOneToForty")
    forty_one_to_fifty: int = Field(..., alias="FortyOneToFifty")
    fifty_one_to_hundred: int = Field(..., alias="FiftyOneToHundred")
    non_ranking: int = Field(..., alias="NonRanking")


class RankDistributionEntry(BaseModel):
    """Schema for the "RankDistribution" key in sites.ranking_distributions()."""

    google: RankingCounts = Field(..., alias="Google")
    google_base_rank: RankingCounts = Field(..., alias="GoogleBaseRank")
    date: datetime = Field(..., alias="date")


from ...global_schemas import BaseResponseModel


class Response(BaseResponseModel):
    """Schema for the 'Response' key in sites.ranking_distributions()."""

    response_code: int = Field(..., alias="responsecode")
    rank_distribution: list[RankDistributionEntry] = Field(..., alias="RankDistribution")


class RankingDistributionsResponse(BaseModel):
    """Top-level schema for sites.ranking_distributions() response."""

    response: Response = Field(..., alias="Response")
