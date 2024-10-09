# getstat/apis/projects/__init__.py
"""Module for handling project-related API requests."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ...api_request import APIRequest
from . import schemas

if TYPE_CHECKING:
    from ... import GetStat


class ProjectsRequest:
    """Handle project-related API requests."""

    def __init__(self, client: GetStat) -> None:
        self.client = client

    def list(self) -> APIRequest:
        """Lists all projects."""
        return APIRequest(
            self.client,
            path=schemas.ProjectEndpoints.list,
            params=None,
            schema_model=schemas.ListResponse,
        )

    def create(self, name: str) -> APIRequest:
        """Creates a new project with the given name."""
        return APIRequest(
            self.client,
            path=schemas.ProjectEndpoints.create,
            params=schemas.CreateRequest(name=name),
            schema_model=schemas.CreateResponse,
        )

    def update(self, project_id: int, name: str) -> APIRequest:
        """Updates the name of a project."""
        return APIRequest(
            self.client,
            path=schemas.ProjectEndpoints.update,
            params=schemas.UpdateRequest(id=project_id, name=name),
            schema_model=schemas.UpdateResponse,
        )

    def delete(self, project_id: int) -> APIRequest:
        """Deletes a project."""
        return APIRequest(
            self.client,
            path=schemas.ProjectEndpoints.delete,
            params=schemas.DeleteRequest(id=project_id),
            schema_model=schemas.DeleteResponse,
        )
