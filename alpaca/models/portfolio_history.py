from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PortfolioHistory(SdkBaseModel):
    timestamp: Optional[list[int]] = UNSET
    """time of each data element, left-labeled (the beginning of time window)"""

    equity: Optional[list[float]] = UNSET
    """equity value of the account in dollar amount as of the end of each time window"""

    profit_loss: Optional[list[float]] = UNSET
    """profit/loss in dollar from the base value"""

    profit_loss_pct: Optional[list[float]] = UNSET
    """profit/loss in percentage from the base value"""

    base_value: Optional[float] = UNSET
    """basis in dollar of the profit loss calculation"""

    timeframe: Optional[str] = UNSET
    """time window size of each data element"""


class PortfolioHistoryDict(TypedDict):
    timestamp: NotRequired[list[int]]
    equity: NotRequired[list[float]]
    profit_loss: NotRequired[list[float]]
    profit_loss_pct: NotRequired[list[float]]
    base_value: NotRequired[float]
    timeframe: NotRequired[str]
