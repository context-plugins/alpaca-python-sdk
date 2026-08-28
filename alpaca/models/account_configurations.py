from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dtbp_check import DtbpCheckOrStr


class AccountConfigurations(SdkBaseModel):
    """The account configuration API provides custom configurations about your trading account settings. These
    configurations control various allow you to modify settings to suit your trading needs."""

    dtbp_check: Optional[DtbpCheckOrStr] = UNSET
    """both, entry, or exit. Controls Day Trading Margin Call (DTMC) checks."""

    trade_confirm_email: Optional[str] = UNSET
    """all or none. If none, emails for order fills are not sent."""

    suspend_trade: Optional[bool] = UNSET
    """If true, new orders are blocked."""

    no_shorting: Optional[bool] = UNSET
    """If true, account becomes long-only mode."""

    fractional_trading: Optional[bool] = UNSET
    """If true, account is able to participate in fractional trading"""

    max_margin_multiplier: Optional[str] = UNSET
    """Can be "1" or "2"
    """

    pdt_check: Optional[str] = UNSET


class AccountConfigurationsDict(TypedDict):
    dtbp_check: NotRequired[DtbpCheckOrStr]
    trade_confirm_email: NotRequired[str]
    suspend_trade: NotRequired[bool]
    no_shorting: NotRequired[bool]
    fractional_trading: NotRequired[bool]
    max_margin_multiplier: NotRequired[str]
    pdt_check: NotRequired[str]
