from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    raw_error_response,
)
from ..models.clock import Clock
from ..server.server import Server


class ClockApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ClockApiWithRawResponse(client, server, auth)

    def get_clock(self, *, request_options: RequestOptionsOrDict | None = None) -> Clock:
        """The clock API serves the current market timestamp, whether or not the market is currently open, as well as
        the times of the next market open and close.

        Returns the market clock.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_clock(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ClockApiWithRawResponse:
        return self._with_raw_response


class AsyncClockApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncClockApiWithRawResponse(client, server, auth)

    async def get_clock(self, *, request_options: RequestOptionsOrDict | None = None) -> Clock:
        """The clock API serves the current market timestamp, whether or not the market is currently open, as well as
        the times of the next market open and close.

        Returns the market clock.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_clock(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncClockApiWithRawResponse:
        return self._with_raw_response


class ClockApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_clock(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Clock, RawError]:
        """The clock API serves the current market timestamp, whether or not the market is currently open, as well as
        the times of the next market open and close.

        Returns the market clock.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/clock"),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Clock],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncClockApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_clock(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Clock, RawError]:
        """The clock API serves the current market timestamp, whether or not the market is currently open, as well as
        the times of the next market open and close.

        Returns the market clock.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/clock"),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Clock],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
