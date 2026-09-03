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
    RFC3339DateTime,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.calendar import Calendar
from ..server.server import Server


class CalendarApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CalendarApiWithRawResponse(client, server, auth)

    def get_calendar(
        self,
        *,
        start: RFC3339DateTime | None = None,
        end: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Calendar]:
        """Returns the market calendar.

        Args:
            start: The first date to retrieve data for (inclusive)
            end: The last date to retrieve data for (inclusive)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_calendar(start=start, end=end, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CalendarApiWithRawResponse:
        return self._with_raw_response


class AsyncCalendarApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCalendarApiWithRawResponse(client, server, auth)

    async def get_calendar(
        self,
        *,
        start: RFC3339DateTime | None = None,
        end: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Calendar]:
        """Returns the market calendar.

        Args:
            start: The first date to retrieve data for (inclusive)
            end: The last date to retrieve data for (inclusive)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_calendar(start=start, end=end, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCalendarApiWithRawResponse:
        return self._with_raw_response


class CalendarApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_calendar(
        self,
        *,
        start: RFC3339DateTime | None = None,
        end: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Calendar], RawError]:
        """Returns the market calendar.

        Args:
            start: The first date to retrieve data for (inclusive)
            end: The last date to retrieve data for (inclusive)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/calendar"),
            query_params=[param[RFC3339DateTime | None]("start", start), param[RFC3339DateTime | None]("end", end)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[Calendar]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCalendarApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_calendar(
        self,
        *,
        start: RFC3339DateTime | None = None,
        end: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Calendar], RawError]:
        """Returns the market calendar.

        Args:
            start: The first date to retrieve data for (inclusive)
            end: The last date to retrieve data for (inclusive)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/calendar"),
            query_params=[param[RFC3339DateTime | None]("start", start), param[RFC3339DateTime | None]("end", end)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[Calendar]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
