# from pydantic import BaseModel, Field


# class SiteEndpoints(BaseModel):
#     all: str = Field(default="sites/all")
#     list: str = Field(default="sites/list")
#     ranking_distributions: str = Field(default="sites/ranking_distributions")
#     create: str = Field(default="sites/create")
#     update: str = Field(default="sites/update")
#     delete: str = Field(default="sites/delete")
#     sov: str = Field(default="sites/sov")
#     most_frequent_domains: str = Field(default="sites/most_frequent_domains")

from dataclasses import dataclass


@dataclass
class SiteEndpoints:
    all: str = "sites/all"
    list: str = "sites/list"
    ranking_distributions: str = "sites/ranking_distributions"
    create: str = "sites/create"
    update: str = "sites/update"
    delete: str = "sites/delete"
    sov: str = "sites/sov"
    most_frequent_domains: str = "sites/most_frequent_domains"
