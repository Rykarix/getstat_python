# getstat/apis/projects/schemass/__init__.py
"""Module with schemass for projects."""

from .create import CreateRequest, CreateResponse
from .delete import DeleteRequest, DeleteResponse
from .endpoints import ProjectEndpoints
from .list import ListRequest, ListResponse
from .update import UpdateRequest, UpdateResponse

__all__ = [
    "ProjectEndpoints",
    "ListResponse",
    "ListRequest",
    "CreateResponse",
    "CreateRequest",
    "UpdateResponse",
    "UpdateRequest",
    "DeleteRequest",
    "DeleteResponse",
]
