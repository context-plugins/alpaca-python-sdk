from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderType(str, Enum):
    """Represents the types of orders Alpaca currently supports

    - market
    - limit
    - stop
    - stop_limit
    - trailing_stop"""

    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"
    STOP_LIMIT = "stop_limit"
    TRAILING_STOP = "trailing_stop"

    __str__ = str.__str__


OrderTypeOrStr: TypeAlias = Annotated[OrderType | str, open_enum_validator(OrderType)]
