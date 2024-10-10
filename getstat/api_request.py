# getstat/api_request.py
# ruff: noqa: ARG001, N802

from __future__ import annotations

import inspect
import types
from functools import wraps
from typing import TYPE_CHECKING, Callable

import pandas as pd
from hide_from_traceback import hide_from_traceback
from pydantic import BaseModel

if TYPE_CHECKING:
    from . import GetStat


def notimplemented(func: Callable) -> Callable:
    """Decorator to raise NotImplementedError when a function is called."""

    errmsg = f"'{func.__name__}' is not yet implemented."
    stack = inspect.stack()
    caller_frame = stack[1]
    frame = caller_frame.frame
    tb = types.TracebackType(
        tb_next=None,
        tb_frame=frame,
        tb_lasti=0,
        tb_lineno=frame.f_lineno,
    )
    e = NotImplementedError(errmsg)

    @wraps(func)
    @hide_from_traceback
    def wrapper(*args: dict, **kwargs: dict) -> wrapper:
        raise e.with_traceback(tb)

    return wrapper


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
