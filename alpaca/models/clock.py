from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class Clock(SdkBaseModel):
    timestamp: Optional[RFC3339DateTime] = UNSET
    """Current timestamp"""

    is_open: Optional[bool] = UNSET
    """Whether or not the market is open"""

    next_open: Optional[RFC3339DateTime] = UNSET
    """Next Market open timestamp"""

    next_close: Optional[RFC3339DateTime] = UNSET
    """Next market close timestamp"""


class ClockDict(TypedDict):
    timestamp: NotRequired[RFC3339DateTime]
    is_open: NotRequired[bool]
    next_open: NotRequired[RFC3339DateTime]
    next_close: NotRequired[RFC3339DateTime]
