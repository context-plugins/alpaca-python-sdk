from __future__ import annotations

from typing import TypeAlias

from ..account_non_trade_activities import AccountNonTradeActivities, AccountNonTradeActivitiesDict
from ..account_trading_activities import AccountTradingActivities, AccountTradingActivitiesDict

V2AccountActivitiesResponse: TypeAlias = AccountTradingActivities | AccountNonTradeActivities
"""Will be a mix of TradingActivity or NonTradeActivity objects based on what is passed in the activity_types
parameter"""

V2AccountActivitiesResponseDict: TypeAlias = AccountTradingActivitiesDict | AccountNonTradeActivitiesDict
