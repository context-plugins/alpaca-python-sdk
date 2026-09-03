from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    Date,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.portfolio_history import PortfolioHistory
from ..server.server import Server


class PortfolioHistoryApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PortfolioHistoryApiWithRawResponse(client, server, auth)

    def get_account_portfolio_history(
        self,
        *,
        period: str | None = None,
        timeframe: str | None = None,
        date_end: Date | None = None,
        extended_hours: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PortfolioHistory:
        """Returns timeseries data about equity and profit/loss (P/L) of the account in requested timespan.

        Args:
            period: The duration of the data in <number> + <unit>, such as 1D, where <unit> can be D for day, W for
                week, M for month and A for year. Defaults to 1M.
            timeframe: The resolution of time window. 1Min, 5Min, 15Min, 1H, or 1D. If omitted, 1Min for less than 7
                days period, 15Min for less than 30 days, or otherwise 1D.
            date_end: The date the data is returned up to, in “YYYY-MM-DD” format. Defaults to the current market date
                (rolls over at the market open if extended_hours is false, otherwise at 7am ET)
            extended_hours: If true, include extended hours in the result. This is effective only for timeframe less
                than 1D.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_account_portfolio_history(
            period=period,
            timeframe=timeframe,
            date_end=date_end,
            extended_hours=extended_hours,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> PortfolioHistoryApiWithRawResponse:
        return self._with_raw_response


class AsyncPortfolioHistoryApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPortfolioHistoryApiWithRawResponse(client, server, auth)

    async def get_account_portfolio_history(
        self,
        *,
        period: str | None = None,
        timeframe: str | None = None,
        date_end: Date | None = None,
        extended_hours: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PortfolioHistory:
        """Returns timeseries data about equity and profit/loss (P/L) of the account in requested timespan.

        Args:
            period: The duration of the data in <number> + <unit>, such as 1D, where <unit> can be D for day, W for
                week, M for month and A for year. Defaults to 1M.
            timeframe: The resolution of time window. 1Min, 5Min, 15Min, 1H, or 1D. If omitted, 1Min for less than 7
                days period, 15Min for less than 30 days, or otherwise 1D.
            date_end: The date the data is returned up to, in “YYYY-MM-DD” format. Defaults to the current market date
                (rolls over at the market open if extended_hours is false, otherwise at 7am ET)
            extended_hours: If true, include extended hours in the result. This is effective only for timeframe less
                than 1D.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_account_portfolio_history(
                period=period,
                timeframe=timeframe,
                date_end=date_end,
                extended_hours=extended_hours,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPortfolioHistoryApiWithRawResponse:
        return self._with_raw_response


class PortfolioHistoryApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_portfolio_history(
        self,
        *,
        period: str | None = None,
        timeframe: str | None = None,
        date_end: Date | None = None,
        extended_hours: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PortfolioHistory, RawError]:
        """Returns timeseries data about equity and profit/loss (P/L) of the account in requested timespan.

        Args:
            period: The duration of the data in <number> + <unit>, such as 1D, where <unit> can be D for day, W for
                week, M for month and A for year. Defaults to 1M.
            timeframe: The resolution of time window. 1Min, 5Min, 15Min, 1H, or 1D. If omitted, 1Min for less than 7
                days period, 15Min for less than 30 days, or otherwise 1D.
            date_end: The date the data is returned up to, in “YYYY-MM-DD” format. Defaults to the current market date
                (rolls over at the market open if extended_hours is false, otherwise at 7am ET)
            extended_hours: If true, include extended hours in the result. This is effective only for timeframe less
                than 1D.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account/portfolio/history"),
            query_params=[
                param[str | None]("period", period),
                param[str | None]("timeframe", timeframe),
                param[Date | None]("date_end", date_end),
                param[str | None]("extended_hours", extended_hours),
            ],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[PortfolioHistory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPortfolioHistoryApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_account_portfolio_history(
        self,
        *,
        period: str | None = None,
        timeframe: str | None = None,
        date_end: Date | None = None,
        extended_hours: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PortfolioHistory, RawError]:
        """Returns timeseries data about equity and profit/loss (P/L) of the account in requested timespan.

        Args:
            period: The duration of the data in <number> + <unit>, such as 1D, where <unit> can be D for day, W for
                week, M for month and A for year. Defaults to 1M.
            timeframe: The resolution of time window. 1Min, 5Min, 15Min, 1H, or 1D. If omitted, 1Min for less than 7
                days period, 15Min for less than 30 days, or otherwise 1D.
            date_end: The date the data is returned up to, in “YYYY-MM-DD” format. Defaults to the current market date
                (rolls over at the market open if extended_hours is false, otherwise at 7am ET)
            extended_hours: If true, include extended hours in the result. This is effective only for timeframe less
                than 1D.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account/portfolio/history"),
            query_params=[
                param[str | None]("period", period),
                param[str | None]("timeframe", timeframe),
                param[Date | None]("date_end", date_end),
                param[str | None]("extended_hours", extended_hours),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[PortfolioHistory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
