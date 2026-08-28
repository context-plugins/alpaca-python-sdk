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
    json_body,
    json_decoder,
    raw_error_response,
)
from ..models.account_configurations import AccountConfigurations, AccountConfigurationsDict
from ..server.server import Server


class AccountConfigurationsApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountConfigurationsApiWithRawResponse(client, server, auth)

    def get_account_config(self, *, request_options: RequestOptionsOrDict | None = None) -> AccountConfigurations:
        """gets the current account configuration values

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_account_config(request_options=request_options).unwrap()

    def patch_account_config(
        self,
        *,
        body: AccountConfigurations | AccountConfigurationsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountConfigurations:
        """Updates and returns the current account configuration values

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.patch_account_config(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AccountConfigurationsApiWithRawResponse:
        return self._with_raw_response


class AsyncAccountConfigurationsApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountConfigurationsApiWithRawResponse(client, server, auth)

    async def get_account_config(self, *, request_options: RequestOptionsOrDict | None = None) -> AccountConfigurations:
        """gets the current account configuration values

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_account_config(request_options=request_options)).unwrap()

    async def patch_account_config(
        self,
        *,
        body: AccountConfigurations | AccountConfigurationsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountConfigurations:
        """Updates and returns the current account configuration values

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.patch_account_config(body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountConfigurationsApiWithRawResponse:
        return self._with_raw_response


class AccountConfigurationsApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_config(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountConfigurations, RawError]:
        """gets the current account configuration values

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account/configurations"),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[AccountConfigurations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def patch_account_config(
        self,
        *,
        body: AccountConfigurations | AccountConfigurationsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountConfigurations, RawError]:
        """Updates and returns the current account configuration values

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/account/configurations"),
            body=json_body[AccountConfigurations | AccountConfigurationsDict | None](body),
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[AccountConfigurations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAccountConfigurationsApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_account_config(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountConfigurations, RawError]:
        """gets the current account configuration values

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account/configurations"),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[AccountConfigurations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def patch_account_config(
        self,
        *,
        body: AccountConfigurations | AccountConfigurationsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountConfigurations, RawError]:
        """Updates and returns the current account configuration values

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/account/configurations"),
            body=json_body[AccountConfigurations | AccountConfigurationsDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[AccountConfigurations],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
