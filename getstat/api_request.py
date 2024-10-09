# getstat/api_request.py

from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
from pydantic import BaseModel

if TYPE_CHECKING:
    from . import GetStat


class APIRequest:
    """Represents an API request that can be executed."""

    def __init__(
        self,
        client: GetStat,
        path: str,
        *,
        params: BaseModel | None = None,
        schema_model: type[BaseModel] | None = None,
    ) -> None:
        self.client = client
        if params:
            self.url = self.client.prepare_url(path, params.model_dump())
        else:
            self.url = self.client.prepare_url(path)
        self.schema_model = schema_model

    def execute(self) -> list | dict | str | pd.DataFrame:
        """Executes the request and returns the response."""
        return self.client.execute(self.url, schema_model=self.schema_model)


__all__ = [
    "APIRequest",
]
