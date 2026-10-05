from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.activity_type import ActivityTypeOrStr


class AccountNonTradeActivities(SdkBaseModel):
    activity_type: Optional[ActivityTypeOrStr] = UNSET
    """- FILL
      Order fills (both partial and full fills)

    - TRANS
      Cash transactions (both CSD and CSW)

    - MISC
      Miscellaneous or rarely used activity types (All types except those in TRANS, DIV, or FILL)

    - ACATC
      ACATS IN/OUT (Cash)

    - ACATS
      ACATS IN/OUT (Securities)

    - CFEE
      Crypto fee

    - CSD
      Cash deposit(+)

    - CSW
      Cash withdrawal(-)

    - DIV
      Dividends

    - DIVCGL
      Dividend (capital gain long term)

    - DIVCGS
      Dividend (capital gain short term)

    - DIVFEE
      Dividend fee

    - DIVFT
      Dividend adjusted (Foreign Tax Withheld)

    - DIVNRA
      Dividend adjusted (NRA Withheld)

    - DIVROC
      Dividend return of capital

    - DIVTW
      Dividend adjusted (Tefra Withheld)

    - DIVTXEX
      Dividend (tax exempt)

    - FEE
      Fee denominated in USD

    - INT
      Interest (credit/margin)

    - INTNRA
      Interest adjusted (NRA Withheld)

    - INTTW
      Interest adjusted (Tefra Withheld)

    - JNL
      Journal entry

    - JNLC
      Journal entry (cash)

    - JNLS
      Journal entry (stock)

    - MA
      Merger/Acquisition

    - NC
      Name change

    - OPASN
      Option assignment

    - OPEXP
      Option expiration

    - OPXRC
      Option exercise

    - PTC
      Pass Thru Charge

    - PTR
      Pass Thru Rebate

    - REORG
      Reorg CA

    - SC
      Symbol change

    - SSO
      Stock spinoff

    - SSP
      Stock split"""

    id: Optional[str] = UNSET
    """An ID for the activity, always in “::” format. Can be sent as page_token in requests to facilitate the paging of
    results."""

    date: Optional[RFC3339DateTime] = UNSET
    """The date on which the activity occurred or on which the transaction associated with the activity settled."""

    net_amount: Optional[str] = UNSET
    """The net amount of money (positive or negative) associated with the activity."""

    symbol: Optional[str] = UNSET
    """The symbol of the security involved with the activity. Not present for all activity types."""

    qty: Optional[str] = UNSET
    """For dividend activities, the number of shares that contributed to the payment. Not present for other activity
    types."""

    per_share_amount: Optional[str] = UNSET
    """For dividend activities, the average amount paid per share. Not present for other activity types."""


class AccountNonTradeActivitiesDict(TypedDict):
    activity_type: NotRequired[ActivityTypeOrStr]
    id: NotRequired[str]
    date: NotRequired[RFC3339DateTime]
    net_amount: NotRequired[str]
    symbol: NotRequired[str]
    qty: NotRequired[str]
    per_share_amount: NotRequired[str]
