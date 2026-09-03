from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DtbpCheck(str, Enum):
    """both, entry, or exit. Controls Day Trading Margin Call (DTMC) checks."""

    BOTH = "both"
    ENTRY = "entry"
    EXIT = "exit"

    __str__ = str.__str__


DtbpCheckOrStr: TypeAlias = Annotated[DtbpCheck | str, open_enum_validator(DtbpCheck)]
