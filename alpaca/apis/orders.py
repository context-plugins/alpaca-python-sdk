from __future__ import annotations

from uuid import UUID

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
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.delete_all_orders_error import DeleteAllOrdersErrorBody, delete_all_orders_error_mapper
from ..errors.delete_order_by_order_id_error import DeleteOrderByOrderIdErrorBody, delete_order_by_order_id_error_mapper
from ..errors.post_order_error import PostOrderErrorBody, post_order_error_mapper
from ..models.canceled_order_response import CanceledOrderResponse
from ..models.enums.direction import DirectionOrStr
from ..models.enums.status1 import Status1OrStr
from ..models.order import Order, OrderDict
from ..models.patch_order_request import PatchOrderRequest, PatchOrderRequestDict
from ..server.server import Server


class Orders:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OrdersWithRawResponse(client, server, auth)

    def delete_all_orders(self, *, request_options: RequestOptionsOrDict | None = None) -> list[CanceledOrderResponse]:
        """Attempts to cancel all open orders. A response will be provided for each order that is attempted to be
        cancelled. If an order is no longer cancelable, the server will respond with status 500 and reject the request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multi-Status with body. an array of objects that include the order id and http status code for each status
            request.

        Raises:
            ApiError: Failed to cancel order. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_all_orders(request_options=request_options).unwrap()

    def delete_order_by_order_id(self, order_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Attempts to cancel an Open Order. If the order is no longer cancelable, the request will be rejected with
        status 422; otherwise accepted with return status 204.

        Args:
            order_id: order id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: The order status is not cancelable. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_order_by_order_id(order_id, request_options=request_options).unwrap()

    def get_all_orders(
        self,
        *,
        status: Status1OrStr | None = None,
        limit: int | None = None,
        after: str | None = None,
        until: str | None = None,
        direction: DirectionOrStr | None = None,
        nested: bool | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Order]:
        """Retrieves a list of orders for the account, filtered by the supplied query parameters.

        Args:
            status: Order status to be queried. open, closed or all. Defaults to open.
            limit: The maximum number of orders in response. Defaults to 50 and max is 500.
            after: The response will include only ones submitted after this timestamp (exclusive.)
            until: The response will include only ones submitted until this timestamp (exclusive.)
            direction: The chronological order of response based on the submission time. asc or desc. Defaults to desc.
            nested: If true, the result will roll up multi-leg orders under the legs field of primary order.
            symbols: A comma-separated list of symbols to filter by (ex. “AAPL,TSLA,MSFT”). A currency pair is required
                for crypto orders (ex. “BTCUSD,BCHUSD,LTCUSD,ETCUSD”).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response An array of Order objects

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_all_orders(
            status=status,
            limit=limit,
            after=after,
            until=until,
            direction=direction,
            nested=nested,
            symbols=symbols,
            request_options=request_options,
        ).unwrap()

    def get_order_by_order_id(
        self, order_id: UUID, *, nested: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Order:
        """Retrieves a single order for the given order_id.

        Args:
            order_id: order id
            nested: If true, the result will roll up multi-leg orders under the legs field of primary order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_order_by_order_id(
            order_id, nested=nested, request_options=request_options
        ).unwrap()

    def patch_order_by_order_id(
        self,
        order_id: UUID,
        body: PatchOrderRequest | PatchOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Replaces a single order with updated parameters. Each parameter overrides the corresponding attribute of the
        existing order. The other attributes remain the same as the existing order.

        A success return code from a replaced order does NOT guarantee the existing open order has been replaced. If the
        existing open order is filled before the replacing (new) order reaches the execution venue, the replacing (new)
        order is rejected, and these events are sent in the trade_updates stream channel.

        While an order is being replaced, buying power is reduced by the larger of the two orders that have been placed
        (the old order being replaced, and the newly placed order to replace it). If you are replacing a buy entry order
        with a higher limit price than the original order, the buying power is calculated based on the newly placed
        order. If you are replacing it with a lower limit price, the buying power is calculated based on the old order.

        Args:
            order_id: order id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response The new Order object with the new order ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.patch_order_by_order_id(order_id, body, request_options=request_options).unwrap()

    def post_order(self, body: Order | OrderDict, *, request_options: RequestOptionsOrDict | None = None) -> Order:
        """Places a new order for the given account. An order request may be rejected if the account is not authorized
        for trading, or if the tradable balance is insufficient to fill the order..

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Forbidden Buying power or shares is not sufficient. Unprocessable Input parameters are not
                recognized. ``error`` is ``RawError``."""
        return self._with_raw_response.post_order(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> OrdersWithRawResponse:
        return self._with_raw_response


class AsyncOrders:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOrdersWithRawResponse(client, server, auth)

    async def delete_all_orders(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CanceledOrderResponse]:
        """Attempts to cancel all open orders. A response will be provided for each order that is attempted to be
        cancelled. If an order is no longer cancelable, the server will respond with status 500 and reject the request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multi-Status with body. an array of objects that include the order id and http status code for each status
            request.

        Raises:
            ApiError: Failed to cancel order. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_all_orders(request_options=request_options)).unwrap()

    async def delete_order_by_order_id(
        self, order_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Attempts to cancel an Open Order. If the order is no longer cancelable, the request will be rejected with
        status 422; otherwise accepted with return status 204.

        Args:
            order_id: order id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: The order status is not cancelable. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_order_by_order_id(order_id, request_options=request_options)
        ).unwrap()

    async def get_all_orders(
        self,
        *,
        status: Status1OrStr | None = None,
        limit: int | None = None,
        after: str | None = None,
        until: str | None = None,
        direction: DirectionOrStr | None = None,
        nested: bool | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Order]:
        """Retrieves a list of orders for the account, filtered by the supplied query parameters.

        Args:
            status: Order status to be queried. open, closed or all. Defaults to open.
            limit: The maximum number of orders in response. Defaults to 50 and max is 500.
            after: The response will include only ones submitted after this timestamp (exclusive.)
            until: The response will include only ones submitted until this timestamp (exclusive.)
            direction: The chronological order of response based on the submission time. asc or desc. Defaults to desc.
            nested: If true, the result will roll up multi-leg orders under the legs field of primary order.
            symbols: A comma-separated list of symbols to filter by (ex. “AAPL,TSLA,MSFT”). A currency pair is required
                for crypto orders (ex. “BTCUSD,BCHUSD,LTCUSD,ETCUSD”).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response An array of Order objects

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_all_orders(
                status=status,
                limit=limit,
                after=after,
                until=until,
                direction=direction,
                nested=nested,
                symbols=symbols,
                request_options=request_options,
            )
        ).unwrap()

    async def get_order_by_order_id(
        self, order_id: UUID, *, nested: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Order:
        """Retrieves a single order for the given order_id.

        Args:
            order_id: order id
            nested: If true, the result will roll up multi-leg orders under the legs field of primary order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_order_by_order_id(
                order_id, nested=nested, request_options=request_options
            )
        ).unwrap()

    async def patch_order_by_order_id(
        self,
        order_id: UUID,
        body: PatchOrderRequest | PatchOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Replaces a single order with updated parameters. Each parameter overrides the corresponding attribute of the
        existing order. The other attributes remain the same as the existing order.

        A success return code from a replaced order does NOT guarantee the existing open order has been replaced. If the
        existing open order is filled before the replacing (new) order reaches the execution venue, the replacing (new)
        order is rejected, and these events are sent in the trade_updates stream channel.

        While an order is being replaced, buying power is reduced by the larger of the two orders that have been placed
        (the old order being replaced, and the newly placed order to replace it). If you are replacing a buy entry order
        with a higher limit price than the original order, the buying power is calculated based on the newly placed
        order. If you are replacing it with a lower limit price, the buying power is calculated based on the old order.

        Args:
            order_id: order id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response The new Order object with the new order ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.patch_order_by_order_id(order_id, body, request_options=request_options)
        ).unwrap()

    async def post_order(
        self, body: Order | OrderDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Order:
        """Places a new order for the given account. An order request may be rejected if the account is not authorized
        for trading, or if the tradable balance is insufficient to fill the order..

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Forbidden Buying power or shares is not sufficient. Unprocessable Input parameters are not
                recognized. ``error`` is ``RawError``."""
        return (await self._with_raw_response.post_order(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncOrdersWithRawResponse:
        return self._with_raw_response


class OrdersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_all_orders(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CanceledOrderResponse], DeleteAllOrdersErrorBody]:
        """Attempts to cancel all open orders. A response will be provided for each order that is attempted to be
        cancelled. If an order is no longer cancelable, the server will respond with status 500 and reject the request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/orders"),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[CanceledOrderResponse]],
            error_mapper=delete_all_orders_error_mapper,
            request_options=request_options,
        )

    def delete_order_by_order_id(
        self, order_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteOrderByOrderIdErrorBody]:
        """Attempts to cancel an Open Order. If the order is no longer cancelable, the request will be rejected with
        status 422; otherwise accepted with return status 204.

        Args:
            order_id: order id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[UUID]("order_id", order_id)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=empty_response,
            error_mapper=delete_order_by_order_id_error_mapper,
            request_options=request_options,
        )

    def get_all_orders(
        self,
        *,
        status: Status1OrStr | None = None,
        limit: int | None = None,
        after: str | None = None,
        until: str | None = None,
        direction: DirectionOrStr | None = None,
        nested: bool | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Order], RawError]:
        """Retrieves a list of orders for the account, filtered by the supplied query parameters.

        Args:
            status: Order status to be queried. open, closed or all. Defaults to open.
            limit: The maximum number of orders in response. Defaults to 50 and max is 500.
            after: The response will include only ones submitted after this timestamp (exclusive.)
            until: The response will include only ones submitted until this timestamp (exclusive.)
            direction: The chronological order of response based on the submission time. asc or desc. Defaults to desc.
            nested: If true, the result will roll up multi-leg orders under the legs field of primary order.
            symbols: A comma-separated list of symbols to filter by (ex. “AAPL,TSLA,MSFT”). A currency pair is required
                for crypto orders (ex. “BTCUSD,BCHUSD,LTCUSD,ETCUSD”).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders"),
            query_params=[
                param[Status1OrStr | None]("status", status),
                param[int | None]("limit", limit),
                param[str | None]("after", after),
                param[str | None]("until", until),
                param[DirectionOrStr | None]("direction", direction),
                param[bool | None]("nested", nested),
                param[str | None]("symbols", symbols),
            ],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[Order]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_order_by_order_id(
        self, order_id: UUID, *, nested: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Order, RawError]:
        """Retrieves a single order for the given order_id.

        Args:
            order_id: order id
            nested: If true, the result will roll up multi-leg orders under the legs field of primary order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[UUID]("order_id", order_id)],
            query_params=[param[bool | None]("nested", nested)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def patch_order_by_order_id(
        self,
        order_id: UUID,
        body: PatchOrderRequest | PatchOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, RawError]:
        """Replaces a single order with updated parameters. Each parameter overrides the corresponding attribute of the
        existing order. The other attributes remain the same as the existing order.

        A success return code from a replaced order does NOT guarantee the existing open order has been replaced. If the
        existing open order is filled before the replacing (new) order reaches the execution venue, the replacing (new)
        order is rejected, and these events are sent in the trade_updates stream channel.

        While an order is being replaced, buying power is reduced by the larger of the two orders that have been placed
        (the old order being replaced, and the newly placed order to replace it). If you are replacing a buy entry order
        with a higher limit price than the original order, the buying power is calculated based on the newly placed
        order. If you are replacing it with a lower limit price, the buying power is calculated based on the old order.

        Args:
            order_id: order id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[UUID]("order_id", order_id)],
            body=json_body[PatchOrderRequest | PatchOrderRequestDict](body),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def post_order(
        self, body: Order | OrderDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Order, PostOrderErrorBody]:
        """Places a new order for the given account. An order request may be rejected if the account is not authorized
        for trading, or if the tradable balance is insufficient to fill the order..

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders"),
            body=json_body[Order | OrderDict](body),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Order],
            error_mapper=post_order_error_mapper,
            request_options=request_options,
        )


class AsyncOrdersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_all_orders(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CanceledOrderResponse], DeleteAllOrdersErrorBody]:
        """Attempts to cancel all open orders. A response will be provided for each order that is attempted to be
        cancelled. If an order is no longer cancelable, the server will respond with status 500 and reject the request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/orders"),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[CanceledOrderResponse]],
            error_mapper=delete_all_orders_error_mapper,
            request_options=request_options,
        )

    async def delete_order_by_order_id(
        self, order_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteOrderByOrderIdErrorBody]:
        """Attempts to cancel an Open Order. If the order is no longer cancelable, the request will be rejected with
        status 422; otherwise accepted with return status 204.

        Args:
            order_id: order id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[UUID]("order_id", order_id)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=empty_response,
            error_mapper=delete_order_by_order_id_error_mapper,
            request_options=request_options,
        )

    async def get_all_orders(
        self,
        *,
        status: Status1OrStr | None = None,
        limit: int | None = None,
        after: str | None = None,
        until: str | None = None,
        direction: DirectionOrStr | None = None,
        nested: bool | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Order], RawError]:
        """Retrieves a list of orders for the account, filtered by the supplied query parameters.

        Args:
            status: Order status to be queried. open, closed or all. Defaults to open.
            limit: The maximum number of orders in response. Defaults to 50 and max is 500.
            after: The response will include only ones submitted after this timestamp (exclusive.)
            until: The response will include only ones submitted until this timestamp (exclusive.)
            direction: The chronological order of response based on the submission time. asc or desc. Defaults to desc.
            nested: If true, the result will roll up multi-leg orders under the legs field of primary order.
            symbols: A comma-separated list of symbols to filter by (ex. “AAPL,TSLA,MSFT”). A currency pair is required
                for crypto orders (ex. “BTCUSD,BCHUSD,LTCUSD,ETCUSD”).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders"),
            query_params=[
                param[Status1OrStr | None]("status", status),
                param[int | None]("limit", limit),
                param[str | None]("after", after),
                param[str | None]("until", until),
                param[DirectionOrStr | None]("direction", direction),
                param[bool | None]("nested", nested),
                param[str | None]("symbols", symbols),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[Order]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_order_by_order_id(
        self, order_id: UUID, *, nested: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Order, RawError]:
        """Retrieves a single order for the given order_id.

        Args:
            order_id: order id
            nested: If true, the result will roll up multi-leg orders under the legs field of primary order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[UUID]("order_id", order_id)],
            query_params=[param[bool | None]("nested", nested)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def patch_order_by_order_id(
        self,
        order_id: UUID,
        body: PatchOrderRequest | PatchOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, RawError]:
        """Replaces a single order with updated parameters. Each parameter overrides the corresponding attribute of the
        existing order. The other attributes remain the same as the existing order.

        A success return code from a replaced order does NOT guarantee the existing open order has been replaced. If the
        existing open order is filled before the replacing (new) order reaches the execution venue, the replacing (new)
        order is rejected, and these events are sent in the trade_updates stream channel.

        While an order is being replaced, buying power is reduced by the larger of the two orders that have been placed
        (the old order being replaced, and the newly placed order to replace it). If you are replacing a buy entry order
        with a higher limit price than the original order, the buying power is calculated based on the newly placed
        order. If you are replacing it with a lower limit price, the buying power is calculated based on the old order.

        Args:
            order_id: order id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[UUID]("order_id", order_id)],
            body=json_body[PatchOrderRequest | PatchOrderRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_order(
        self, body: Order | OrderDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Order, PostOrderErrorBody]:
        """Places a new order for the given account. An order request may be rejected if the account is not authorized
        for trading, or if the tradable balance is insufficient to fill the order..

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders"),
            body=json_body[Order | OrderDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Order],
            error_mapper=post_order_error_mapper,
            request_options=request_options,
        )
