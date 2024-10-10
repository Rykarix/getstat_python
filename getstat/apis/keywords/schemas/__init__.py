# getstat/apis/Keywords/schemass/__init__.py
"""Module with schemass for Keywords."""

from .create import CreateRequest, CreateResponse
from .delete import DeleteRequest, DeleteResponse
from .endpoints import KeywordEndpoints
from .list import ListRequest, ListResponse

__all__ = [
    "KeywordEndpoints",
    "ListResponse",
    "ListRequest",
    "CreateResponse",
    "CreateRequest",
    "UpdateResponse",
    "UpdateRequest",
    "DeleteRequest",
    "DeleteResponse",
]
