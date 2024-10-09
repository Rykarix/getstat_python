# getstat/apis/tags/__init__.py
"""Module for handling tags-related API requests."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from ...api_request import APIRequest
from . import schemas

if TYPE_CHECKING:
    from ... import GetStat


class TagsRequest:
    """Handle Tags-related API requests."""

    def __init__(self, client: GetStat) -> None:
        self.client = client

    def list(self, site_id: int, start: int = 0, results: int = 100) -> APIRequest:
        """Lists all tags in a site."""
        return APIRequest(
            self.client,
            path=schemas.TagEndpoints.list,
            params=schemas.ListRequest(site_id=site_id, start=start, results=results),
            schema_model=schemas.ListResponse,
        )

    def ranking_distributions(self, tag_id: int, from_date: str, to_date: str) -> APIRequest:
        """Gets ranking distributions for a site."""
        return APIRequest(
            self.client,
            path=schemas.TagEndpoints.ranking_distributions,
            params=schemas.RankingDistributionsRequest(
                id=tag_id,
                from_date=from_date,
                to_date=to_date,
            ),
            schema_model=schemas.RankingDistributionsResponse,
        )

    def mfd(
        self,
        tag_id: int,
        engine: Literal["google"],
    ) -> APIRequest:
        """Lists all sites with pagination."""
        return APIRequest(
            self.client,
            path=schemas.TagEndpoints.most_frequent_domains,
            params=schemas.MFDRequest(
                id=tag_id,
                engine=engine,
            ),
            schema_model=schemas.MFDResponse,
        )

    def sov(
        self,
        tag_id: int,
        from_date: str,
        to_date: str,
        *,
        results: int = 100,
        start: int = 0,
    ) -> APIRequest:
        """Lists all sites with pagination."""
        return APIRequest(
            self.client,
            path=schemas.TagEndpoints.sov,
            params=schemas.SOVRequest(
                id=tag_id,
                from_date=from_date,
                to_date=to_date,
                results=results,
                start=start,
            ),
            schema_model=schemas.SOVResponse,
        )
