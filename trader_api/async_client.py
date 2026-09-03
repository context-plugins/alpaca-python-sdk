from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.account_activities import AsyncAccountActivities
from .apis.account_configurations_api import AsyncAccountConfigurationsApi
from .apis.accounts import AsyncAccounts
from .apis.calendar_api import AsyncCalendarApi
from .apis.clock_api import AsyncClockApi
from .apis.orders import AsyncOrders
from .apis.portfolio_history_api import AsyncPortfolioHistoryApi
from .apis.positions import AsyncPositions
from .apis.watchlists import AsyncWatchlists
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseTraderApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncTraderApiClient(BaseTraderApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "paper",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key: str | None = None,
        api_secret: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "TraderApiClient/2.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "2.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            api_key=ApiKeyHeaderScheme("APCA-API-KEY-ID", api_key) if api_key is not None else no_auth,
            api_secret=ApiKeyHeaderScheme("APCA-API-SECRET-KEY", api_secret) if api_secret is not None else no_auth,
        )

    @cached_property
    def account_activities(self) -> AsyncAccountActivities:
        return AsyncAccountActivities(self._raw_client, self._server, self._auth)

    @cached_property
    def account_configurations_api(self) -> AsyncAccountConfigurationsApi:
        return AsyncAccountConfigurationsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def accounts(self) -> AsyncAccounts:
        return AsyncAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def calendar_api(self) -> AsyncCalendarApi:
        return AsyncCalendarApi(self._raw_client, self._server, self._auth)

    @cached_property
    def clock_api(self) -> AsyncClockApi:
        return AsyncClockApi(self._raw_client, self._server, self._auth)

    @cached_property
    def orders(self) -> AsyncOrders:
        return AsyncOrders(self._raw_client, self._server, self._auth)

    @cached_property
    def portfolio_history_api(self) -> AsyncPortfolioHistoryApi:
        return AsyncPortfolioHistoryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def positions(self) -> AsyncPositions:
        return AsyncPositions(self._raw_client, self._server, self._auth)

    @cached_property
    def watchlists(self) -> AsyncWatchlists:
        return AsyncWatchlists(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncTraderApiClient
