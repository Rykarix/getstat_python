# getstat/apis/keywords/schemas/list.py
"""Schemas for the keywords.list() method."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated


class KeywordStats(BaseModel):
    """Schema for keyword statistics."""

    advertiser_competition: float = Field(..., alias="AdvertiserCompetition")
    global_search_volume: int = Field(..., alias="GlobalSearchVolume")
    regional_search_volume: int = Field(..., alias="RegionalSearchVolume")
    local_search_trends_by_month: dict[str, int | None] = Field(
        ...,
        alias="LocalSearchTrendsByMonth",
    )
    cpc: float = Field(..., alias="CPC")

    @field_validator("local_search_trends_by_month", mode="before")
    @classmethod
    def parse_search_trends(cls, v: dict[str, int | None]) -> dict[str, int | None]:
        """Convert the search trends to integers."""
        return {k: None if value == "-" else int(value) for k, value in v.items()}


class KeywordRankingGoogle(BaseModel):
    """Schema for Google keyword ranking details."""

    rank: int | None = Field(None, alias="Rank")
    base_rank: int | None = Field(None, alias="BaseRank")
    url: str | None = Field(None, alias="Url")


class KeywordRanking(BaseModel):
    """Schema for keyword ranking."""

    date: datetime
    google: KeywordRankingGoogle = Field(..., alias="Google")


class Result(BaseModel):
    """Schema for the 'Result' key of keywords.list()."""

    id: int = Field(..., alias="Id")
    keyword: str = Field(..., alias="Keyword")
    keyword_market: str = Field(..., alias="KeywordMarket")
    keyword_device: str = Field(..., alias="KeywordDevice")
    keyword_tags: str = Field(..., alias="KeywordTags")
    keyword_stats: KeywordStats = Field(..., alias="KeywordStats")
    keyword_ranking: KeywordRanking = Field(..., alias="KeywordRanking")
    created_at: datetime = Field(..., alias="CreatedAt")
    request_url: str = Field(..., alias="RequestUrl")
    keyword_location: str | None = Field(None, alias="KeywordLocation")
    keyword_translation: str | None = Field(None, alias="KeywordTranslation")


class ListRequest(BaseModel):
    """Schema for the request parameters of keywords.list()."""

    site_id: int
    start: int
    results: Annotated[
        int,
        Field(
            default=100,
            strict=True,
            le=5000,  # TODO: Check if this is correct for this endpoint
            description="The number of results per page.",
        ),
    ]


class Response(BaseModel):
    """Schema for the 'Response' key in keywords.list()."""

    response_code: int = Field(..., alias="responsecode")
    results_returned: int = Field(..., alias="resultsreturned")
    total_results: int = Field(..., alias="totalresults")
    next_page: str | None = Field(None, alias="nextpage")
    result: list[Result] = Field(..., alias="Result")


class ListResponse(BaseModel):
    """Top-level schema for keywords.list() response."""

    response: Response = Field(..., alias="Response")


def fake_data() -> dict:
    """A 'typical' json response for keywords.list()."""
    return {
        "Response": {
            "responsecode": "200",
            "resultsreturned": "63",
            "totalresults": "150",
            "nextpage": "/keywords/list?site_id=1&start=1000&format=json",
            "Result": [
                {
                    "Id": "11",
                    "Keyword": "black celebrity gossip",
                    "KeywordMarket": "US-en",
                    "KeywordLocation": "Boston",
                    "KeywordDevice": "Smartphone",
                    "KeywordTranslation": "potins de célébrités noires",
                    "KeywordTags": "gossip",
                    "KeywordStats": {
                        "AdvertiserCompetition": "0.86748",
                        "GlobalSearchVolume": "80000",
                        "RegionalSearchVolume": "54000",
                        "LocalSearchTrendsByMonth": {
                            "Oct": "-",
                            "Sep": "49500",
                            "Aug": "60500",
                            "Jul": "49500",
                            "Jun": "49500",
                            "May": "49500",
                            "Apr": "49500",
                            "Mar": "49500",
                            "Feb": "49500",
                            "Jan": "49500",
                            "Dec": "40500",
                            "Nov": "49500",
                        },
                        "CPC": "1.42",
                    },
                    "KeywordRanking": {
                        "date": "2014-07-09",
                        "Google": {
                            "Rank": "1",
                            "BaseRank": "1",
                            "Url": "www.zillow.com/mortgage-rates/ca/",
                        },
                    },
                    "CreatedAt": "2011-01-25",
                    "RequestUrl": "/rankings?keyword_id=11&format=json&from_date=2011-01-25&to_date=",
                },
            ],
        },
    }


def validation_test(schema_model: type[BaseModel], json_data: dict) -> BaseModel:
    """Test the schema validation of the given json data."""
    return schema_model.model_validate(json_data)


if __name__ == "__main__":
    fake_json_data = fake_data()
    validate = validation_test(ListResponse, fake_json_data)
