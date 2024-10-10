"""Helper functions for input/output operations."""

# ruff: noqa: G004
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from getstat.api_request import APIRequest


def fetch_or_load_parquet(
    task: APIRequest,
    levelstr: str,
    taskstr: str,
    *,
    overwrite: bool = False,
) -> pd.DataFrame:
    """Fetches data from GetStat API or loads from disk."""
    filepath = DataPath / f"{levelstr}_{taskstr}.parquet"

    if not filepath.exists() or overwrite:
        log.debug(f"Fetching {levelstr}.{taskstr}() from GetStat API...")
        df = task.execute()
        df.to_parquet(filepath)
    else:
        log.debug(f"Loading {levelstr}.{taskstr}() from disk...")
        df = pd.read_parquet(filepath)
    return df


if __name__ == "__main__":
    """Example usage of the GetStat API client."""
    import logging
    import os
    from pathlib import Path

    import pandas as pd
    from getstat import GetStat

    # === Test related vars:
    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    CWD = Path().cwd()
    DataPath = CWD / "data"
    DataPath.mkdir(parents=True, exist_ok=True)
    overwrite = False

    # === Initialise client with credentials:
    subdomain: str = os.environ.get("GETSTAT_SUBDOMAIN", None)
    apikey: str = os.environ.get("GETSTAT_APIKEY", None)
    site_id = os.environ.get("SITE_ID_TEST", None)
    project_id = os.environ.get("PROJECT_ID_TEST", None)
    tag_id = os.environ.get("TAG_ID_TEST", None)

    # Either:
    # client = GetStat(subdomain=subdomain, apikey=apikey)
    # Or, if you want to return data as a pandas DataFrame:
    client = GetStat(subdomain=subdomain, apikey=apikey, return_dataframe=True)

    LEVEL = "project"
    log.warning(f"============= {LEVEL}-level data =============")

    TASK = "list"
    task = client.projects.list()
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")

    LEVEL = "sites"
    log.warning(f"============= {LEVEL}-level data =============")

    TASK = "list"
    task = client.sites.list(project_id=project_id)
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")

    TASK = "ranking_distributions"
    task = client.sites.ranking_distributions(
        site_id=site_id,
        from_date="2024-10-01",
        to_date="2024-10-06",
    )
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")

    TASK = "sov"
    task = client.sites.sov(site_id=site_id, from_date="2024-10-01", to_date="2024-10-06")
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")

    TASK = "mfd"
    task = client.sites.mfd(site_id=site_id, engine="google")
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")

    LEVEL = "tag"
    log.warning(f"============= {LEVEL}-level data =============")

    TASK = "list"
    task = client.tags.list(site_id=site_id)
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")

    TASK = "ranking_distributions"
    task = client.tags.ranking_distributions(
        tag_id=tag_id,
        from_date="2024-10-01",
        to_date="2024-10-06",
    )
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")

    TASK = "sov"
    task = client.tags.sov(tag_id=tag_id, from_date="2024-10-01", to_date="2024-10-06")
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")

    TASK = "mfd"
    task = client.tags.mfd(tag_id=tag_id, engine="google")
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")

    LEVEL = "keyword"
    log.warning(f"============= {LEVEL}-level data =============")

    TASK = "list"
    task = client.keywords.list(site_id=site_id)
    df = fetch_or_load_parquet(task, LEVEL, TASK, overwrite=overwrite)
    log.info(f"Data for: {LEVEL}.{TASK}()")
