from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Exchange(str, Enum):
    """Represents the current exchanges Alpaca supports. List is currently:

    - AMEX
    - ARCA
    - BATS
    - NYSE
    - NASDAQ
    - NYSEARCA
    - OTC"""

    AMEX = "AMEX"
    ARCA = "ARCA"
    BATS = "BATS"
    NYSE = "NYSE"
    NASDAQ = "NASDAQ"
    NYSEARCA = "NYSEARCA"
    OTC = "OTC"

    __str__ = str.__str__


ExchangeOrStr: TypeAlias = Annotated[Exchange | str, open_enum_validator(Exchange)]
