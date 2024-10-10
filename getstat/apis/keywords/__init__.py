# getstat/apis/keyword/__init__.py
"""Module for handling keyword-related API requests."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ...api_request import APIRequest
from . import schemas

if TYPE_CHECKING:
    from ... import GetStat


class KeywordsRequest:
    """Handle Keyword-related API requests."""

    def __init__(self, client: GetStat) -> None:
        self.client = client

    def list(self, site_id: int, start: int = 0, results: int = 100) -> APIRequest:
        """Lists all Keywords."""
        return APIRequest(
            self.client,
            path=schemas.KeywordEndpoints.list,
            params=schemas.ListRequest(site_id=site_id, start=start, limit=results),
            schema_model=schemas.ListResponse,
        )

    def create(self, name: str) -> APIRequest:
        """Creates a new Keyword with the given name."""
        return APIRequest(
            self.client,
            path=schemas.KeywordEndpoints.create,
            params=schemas.CreateRequest(name=name),
            schema_model=schemas.CreateResponse,
        )

    def delete(self, Keyword_id: int) -> APIRequest:
        """Deletes a Keyword."""
        return APIRequest(
            self.client,
            path=schemas.KeywordEndpoints.delete,
            params=schemas.DeleteRequest(id=Keyword_id),
            schema_model=schemas.DeleteResponse,
        )
