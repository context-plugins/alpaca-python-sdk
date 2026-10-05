from __future__ import annotations

from typing import TypeAlias

from ..account_non_trade_activities import AccountNonTradeActivities, AccountNonTradeActivitiesDict
from ..account_trading_activities import AccountTradingActivities, AccountTradingActivitiesDict

V2AccountActivitiesResponse1: TypeAlias = AccountTradingActivities | AccountNonTradeActivities
"""Will be one of a TradingActivity or NonTradeActivity based on activity_type used in path"""

V2AccountActivitiesResponse1Dict: TypeAlias = AccountTradingActivitiesDict | AccountNonTradeActivitiesDict
