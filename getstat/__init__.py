# getstat/__init__.py

"""Module to interact with GetStat API.

Useful links:
GetStat API Documentation
- https://help.getstat.com/knowledgebase/requests-and-responses/

Ada / can-ada documentation (WHATWG URL compliant url parser):
- https://www.ada-url.com/
- https://pypi.org/project/can-ada/
"""

from __future__ import annotations

import json
from typing import Any

import pandas as pd
import requests
from ada_url import URL, URLSearchParams, join_url
from pydantic import BaseModel

from .apis.projects import ProjectsRequest
from .apis.sites import SitesRequest
from .apis.tags import TagsRequest


class GetStat:
    """GetStat API client."""

    def __init__(
        self,
        subdomain: str,
        apikey: str,
        *,
        return_dataframe: bool = False,
        respond_in_json: bool = True,
    ) -> None:
        """Initialize the GetStat API client.

        Args:
        ----
            subdomain (str): The subdomain for the GetStat API.
            apikey (str): The API key for the GetStat API.
            return_dataframe (bool): Whether to return response data as a dictionary or a pandas DataFrame.
            respond_in_json (bool): Whether to request data in JSON or XML format.

        """
        if not subdomain or not apikey:
            errmsg = "Subdomain and API key must be provided."
            raise ValueError(errmsg)

        base_url_str = f"http://{subdomain}.getstat.com/api/v2/{apikey}/"
        self.baseurl: URL = URL(base_url_str)
        self.respond_in_json: bool = respond_in_json
        self.return_dataframe: bool = return_dataframe
        self.projects = ProjectsRequest(self)
        self.sites = SitesRequest(self)
        self.tags = TagsRequest(self)

    def add_query_params(self, url: URL, params: dict[str, Any]) -> URL:
        """Adds query parameters to a URL."""
        search_params = URLSearchParams(url.search[1:]) if url.search else URLSearchParams("")

        for key, value in params.items():
            search_params.append(key, str(value))

        url.search = "?" + str(search_params)
        return url

    def prepare_url(self, path: str, params: dict[str, Any] | None = None) -> URL:
        """Constructs a URL with the given path and query parameters."""
        base_url = self.baseurl.href
        url_str = join_url(base_url, path)
        url = URL(url_str)
        if params:
            url = self.add_query_params(url, params)
        if self.respond_in_json:
            url = self.add_query_params(url, {"format": "json"})
        return url

    def execute(
        self,
        url: URL,
        *,
        schema_model: BaseModel | None = None,
    ) -> list | dict | str | pd.DataFrame:
        """Executes the HTTP GET request to the given URL and returns the response."""

        response = requests.get(url.href, timeout=30)
        # Handle errors
        response.raise_for_status()
        if list(response.json().keys()) == ["Result"]:
            errmsg = response.json()["Result"]
            raise ValueError(errmsg)

        if self.respond_in_json:
            json_data = json.loads(response.text)
            if self.return_dataframe:
                if schema_model is None:
                    errmsg = "A schema_model must be provided when dataframe=True."
                    raise ValueError(errmsg)
                return self.schema_to_dataframe(schema_model, json_data)
            else:
                return json_data
        else:
            return response.text

    def schema_to_dataframe(self, schema_model: type[BaseModel], json_data: dict) -> pd.DataFrame:
        """Converts JSON data to a pandas DataFrame using the provided schema model."""
        validated_data = schema_model.model_validate(json_data)
        response = validated_data.response
        data_list = None
        if hasattr(response, "result"):
            data_list = response.result
        elif hasattr(response, "rank_distribution"):
            data_list = response.rank_distribution
        elif hasattr(response, "share_of_voice"):
            data_list = response.share_of_voice
        elif hasattr(response, "site"):
            data_list = response.site
        else:
            errmsg = "Could not find expected data in the response."
            raise ValueError(errmsg)
        data_for_df = [item.model_dump() for item in data_list]
        return pd.DataFrame(data_for_df)


__all__ = [
    "GetStat",
]
