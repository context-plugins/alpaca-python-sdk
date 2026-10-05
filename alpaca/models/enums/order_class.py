from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderClass(str, Enum):
    """This will either be the empty string "", "simple", "bracket", "oco", or "oto"."""

    SIMPLE = "simple"
    BRACKET = "bracket"
    OCO = "oco"
    OTO = "oto"

    __str__ = str.__str__


OrderClassOrStr: TypeAlias = Annotated[OrderClass | str, open_enum_validator(OrderClass)]
