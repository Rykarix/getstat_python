# from pydantic import BaseModel, Field


# class TagEndpoints(BaseModel):
#     list: str = Field(default="tags/list")
#     ranking_distributions: str = Field(default="tags/ranking_distributions")
#     sov: str = Field(default="tags/sov")
#     most_frequent_domains: str = Field(default="tags/most_frequent_domains")

from dataclasses import dataclass


@dataclass
class TagEndpoints:
    list: str = "tags/list"
    ranking_distributions: str = "tags/ranking_distributions"
    sov: str = "tags/sov"
    most_frequent_domains: str = "tags/most_frequent_domains"
