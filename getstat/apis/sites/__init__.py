# getstat/apis/sites/__init__.py
"""Module for handling sites-related API requests."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from ...api_request import APIRequest
from . import schemas

if TYPE_CHECKING:
    from ... import GetStat


class SitesRequest:
    """Handle sites-related API requests."""

    def __init__(self, client: GetStat) -> None:
        self.client = client

    def list(self, project_id: int) -> APIRequest:
        """Lists all sites in a project."""
        return APIRequest(
            self.client,
            path=schemas.SiteEndpoints.list,
            params=schemas.ListRequest(project_id=project_id),
            schema_model=schemas.ListResponse,
        )

    def all(
        self,
        start: int = 0,
        results: int = 100,
    ) -> APIRequest:
        """Lists all sites with pagination."""
        return APIRequest(
            self.client,
            path=schemas.SiteEndpoints.all,
            params=schemas.AllRequest(start=start, results=results),
            schema_model=schemas.AllResponse,
        )

    def create(
        self,
        project_id: int,
        site_url: str,
        *,
        drop_www_prefix: bool = True,
        drop_directories: bool = False,
    ) -> APIRequest:
        """Creates a new site in a project."""
        return APIRequest(
            self.client,
            path=schemas.SiteEndpoints.create,
            params=schemas.CreateRequest(
                project_id=project_id,
                url=site_url,
                drop_www_prefix=drop_www_prefix,
                drop_directories=drop_directories,
            ),
            schema_model=schemas.CreateResponse,
        )

    def update(
        self,
        site_id: int,
        url: str | None = None,
        title: str | None = None,
        drop_www_prefix: bool | None = None,
        drop_directories: bool | None = None,
    ) -> APIRequest:
        """Updates a site's information."""

        return APIRequest(
            self.client,
            path=schemas.SiteEndpoints.update,
            params=schemas.UpdateRequest(
                id=site_id,
                url=url,
                title=title,
                drop_www_prefix=drop_www_prefix,
                drop_directories=drop_directories,
            ),
            schema_model=schemas.UpdateResponse,
        )

    def ranking_distributions(
        self,
        site_id: int,
        from_date: str,
        to_date: str,
    ) -> APIRequest:
        """Gets ranking distributions for a site."""
        return APIRequest(
            self.client,
            path=schemas.SiteEndpoints.ranking_distributions,
            params=schemas.RankingDistributionsRequest(
                id=site_id,
                from_date=from_date,
                to_date=to_date,
            ),
            schema_model=schemas.RankingDistributionsResponse,
        )

    def delete(
        self,
        site_id: int,
    ) -> APIRequest:
        """Deletes a site."""
        return APIRequest(
            self.client,
            path=schemas.SiteEndpoints.delete,
            params=schemas.DeleteRequest(id=site_id),
            schema_model=schemas.DeleteResponse,
        )

    def sov(
        self,
        site_id: int,
        from_date: str,
        to_date: str,
        *,
        results: int = 100,
        start: int = 0,
    ) -> APIRequest:
        """Returns the Share of Voice for each competitor domain that appears on the SERP for a specified site."""
        return APIRequest(
            self.client,
            path=schemas.SiteEndpoints.sov,
            params=schemas.SOVRequest(
                id=site_id,
                from_date=from_date,
                to_date=to_date,
                results=results,
                start=start,
            ),
            schema_model=schemas.SOVResponse,
        )

    def mfd(
        self,
        site_id: int,
        engine: Literal["google"],
    ) -> APIRequest:
        """Returns the competitor domains most frequently in the top 10 for the site specified for the engine specified."""
        return APIRequest(
            self.client,
            path=schemas.SiteEndpoints.most_frequent_domains,
            params=schemas.MFDRequest(
                id=site_id,
                engine=engine,
            ),
            schema_model=schemas.MFDResponse,
        )
