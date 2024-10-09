# getstat/helpers/validation.py
"""Validation helper functions for the GetStat API."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

import numpy as np
import pandas as pd

if TYPE_CHECKING:
    from pandas._libs.tslibs.nattype import NaTType


def check_na(v: str, field_type: type) -> float | NaTType | None:
    """Convert 'N/A' values based on the field type."""
    if isinstance(v, str) and v == "N/A":
        # If it's a UnionType, just get the first type as the 2nd will be None
        if hasattr(field_type, "__args__"):
            field_type = field_type.__args__[0]
        if field_type is int:
            return -1
        elif field_type is float:
            return np.nan
        elif field_type is datetime:
            return pd.NaT
        elif field_type is str:
            return None
        else:
            return v
    return v
