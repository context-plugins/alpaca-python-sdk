from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.asset_class import AssetClassOrStr
from .enums.exchange import ExchangeOrStr


class Position(SdkBaseModel):
    """The positions API provides information about an account’s current open positions. The response will include
    information such as cost basis, shares traded, and market value, which will be updated live as price information is
    updated. Once a position is closed, it will no longer be queryable through this API."""

    asset_id: UUID
    """Asset ID"""

    symbol: str
    """Symbol name of the asset"""

    exchange: ExchangeOrStr
    """Represents the current exchanges Alpaca supports. List is currently:

    - AMEX
    - ARCA
    - BATS
    - NYSE
    - NASDAQ
    - NYSEARCA
    - OTC"""

    asset_class: AssetClassOrStr
    """Represents what class of asset this is. Currently only supports ``us_equity`` or ``crypto``"""

    avg_entry_price: str
    """Average entry price of the position"""

    qty: str
    """The number of shares"""

    qty_available: Optional[str] = UNSET
    """Total number of shares available minus open orders"""

    side: str
    """“long”"""

    market_value: str
    """Total dollar amount of the position"""

    cost_basis: str
    """Total cost basis in dollar"""

    unrealized_pl: str
    """Unrealized profit/loss in dollars"""

    unrealized_plpc: str
    """Unrealized profit/loss percent (by a factor of 1)"""

    unrealized_intraday_pl: str
    """Unrealized profit/loss in dollars for the day"""

    unrealized_intraday_plpc: str
    """Unrealized profit/loss percent (by a factor of 1)"""

    current_price: str
    """Current asset price per share"""

    lastday_price: str
    """Last day’s asset price per share based on the closing value of the last trading day"""

    change_today: str
    """Percent change from last day price (by a factor of 1)"""

    asset_marginable: bool


class PositionDict(TypedDict):
    asset_id: UUID
    symbol: str
    exchange: ExchangeOrStr
    asset_class: AssetClassOrStr
    avg_entry_price: str
    qty: str
    qty_available: NotRequired[str]
    side: str
    market_value: str
    cost_basis: str
    unrealized_pl: str
    unrealized_plpc: str
    unrealized_intraday_pl: str
    unrealized_intraday_plpc: str
    current_price: str
    lastday_price: str
    change_today: str
    asset_marginable: bool
