# getstat/apis/keywords/schemas/base.py
"""Base schema for keyword data."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


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


class KeywordRankingGoogle(BaseModel):
    """Schema for Google keyword ranking details."""

    rank: int = Field(..., alias="Rank")
    base_rank: int = Field(..., alias="BaseRank")
    url: str = Field(..., alias="Url")


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
