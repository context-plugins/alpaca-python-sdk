from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetClass(str, Enum):
    """Represents what class of asset this is. Currently only supports ``us_equity`` or ``crypto``"""

    US_EQUITY = "us_equity"
    CRYPTO = "crypto"

    __str__ = str.__str__


AssetClassOrStr: TypeAlias = Annotated[AssetClass | str, open_enum_validator(AssetClass)]
