from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PostWatchlistRequest(SdkBaseModel):
    """Request format used for creating a new watchlist or updating an existing watchlist with a set of assets and
    name."""

    name: str
    symbols: Optional[list[str | None]] = UNSET


class PostWatchlistRequestDict(TypedDict):
    name: str
    symbols: NotRequired[list[str | None]]
