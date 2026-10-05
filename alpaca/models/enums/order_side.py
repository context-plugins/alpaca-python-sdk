from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderSide(str, Enum):
    """Represents which side this order was on:

    - buy
    - sell"""

    BUY = "buy"
    SELL = "sell"

    __str__ = str.__str__


OrderSideOrStr: TypeAlias = Annotated[OrderSide | str, open_enum_validator(OrderSide)]
