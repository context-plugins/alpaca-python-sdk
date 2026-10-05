from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Calendar(SdkBaseModel):
    date: str
    """Date string in “%Y-%m-%d” format"""

    open: str
    """The time the market opens at on this date in “%H:%M” format"""

    close: str
    """The time the market closes at on this date in “%H:%M” format"""

    session_open: str
    session_close: str


class CalendarDict(TypedDict):
    date: str
    open: str
    close: str
    session_open: str
    session_close: str
