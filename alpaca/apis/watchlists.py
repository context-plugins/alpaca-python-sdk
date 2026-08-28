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
from ..models.add_asset_to_watchlist_request import AddAssetToWatchlistRequest, AddAssetToWatchlistRequestDict
from ..models.post_watchlist_request import PostWatchlistRequest, PostWatchlistRequestDict
from ..models.watchlist import Watchlist
from ..server.server import Server


class Watchlists:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WatchlistsWithRawResponse(client, server, auth)

    def add_asset_to_watchlist(
        self,
        watchlist_id: UUID,
        *,
        body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Append an asset for the symbol to the end of watchlist asset list

        Args:
            watchlist_id: watchlist id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.add_asset_to_watchlist(
            watchlist_id, body=body, request_options=request_options
        ).unwrap()

    def add_asset_to_watchlist_by_name(
        self,
        name: str,
        *,
        body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Append an asset for the symbol to the end of watchlist asset list

        Args:
            name: name of the watchlist
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.add_asset_to_watchlist_by_name(
            name, body=body, request_options=request_options
        ).unwrap()

    def delete_watchlist_by_id(
        self, watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a watchlist. This is a permanent deletion.

        Args:
            watchlist_id: watchlist id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_watchlist_by_id(watchlist_id, request_options=request_options).unwrap()

    def delete_watchlist_by_name(self, name: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a watchlist. This is a permanent deletion.

        Args:
            name: name of the watchlist
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_watchlist_by_name(name, request_options=request_options).unwrap()

    def get_watchlist_by_id(
        self, watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> Watchlist:
        """Returns a watchlist identified by the ID.

        Args:
            watchlist_id: watchlist id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_watchlist_by_id(watchlist_id, request_options=request_options).unwrap()

    def get_watchlist_by_name(self, name: str, *, request_options: RequestOptionsOrDict | None = None) -> Watchlist:
        """Returns a watchlist by name

        Args:
            name: name of the watchlist
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_watchlist_by_name(name, request_options=request_options).unwrap()

    def get_watchlists(self, *, request_options: RequestOptionsOrDict | None = None) -> list[Watchlist]:
        """Returns the list of watchlists registered under the account.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_watchlists(request_options=request_options).unwrap()

    def post_watchlist(
        self,
        body: PostWatchlistRequest | PostWatchlistRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Create a new watchlist with initial set of assets.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.post_watchlist(body, request_options=request_options).unwrap()

    def remove_asset_from_watchlist(
        self, watchlist_id: UUID, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Watchlist:
        """Delete one entry for an asset by symbol name

        Args:
            watchlist_id: Watchlist ID
            symbol: symbol name to remove from the watchlist content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns the updated watchlist

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.remove_asset_from_watchlist(
            watchlist_id, symbol, request_options=request_options
        ).unwrap()

    def update_watchlist_by_id(
        self,
        watchlist_id: UUID,
        *,
        body: PostWatchlistRequest | PostWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Update the name and/or content of watchlist

        Args:
            watchlist_id: watchlist id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_watchlist_by_id(
            watchlist_id, body=body, request_options=request_options
        ).unwrap()

    def update_watchlist_by_name(
        self,
        name: str,
        *,
        body: PostWatchlistRequest | PostWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Update the name and/or content of watchlist

        Args:
            name: name of the watchlist
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_watchlist_by_name(
            name, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> WatchlistsWithRawResponse:
        return self._with_raw_response


class AsyncWatchlists:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWatchlistsWithRawResponse(client, server, auth)

    async def add_asset_to_watchlist(
        self,
        watchlist_id: UUID,
        *,
        body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Append an asset for the symbol to the end of watchlist asset list

        Args:
            watchlist_id: watchlist id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_asset_to_watchlist(
                watchlist_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def add_asset_to_watchlist_by_name(
        self,
        name: str,
        *,
        body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Append an asset for the symbol to the end of watchlist asset list

        Args:
            name: name of the watchlist
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_asset_to_watchlist_by_name(
                name, body=body, request_options=request_options
            )
        ).unwrap()

    async def delete_watchlist_by_id(
        self, watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a watchlist. This is a permanent deletion.

        Args:
            watchlist_id: watchlist id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_watchlist_by_id(watchlist_id, request_options=request_options)
        ).unwrap()

    async def delete_watchlist_by_name(self, name: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a watchlist. This is a permanent deletion.

        Args:
            name: name of the watchlist
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_watchlist_by_name(name, request_options=request_options)).unwrap()

    async def get_watchlist_by_id(
        self, watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> Watchlist:
        """Returns a watchlist identified by the ID.

        Args:
            watchlist_id: watchlist id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_watchlist_by_id(watchlist_id, request_options=request_options)
        ).unwrap()

    async def get_watchlist_by_name(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Watchlist:
        """Returns a watchlist by name

        Args:
            name: name of the watchlist
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_watchlist_by_name(name, request_options=request_options)).unwrap()

    async def get_watchlists(self, *, request_options: RequestOptionsOrDict | None = None) -> list[Watchlist]:
        """Returns the list of watchlists registered under the account.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_watchlists(request_options=request_options)).unwrap()

    async def post_watchlist(
        self,
        body: PostWatchlistRequest | PostWatchlistRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Create a new watchlist with initial set of assets.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.post_watchlist(body, request_options=request_options)).unwrap()

    async def remove_asset_from_watchlist(
        self, watchlist_id: UUID, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Watchlist:
        """Delete one entry for an asset by symbol name

        Args:
            watchlist_id: Watchlist ID
            symbol: symbol name to remove from the watchlist content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns the updated watchlist

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.remove_asset_from_watchlist(
                watchlist_id, symbol, request_options=request_options
            )
        ).unwrap()

    async def update_watchlist_by_id(
        self,
        watchlist_id: UUID,
        *,
        body: PostWatchlistRequest | PostWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Update the name and/or content of watchlist

        Args:
            watchlist_id: watchlist id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_watchlist_by_id(
                watchlist_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def update_watchlist_by_name(
        self,
        name: str,
        *,
        body: PostWatchlistRequest | PostWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Watchlist:
        """Update the name and/or content of watchlist

        Args:
            name: name of the watchlist
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_watchlist_by_name(name, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncWatchlistsWithRawResponse:
        return self._with_raw_response


class WatchlistsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_asset_to_watchlist(
        self,
        watchlist_id: UUID,
        *,
        body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Append an asset for the symbol to the end of watchlist asset list

        Args:
            watchlist_id: watchlist id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id)],
            body=json_body[AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None](body),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def add_asset_to_watchlist_by_name(
        self,
        name: str,
        *,
        body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Append an asset for the symbol to the end of watchlist asset list

        Args:
            name: name of the watchlist
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/watchlists:by_name"),
            query_params=[param[str]("name", name)],
            body=json_body[AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None](body),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_watchlist_by_id(
        self, watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a watchlist. This is a permanent deletion.

        Args:
            watchlist_id: watchlist id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_watchlist_by_name(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a watchlist. This is a permanent deletion.

        Args:
            name: name of the watchlist
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/watchlists:by_name"),
            query_params=[param[str]("name", name)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_watchlist_by_id(
        self, watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Watchlist, RawError]:
        """Returns a watchlist identified by the ID.

        Args:
            watchlist_id: watchlist id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_watchlist_by_name(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Watchlist, RawError]:
        """Returns a watchlist by name

        Args:
            name: name of the watchlist
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/watchlists:by_name"),
            query_params=[param[str]("name", name)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_watchlists(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Watchlist], RawError]:
        """Returns the list of watchlists registered under the account.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/watchlists"),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[Watchlist]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def post_watchlist(
        self,
        body: PostWatchlistRequest | PostWatchlistRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Create a new watchlist with initial set of assets.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/watchlists"),
            body=json_body[PostWatchlistRequest | PostWatchlistRequestDict](body),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_asset_from_watchlist(
        self, watchlist_id: UUID, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Watchlist, RawError]:
        """Delete one entry for an asset by symbol name

        Args:
            watchlist_id: Watchlist ID
            symbol: symbol name to remove from the watchlist content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}/{symbol}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id), param[str]("symbol", symbol)],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_watchlist_by_id(
        self,
        watchlist_id: UUID,
        *,
        body: PostWatchlistRequest | PostWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Update the name and/or content of watchlist

        Args:
            watchlist_id: watchlist id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id)],
            body=json_body[PostWatchlistRequest | PostWatchlistRequestDict | None](body),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_watchlist_by_name(
        self,
        name: str,
        *,
        body: PostWatchlistRequest | PostWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Update the name and/or content of watchlist

        Args:
            name: name of the watchlist
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/watchlists:by_name"),
            query_params=[param[str]("name", name)],
            body=json_body[PostWatchlistRequest | PostWatchlistRequestDict | None](body),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncWatchlistsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_asset_to_watchlist(
        self,
        watchlist_id: UUID,
        *,
        body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Append an asset for the symbol to the end of watchlist asset list

        Args:
            watchlist_id: watchlist id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id)],
            body=json_body[AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def add_asset_to_watchlist_by_name(
        self,
        name: str,
        *,
        body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Append an asset for the symbol to the end of watchlist asset list

        Args:
            name: name of the watchlist
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/watchlists:by_name"),
            query_params=[param[str]("name", name)],
            body=json_body[AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_watchlist_by_id(
        self, watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a watchlist. This is a permanent deletion.

        Args:
            watchlist_id: watchlist id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_watchlist_by_name(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a watchlist. This is a permanent deletion.

        Args:
            name: name of the watchlist
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/watchlists:by_name"),
            query_params=[param[str]("name", name)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_watchlist_by_id(
        self, watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Watchlist, RawError]:
        """Returns a watchlist identified by the ID.

        Args:
            watchlist_id: watchlist id
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_watchlist_by_name(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Watchlist, RawError]:
        """Returns a watchlist by name

        Args:
            name: name of the watchlist
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/watchlists:by_name"),
            query_params=[param[str]("name", name)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_watchlists(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Watchlist], RawError]:
        """Returns the list of watchlists registered under the account.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/watchlists"),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[Watchlist]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_watchlist(
        self,
        body: PostWatchlistRequest | PostWatchlistRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Create a new watchlist with initial set of assets.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/watchlists"),
            body=json_body[PostWatchlistRequest | PostWatchlistRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_asset_from_watchlist(
        self, watchlist_id: UUID, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Watchlist, RawError]:
        """Delete one entry for an asset by symbol name

        Args:
            watchlist_id: Watchlist ID
            symbol: symbol name to remove from the watchlist content
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}/{symbol}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id), param[str]("symbol", symbol)],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_watchlist_by_id(
        self,
        watchlist_id: UUID,
        *,
        body: PostWatchlistRequest | PostWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Update the name and/or content of watchlist

        Args:
            watchlist_id: watchlist id
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/watchlists/{watchlist_id}"),
            path_params=[param[UUID]("watchlist_id", watchlist_id)],
            body=json_body[PostWatchlistRequest | PostWatchlistRequestDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_watchlist_by_name(
        self,
        name: str,
        *,
        body: PostWatchlistRequest | PostWatchlistRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Watchlist, RawError]:
        """Update the name and/or content of watchlist

        Args:
            name: name of the watchlist
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/watchlists:by_name"),
            query_params=[param[str]("name", name)],
            body=json_body[PostWatchlistRequest | PostWatchlistRequestDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Watchlist],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
