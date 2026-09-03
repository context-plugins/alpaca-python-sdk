from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .assets import Assets, AssetsDict


class Watchlist(SdkBaseModel):
    """The watchlist API provides CRUD operation for the account’s watchlist. An account can have multiple watchlists
    and each is uniquely identified by id but can also be addressed by user-defined name. Each watchlist is an ordered
    list of assets."""

    id: UUID
    """watchlist id"""

    account_id: UUID
    """account ID"""

    created_at: RFC3339DateTime
    updated_at: RFC3339DateTime
    name: str
    """user-defined watchlist name (up to 64 characters)"""

    assets: Optional[list[Assets]] = UNSET
    """the content of this watchlist, in the order as registered by the client"""


class WatchlistDict(TypedDict):
    id: UUID
    account_id: UUID
    created_at: RFC3339DateTime
    updated_at: RFC3339DateTime
    name: str
    assets: NotRequired[list[Assets | AssetsDict]]
