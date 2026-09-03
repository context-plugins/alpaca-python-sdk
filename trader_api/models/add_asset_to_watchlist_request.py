from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddAssetToWatchlistRequest(SdkBaseModel):
    """Append an asset for the symbol to the end of watchlist asset list"""

    symbol: Optional[str] = UNSET
    """symbol name to append to watchlist"""


class AddAssetToWatchlistRequestDict(TypedDict):
    symbol: NotRequired[str]
