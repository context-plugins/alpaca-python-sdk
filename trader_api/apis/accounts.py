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
from ..models.account import Account
from ..server.server import Server


class Accounts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountsWithRawResponse(client, server, auth)

    def get_account(self, *, request_options: RequestOptionsOrDict | None = None) -> Account:
        """Returns the account associated with the API key.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_account(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AccountsWithRawResponse:
        return self._with_raw_response


class AsyncAccounts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountsWithRawResponse(client, server, auth)

    async def get_account(self, *, request_options: RequestOptionsOrDict | None = None) -> Account:
        """Returns the account associated with the API key.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_account(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountsWithRawResponse:
        return self._with_raw_response


class AccountsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Account, RawError]:
        """Returns the account associated with the API key.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account"),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Account],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAccountsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_account(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Account, RawError]:
        """Returns the account associated with the API key.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account"),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[Account],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
