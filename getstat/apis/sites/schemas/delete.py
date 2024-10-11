# getstat/apis/sites/schemas/delete.py
"""Schemas for the sites.delete() method.

https://help.getstat.com/knowledgebase/requests-and-responses/#sitesdelete
Sites: Delete - This request deletes a site under the specified id.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class DeleteRequest(BaseModel):
    """Schema to validate the params parsed to sites.delete()."""

    # TODO


class DeleteResult(BaseModel):
    """Schema for the 'Result' key in sites.delete()."""

    id: int = Field(..., alias="Id")


from ...global_schemas import BaseResponseModel


class Response(BaseResponseModel):
    """Schema for the "Response" key in sites.delete()."""

    response_code: int = Field(..., alias="responsecode")
    result: DeleteResult = Field(..., alias="Result")


class DeleteResponse(BaseModel):
    """Top-level schema for sites.delete() response."""

    response: Response = Field(..., alias="Response")
