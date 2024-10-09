# getstat/apis/projects/schemas/endpoints.py
"""Schema for project endpoints."""

from dataclasses import dataclass


@dataclass
class ProjectEndpoints:
    list: str = "projects/list"
    create: str = "projects/create"
    update: str = "projects/update"
    delete: str = "projects/delete"
