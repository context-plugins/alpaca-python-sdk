from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.account_activities import AccountActivities
from .apis.account_configurations_api import AccountConfigurationsApi
from .apis.accounts import Accounts
from .apis.calendar_api import CalendarApi
from .apis.clock_api import ClockApi
from .apis.orders import Orders
from .apis.portfolio_history_api import PortfolioHistoryApi
from .apis.positions import Positions
from .apis.watchlists import Watchlists
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseAlpacaClient
from .core import ApiKeyHeaderScheme, HttpClient, HttpxClient, RawClient, no_auth
from .server.environment import Environment


class AlpacaClient(BaseAlpacaClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "paper",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        api_key: str | None = None,
        api_secret: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout)
        )
        self._auth = AuthSchemes(
            api_key=ApiKeyHeaderScheme("APCA-API-KEY-ID", api_key) if api_key is not None else no_auth,
            api_secret=ApiKeyHeaderScheme("APCA-API-SECRET-KEY", api_secret) if api_secret is not None else no_auth,
        )

    @cached_property
    def account_activities(self) -> AccountActivities:
        return AccountActivities(self._raw_client, self._server, self._auth)

    @cached_property
    def account_configurations_api(self) -> AccountConfigurationsApi:
        return AccountConfigurationsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def accounts(self) -> Accounts:
        return Accounts(self._raw_client, self._server, self._auth)

    @cached_property
    def calendar_api(self) -> CalendarApi:
        return CalendarApi(self._raw_client, self._server, self._auth)

    @cached_property
    def clock_api(self) -> ClockApi:
        return ClockApi(self._raw_client, self._server, self._auth)

    @cached_property
    def orders(self) -> Orders:
        return Orders(self._raw_client, self._server, self._auth)

    @cached_property
    def portfolio_history_api(self) -> PortfolioHistoryApi:
        return PortfolioHistoryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def positions(self) -> Positions:
        return Positions(self._raw_client, self._server, self._auth)

    @cached_property
    def watchlists(self) -> Watchlists:
        return Watchlists(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = AlpacaClient
