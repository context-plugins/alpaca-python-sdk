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
    param,
    raw_error_response,
)
from ..errors.delete_all_open_positions_error import (
    DeleteAllOpenPositionsErrorBody,
    delete_all_open_positions_error_mapper,
)
from ..models.order import Order
from ..models.position import Position
from ..models.position_closed_reponse import PositionClosedReponse
from ..server.server import Server


class Positions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PositionsWithRawResponse(client, server, auth)

    def delete_all_open_positions(
        self, *, cancel_orders: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[PositionClosedReponse]:
        """Closes (liquidates) all of the account’s open long and short positions. A response will be provided for each
        order that is attempted to be cancelled. If an order is no longer cancelable, the server will respond with
        status 500 and reject the request.

        Args:
            cancel_orders: If true is specified, cancel all open orders before liquidating all positions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multi-Status with body. an array of PositionClosed responses

        Raises:
            ApiError: Failed to liquidate ``error`` is ``RawError``."""
        return self._with_raw_response.delete_all_open_positions(
            cancel_orders=cancel_orders, request_options=request_options
        ).unwrap()

    def delete_open_position(
        self,
        symbol_or_asset_id: str,
        *,
        qty: float | None = None,
        percentage: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Closes (liquidates) the account’s open position for the given symbol. Works for both long and short
        positions.

        Args:
            symbol_or_asset_id: symbol or assetId
            qty: the number of shares to liquidate. Can accept up to 9 decimal points. Cannot work with percentage
            percentage: percentage of position to liquidate. Must be between 0 and 100. Would only sell fractional if
                position is originally fractional. Can accept up to 9 decimal points. Cannot work with qty
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response Returns the order created to close out this position

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_open_position(
            symbol_or_asset_id, qty=qty, percentage=percentage, request_options=request_options
        ).unwrap()

    def get_all_open_positions(self, *, request_options: RequestOptionsOrDict | None = None) -> list[Position]:
        """The positions API provides information about an account’s current open positions. The response will include
        information such as cost basis, shares traded, and market value, which will be updated live as price information
        is updated. Once a position is closed, it will no longer be queryable through this API

        Retrieves a list of the account’s open positions

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_all_open_positions(request_options=request_options).unwrap()

    def get_open_position(
        self, symbol_or_asset_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Position:
        """Retrieves the account’s open position for the given symbol or assetId.

        Args:
            symbol_or_asset_id: symbol or assetId
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_open_position(symbol_or_asset_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> PositionsWithRawResponse:
        return self._with_raw_response


class AsyncPositions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPositionsWithRawResponse(client, server, auth)

    async def delete_all_open_positions(
        self, *, cancel_orders: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[PositionClosedReponse]:
        """Closes (liquidates) all of the account’s open long and short positions. A response will be provided for each
        order that is attempted to be cancelled. If an order is no longer cancelable, the server will respond with
        status 500 and reject the request.

        Args:
            cancel_orders: If true is specified, cancel all open orders before liquidating all positions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multi-Status with body. an array of PositionClosed responses

        Raises:
            ApiError: Failed to liquidate ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_all_open_positions(
                cancel_orders=cancel_orders, request_options=request_options
            )
        ).unwrap()

    async def delete_open_position(
        self,
        symbol_or_asset_id: str,
        *,
        qty: float | None = None,
        percentage: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Closes (liquidates) the account’s open position for the given symbol. Works for both long and short
        positions.

        Args:
            symbol_or_asset_id: symbol or assetId
            qty: the number of shares to liquidate. Can accept up to 9 decimal points. Cannot work with percentage
            percentage: percentage of position to liquidate. Must be between 0 and 100. Would only sell fractional if
                position is originally fractional. Can accept up to 9 decimal points. Cannot work with qty
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response Returns the order created to close out this position

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_open_position(
                symbol_or_asset_id, qty=qty, percentage=percentage, request_options=request_options
            )
        ).unwrap()

    async def get_all_open_positions(self, *, request_options: RequestOptionsOrDict | None = None) -> list[Position]:
        """The positions API provides information about an account’s current open positions. The response will include
        information such as cost basis, shares traded, and market value, which will be updated live as price information
        is updated. Once a position is closed, it will no longer be queryable through this API

        Retrieves a list of the account’s open positions

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_all_open_positions(request_options=request_options)).unwrap()

    async def get_open_position(
        self, symbol_or_asset_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Position:
        """Retrieves the account’s open position for the given symbol or assetId.

        Args:
            symbol_or_asset_id: symbol or assetId
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_open_position(symbol_or_asset_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPositionsWithRawResponse:
        return self._with_raw_response


class PositionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_all_open_positions(
        self, *, cancel_orders: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PositionClosedReponse], DeleteAllOpenPositionsErrorBody]:
        """Closes (liquidates) all of the account’s open long and short positions. A response will be provided for each
        order that is attempted to be cancelled. If an order is no longer cancelable, the server will respond with
        status 500 and reject the request.

        Args:
            cancel_orders: If true is specified, cancel all open orders before liquidating all positions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/positions"),
            query_params=[param[bool | None]("cancel_orders", cancel_orders)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[PositionClosedReponse]],
            error_mapper=delete_all_open_positions_error_mapper,
            request_options=request_options,
        )

    def delete_open_position(
        self,
        symbol_or_asset_id: str,
        *,
        qty: float | None = None,
        percentage: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, RawError]:
        """Closes (liquidates) the account’s open position for the given symbol. Works for both long and short
        positions.

        Args:
            symbol_or_asset_id: symbol or assetId
            qty: the number of shares to liquidate. Can accept up to 9 decimal points. Cannot work with percentage
            percentage: percentage of position to liquidate. Must be between 0 and 100. Would only sell fractional if
                position is originally fractional. Can accept up to 9 decimal points. Cannot work with qty
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/positions/{symbol_or_asset_id}"),
            path_params=[param[str]("symbol_or_asset_id", symbol_or_asset_id)],
            query_params=[param[float | None]("qty", qty), param[float | None]("percentage", percentage)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_all_open_positions(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Position], RawError]:
        """The positions API provides information about an account’s current open positions. The response will include
        information such as cost basis, shares traded, and market value, which will be updated live as price information
        is updated. Once a position is closed, it will no longer be queryable through this API

        Retrieves a list of the account’s open positions

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/positions"),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[Position]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_open_position(
        self, symbol_or_asset_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Position, RawError]:
        """Retrieves the account’s open position for the given symbol or assetId.

        Args:
            symbol_or_asset_id: symbol or assetId
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/positions/{symbol_or_asset_id}"),
            path_params=[param[str]("symbol_or_asset_id", symbol_or_asset_id)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Position],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPositionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_all_open_positions(
        self, *, cancel_orders: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PositionClosedReponse], DeleteAllOpenPositionsErrorBody]:
        """Closes (liquidates) all of the account’s open long and short positions. A response will be provided for each
        order that is attempted to be cancelled. If an order is no longer cancelable, the server will respond with
        status 500 and reject the request.

        Args:
            cancel_orders: If true is specified, cancel all open orders before liquidating all positions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/positions"),
            query_params=[param[bool | None]("cancel_orders", cancel_orders)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[PositionClosedReponse]],
            error_mapper=delete_all_open_positions_error_mapper,
            request_options=request_options,
        )

    async def delete_open_position(
        self,
        symbol_or_asset_id: str,
        *,
        qty: float | None = None,
        percentage: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, RawError]:
        """Closes (liquidates) the account’s open position for the given symbol. Works for both long and short
        positions.

        Args:
            symbol_or_asset_id: symbol or assetId
            qty: the number of shares to liquidate. Can accept up to 9 decimal points. Cannot work with percentage
            percentage: percentage of position to liquidate. Must be between 0 and 100. Would only sell fractional if
                position is originally fractional. Can accept up to 9 decimal points. Cannot work with qty
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/positions/{symbol_or_asset_id}"),
            path_params=[param[str]("symbol_or_asset_id", symbol_or_asset_id)],
            query_params=[param[float | None]("qty", qty), param[float | None]("percentage", percentage)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_all_open_positions(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Position], RawError]:
        """The positions API provides information about an account’s current open positions. The response will include
        information such as cost basis, shares traded, and market value, which will be updated live as price information
        is updated. Once a position is closed, it will no longer be queryable through this API

        Retrieves a list of the account’s open positions

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/positions"),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[Position]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_open_position(
        self, symbol_or_asset_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Position, RawError]:
        """Retrieves the account’s open position for the given symbol or assetId.

        Args:
            symbol_or_asset_id: symbol or assetId
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/positions/{symbol_or_asset_id}"),
            path_params=[param[str]("symbol_or_asset_id", symbol_or_asset_id)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Position],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
