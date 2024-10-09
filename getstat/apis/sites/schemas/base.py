# getstat/apis/sites/schemas/base.py
"""Schemas for GetStat Sites API."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field, field_validator

if TYPE_CHECKING:
    from pandas._libs.tslibs.nattype import NaTType
    from pydantic import ValidationInfo

from ....helpers import validation


class ListResult(BaseModel):
    """Schema For the 'Result' key in sites.list()."""

    id: int = Field(..., alias="Id")
    title: str = Field(..., alias="Title")
    url: str = Field(..., alias="Url")
    total_keywords: int = Field(..., alias="TotalKeywords")
    created_at: datetime = Field(..., alias="CreatedAt")
    updated_at: datetime = Field(..., alias="UpdatedAt")
    request_url: str = Field(..., alias="RequestUrl")
    synced: int = Field(..., alias="Synced")
    folder_id: int = Field(..., alias="FolderId")
    folder_name: str | None = Field(None, alias="FolderName")

    @field_validator("*", mode="before")
    @classmethod
    def check_na_validator(cls, v: str, info: ValidationInfo) -> float | NaTType | None:
        """Use the helper function for 'N/A' validation."""
        field_type = cls.model_fields[info.field_name].annotation
        return validation.check_na(v, field_type)


class AllResult(ListResult):
    """Schema for the 'Result' key in sites.all()."""

    project_id: int | None = Field(-1, alias="ProjectId")

    @field_validator("*", mode="before")
    @classmethod
    def check_na_validator(cls, v: str, info: ValidationInfo) -> float | NaTType | None:
        """Use the helper function for 'N/A' validation."""
        field_type = cls.model_fields[info.field_name].annotation
        return validation.check_na(v, field_type)


class CreateOrUpdateResult(BaseModel):
    """Schema For the 'Result' key in sites.create() or sites.update()."""

    id: int = Field(..., alias="Id")
    project_id: int = Field(..., alias="ProjectId")
    title: str = Field(..., alias="Title")
    url: str = Field(..., alias="Url")
    drop_www_prefix: bool = Field(..., alias="DropWWWPrefix")
    drop_directories: bool = Field(..., alias="DropDirectories")
    created_at: datetime = Field(..., alias="CreatedAt")
    updated_at: datetime | None = Field(..., alias="UpdatedAt")

    # TODO: TEST THIS FUNCTION
    @field_validator("*", mode="before")
    @classmethod
    def check_na_validator(cls, v: str, info: ValidationInfo) -> float | NaTType | None:
        """Use the helper function for 'N/A' validation."""
        field_type = cls.model_fields[info.field_name].annotation
        return validation.check_na(v, field_type)
