from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.account_status import AccountStatusOrStr


class Account(SdkBaseModel):
    """The account API serves important information related to an account, including account status, funds available for
    trade, funds available for withdrawal, and various flags relevant to an account’s ability to trade. An account maybe
    be blocked for just for trades (trades_blocked flag) or for both trades and transfers (account_blocked flag) if
    Alpaca identifies the account to engaging in any suspicious activity. Also, in accordance with FINRA’s pattern day
    trading rule, an account may be flagged for pattern day trading (pattern_day_trader flag), which would inhibit an
    account from placing any further day-trades. Please note that cryptocurrencies are not eligible assets to be used as
    collateral for margin accounts and will require the asset be traded using cash only."""

    id: UUID
    """Account Id."""

    account_number: Optional[str] = UNSET
    """Account number."""

    status: AccountStatusOrStr
    """An enum representing the various possible account status values.

    Most likely, the account status is ACTIVE unless there is any problem. The account status may get in ACCOUNT_UPDATED
    when personal information is being updated from the dashboard, in which case you may not be allowed trading for a
    short period of time until the change is approved.

    - ONBOARDING
      The account is onboarding.
    - SUBMISSION_FAILED
      The account application submission failed for some reason.
    - SUBMITTED
      The account application has been submitted for review.
    - ACCOUNT_UPDATED
      The account information is being updated.
    - APPROVAL_PENDING
      The final account approval is pending.
    - ACTIVE
      The account is active for trading.
    - REJECTED
      The account application has been rejected."""

    currency: Optional[str] = UNSET
    """USD"""

    cash: Optional[str] = UNSET
    """Cash Balance"""

    portfolio_value: Optional[str] = UNSET
    """Total value of cash + holding positions (This field is deprecated. It is equivalent to the equity field.)"""

    pattern_day_trader: Optional[bool] = UNSET
    """Whether or not the account has been flagged as a pattern day trader"""

    trade_suspended_by_user: Optional[bool] = UNSET
    """User setting. If true, the account is not allowed to place orders."""

    trading_blocked: Optional[bool] = UNSET
    """If true, the account is not allowed to place orders."""

    transfers_blocked: Optional[bool] = UNSET
    """If true, the account is not allowed to request money transfers."""

    account_blocked: Optional[bool] = UNSET
    """If true, the account activity by user is prohibited."""

    created_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp this account was created at"""

    shorting_enabled: Optional[bool] = UNSET
    """Flag to denote whether or not the account is permitted to short"""

    long_market_value: Optional[str] = UNSET
    """Real-time MtM value of all long positions held in the account"""

    short_market_value: Optional[str] = UNSET
    """Real-time MtM value of all short positions held in the account"""

    equity: Optional[str] = UNSET
    """Cash + long_market_value + short_market_value"""

    last_equity: Optional[str] = UNSET
    """Equity as of previous trading day at 16:00:00 ET"""

    multiplier: Optional[str] = UNSET
    """Buying power multiplier that represents account margin classification; valid values 1 (standard limited margin
    account with 1x buying power), 2 (reg T margin account with 2x intraday and overnight buying power; this is the
    default for all non-PDT accounts with $2,000 or more equity), 4 (PDT account with 4x intraday buying power and 2x
    reg T overnight buying power)"""

    buying_power: Optional[str] = UNSET
    """Current available $ buying power; If multiplier = 4, this is your daytrade buying power which is calculated as
    (last_equity - (last) maintenance_margin) * 4; If multiplier = 2, buying_power = max(equity – initial_margin,0) * 2;
    If multiplier = 1, buying_power = cash"""

    initial_margin: Optional[str] = UNSET
    """Reg T initial margin requirement (continuously updated value)"""

    maintenance_margin: Optional[str] = UNSET
    """Maintenance margin requirement (continuously updated value)"""

    sma: Optional[str] = UNSET
    """Value of special memorandum account (will be used at a later date to provide additional buying_power)"""

    daytrade_count: Optional[int] = UNSET
    """The current number of daytrades that have been made in the last 5 trading days (inclusive of today)"""

    last_maintenance_margin: Optional[str] = UNSET
    """Your maintenance margin requirement on the previous trading day"""

    daytrading_buying_power: Optional[str] = UNSET
    """Your buying power for day trades (continuously updated value)"""

    regt_buying_power: Optional[str] = UNSET
    """Your buying power under Regulation T (your excess equity - equity minus margin value - times your margin
    multiplier)"""


class AccountDict(TypedDict):
    id: UUID
    account_number: NotRequired[str]
    status: AccountStatusOrStr
    currency: NotRequired[str]
    cash: NotRequired[str]
    portfolio_value: NotRequired[str]
    pattern_day_trader: NotRequired[bool]
    trade_suspended_by_user: NotRequired[bool]
    trading_blocked: NotRequired[bool]
    transfers_blocked: NotRequired[bool]
    account_blocked: NotRequired[bool]
    created_at: NotRequired[RFC3339DateTime]
    shorting_enabled: NotRequired[bool]
    long_market_value: NotRequired[str]
    short_market_value: NotRequired[str]
    equity: NotRequired[str]
    last_equity: NotRequired[str]
    multiplier: NotRequired[str]
    buying_power: NotRequired[str]
    initial_margin: NotRequired[str]
    maintenance_margin: NotRequired[str]
    sma: NotRequired[str]
    daytrade_count: NotRequired[int]
    last_maintenance_margin: NotRequired[str]
    daytrading_buying_power: NotRequired[str]
    regt_buying_power: NotRequired[str]
