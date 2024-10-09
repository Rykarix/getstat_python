# ruff: noqa: G004, PLR2004
from __future__ import annotations

import json
import logging
import os
import re
from pathlib import Path

import coloredlogs
import requests
from lxml import html

# === Logging:
log = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", logger=log)


def load_json(filepath: Path) -> dict:
    """Load data from a JSON file."""
    filepath = Path(filepath).absolute()
    log.debug(f"Attempting to load JSON data from: {filepath}")

    try:
        with filepath.open(mode="r", encoding="utf-8") as file:
            data = json.load(file)
            log.info(f"Data loaded from {filepath}")
    except FileNotFoundError:
        log.exception("File not found")
        raise
    except PermissionError:
        log.exception("Permission denied")
        raise
    except Exception:
        log.exception(f"Failed to load data from {filepath}")
        raise
    return data if data else {}


def save_json(data: dict, filepath: Path) -> None:
    """Save data to a JSON file."""
    filepath = Path(filepath).absolute()
    filepath.parent.mkdir(parents=True, exist_ok=True)
    log.debug(f"Attempting to save JSON data to: {filepath}")
    try:
        with filepath.open(mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        log.info(f"Data saved to {filepath}")
    except PermissionError:
        log.exception("Permission denied")
        raise
    except Exception:
        log.exception(f"Failed to save data to {filepath}")
        raise


def split_endpoint_from_search_params(url: str) -> tuple[str, str]:
    """Split the endpoint from the search parameters in a URL.

    Notes:
    - Match on the first '?' or '[' (inclusive)
    - Ignore the first character of the endpoint if it's `/`

    """
    split_result = re.split(r"[\[\?]", url, maxsplit=1)
    endpoint = split_result[0]
    search_params = split_result[1] if len(split_result) > 1 else ""
    if endpoint.startswith("/"):
        endpoint = endpoint[1:]
    return endpoint, search_params


def fetch_getstat_apis(url: str) -> dict:
    """Fetch all GetStat API endpoints and their search parameters from a URL."""
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        tree = html.fromstring(response.content)
        json_request_paragraphs = tree.xpath("//p[contains(text(), 'XML request URL:')]")
        d = {}
        for paragraph in json_request_paragraphs:
            next_sibling = paragraph.getnext()
            if next_sibling is not None and next_sibling.tag == "pre":
                url_path = next_sibling.text_content().strip()
                endpoint, search_param = split_endpoint_from_search_params(url_path)
                d[endpoint] = search_param
    return dict(sorted(d.items()))


if __name__ == "__main__":
    """Example usage of the GetStat API client."""

    CWD = Path().cwd()
    DataPath = CWD / "data"
    DataPath.mkdir(parents=True, exist_ok=True)
    overwrite = True

    filepath = DataPath / "getstat_endpoints.json"
    if not filepath.exists() or overwrite:
        log.info("Saving GetStat endpoints to disk...")
        url = "https://help.getstat.com/knowledgebase/requests-and-responses/"
        endpoints = fetch_getstat_apis(url)
        save_json(endpoints, filepath)
    else:
        log.info("Loading GetStat endpoints from disk...")
        endpoints = load_json(filepath)
    log.info(json.dumps(endpoints, indent=2))
