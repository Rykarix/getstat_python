# getstat/apis/keywords/schemas/endpoints.py
"""Schema for keywords endpoints."""

from dataclasses import dataclass


@dataclass
class KeywordEndpoints:
    list: str = "keywords/list"
    create: str = "keywords/create"
    delete: str = "keywords/delete"
