from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.activity_type import ActivityTypeOrStr
from .enums.order_status import OrderStatusOrStr
from .enums.type import TypeOrStr


class AccountTradingActivities(SdkBaseModel):
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
    """An id for the activity. Always in “::” format. Can be sent as page_token in requests to facilitate the paging of
    results."""

    cum_qty: Optional[str] = UNSET
    """The cumulative quantity of shares involved in the execution."""

    leaves_qty: Optional[str] = UNSET
    """For partially_filled orders, the quantity of shares that are left to be filled."""

    price: Optional[str] = UNSET
    """The per-share price that the trade was executed at."""

    qty: Optional[str] = UNSET
    """The number of shares involved in the trade execution."""

    side: Optional[str] = UNSET
    """buy or sell"""

    symbol: Optional[str] = UNSET
    """The symbol of the security being traded."""

    transaction_time: Optional[RFC3339DateTime] = UNSET
    """The time at which the execution occurred."""

    order_id: Optional[UUID] = UNSET
    """The id for the order that filled."""

    type_: Optional[TypeOrStr] = Field(default=UNSET, alias="type")
    """fill or partial_fill"""

    order_status: Optional[OrderStatusOrStr] = UNSET
    """An order executed through Alpaca can experience several status changes during its lifecycle. The most common
    statuses are described in detail below:

    - new
      The order has been received by Alpaca, and routed to exchanges for execution. This is the usual initial state of
        an order.

    - partially_filled
      The order has been partially filled.

    - filled
      The order has been filled, and no further updates will occur for the order.

    - done_for_day
      The order is done executing for the day, and will not receive further updates until the next trading day.

    - canceled
      The order has been canceled, and no further updates will occur for the order. This can be either due to a cancel
        request by the user, or the order has been canceled by the exchanges due to its time-in-force.

    - expired
      The order has expired, and no further updates will occur for the order.

    - replaced
      The order was replaced by another order, or was updated due to a market event such as corporate action.

    - pending_cancel
      The order is waiting to be canceled.

    - pending_replace
      The order is waiting to be replaced by another order. The order will reject cancel request while in this state.

    Less common states are described below. Note that these states only occur on very rare occasions, and most users
    will likely never see their orders reach these states:

    - accepted
      The order has been received by Alpaca, but hasn’t yet been routed to the execution venue. This could be seen often
        out side of trading session hours.

    - pending_new
      The order has been received by Alpaca, and routed to the exchanges, but has not yet been accepted for execution.
        This state only occurs on rare occasions.

    - accepted_for_bidding
      The order has been received by exchanges, and is evaluated for pricing. This state only occurs on rare occasions.

    - stopped
      The order has been stopped, and a trade is guaranteed for the order, usually at a stated price or better, but has
        not yet occurred. This state only occurs on rare occasions.

    - rejected
      The order has been rejected, and no further updates will occur for the order. This state occurs on rare occasions
        and may occur based on various conditions decided by the exchanges.

    - suspended
      The order has been suspended, and is not eligible for trading. This state only occurs on rare occasions.

    - calculated
      The order has been completed for the day (either filled or done for day), but remaining settlement calculations
        are still pending. This state only occurs on rare occasions.


    An order may be canceled through the API up until the point it reaches a state of either filled, canceled, or
    expired."""


class AccountTradingActivitiesDict(TypedDict):
    activity_type: NotRequired[ActivityTypeOrStr]
    id: NotRequired[str]
    cum_qty: NotRequired[str]
    leaves_qty: NotRequired[str]
    price: NotRequired[str]
    qty: NotRequired[str]
    side: NotRequired[str]
    symbol: NotRequired[str]
    transaction_time: NotRequired[RFC3339DateTime]
    order_id: NotRequired[UUID]
    type_: NotRequired[TypeOrStr]
    order_status: NotRequired[OrderStatusOrStr]
