from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.asset_class import AssetClassOrStr
from .enums.exchange import ExchangeOrStr
from .enums.status import StatusOrStr


class Assets(SdkBaseModel):
    """The assets API serves as the master list of assets available for trade and data consumption from Alpaca. Assets
    are sorted by asset class, exchange and symbol. Some assets are only available for data consumption via Polygon, and
    are not tradable with Alpaca. These assets will be marked with the flag tradable=false."""

    id: UUID
    """Asset ID"""

    class_: AssetClassOrStr = Field(alias="class")
    """Represents what class of asset this is. Currently only supports ``us_equity`` or ``crypto``"""

    exchange: ExchangeOrStr
    """Represents the current exchanges Alpaca supports. List is currently:

    - AMEX
    - ARCA
    - BATS
    - NYSE
    - NASDAQ
    - NYSEARCA
    - OTC"""

    symbol: str
    """The symbol of the asset"""

    name: str
    """The official name of the asset"""

    status: StatusOrStr
    """active or inactive"""

    tradable: bool
    """Asset is tradable on Alpaca or not"""

    marginable: bool
    """Asset is marginable or not"""

    shortable: bool
    """Asset is shortable or not"""

    easy_to_borrow: bool
    """Asset is easy-to-borrow or not (filtering for easy_to_borrow = True is the best way to check whether the name is
    currently available to short at Alpaca)."""

    fractionable: bool
    """Asset is fractionable or not"""


class AssetsDict(TypedDict):
    id: UUID
    class_: AssetClassOrStr
    exchange: ExchangeOrStr
    symbol: str
    name: str
    status: StatusOrStr
    tradable: bool
    marginable: bool
    shortable: bool
    easy_to_borrow: bool
    fractionable: bool
