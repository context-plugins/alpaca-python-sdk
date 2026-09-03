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
from ..models.enums.direction import DirectionOrStr
from ..models.unions.v2_account_activities_response import V2AccountActivitiesResponse
from ..models.unions.v2_account_activities_response1 import V2AccountActivitiesResponse1
from ..server.server import Server


class AccountActivities:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountActivitiesWithRawResponse(client, server, auth)

    def get_account_activities(
        self,
        *,
        date: RFC3339DateTime | None = None,
        until: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        direction: DirectionOrStr | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        activity_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V2AccountActivitiesResponse]:
        """Returns account activity entries for many types of activities.

        Args:
            date: The date for which you want to see activities.
            until: The response will contain only activities submitted before this date. (Cannot be used with date.)
            after: The response will contain only activities submitted after this date. (Cannot be used with date.)
            direction: asc or desc (default desc if unspecified.)
            page_size: The maximum number of entries to return in the response. (See the section on paging above.)
            page_token: The ID of the end of your current page of results.
            activity_types: A comma-separated list of the activity types to include in the response. If unspecified,
                activities of all types will be returned. See ActivityType model for values
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            returns an array of Account activities

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_account_activities(
            date=date,
            until=until,
            after=after,
            direction=direction,
            page_size=page_size,
            page_token=page_token,
            activity_types=activity_types,
            request_options=request_options,
        ).unwrap()

    def get_account_activities_by_activity_type(
        self,
        activity_type: str,
        *,
        date: RFC3339DateTime | None = None,
        until: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        direction: DirectionOrStr | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V2AccountActivitiesResponse1]:
        """Returns account activity entries for a specific type of activity.

        Args:
            activity_type: The activity type you want to view entries for. A list of valid activity types can be found
                at the bottom of this page.
            date: The date for which you want to see activities.
            until: The response will contain only activities submitted before this date. (Cannot be used with date.)
            after: The response will contain only activities submitted after this date. (Cannot be used with date.)
            direction: asc or desc (default desc if unspecified.)
            page_size: The maximum number of entries to return in the response. (See the section on paging above.)
            page_token: The ID of the end of your current page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            returns an array of Account activities

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_account_activities_by_activity_type(
            activity_type,
            date=date,
            until=until,
            after=after,
            direction=direction,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> AccountActivitiesWithRawResponse:
        return self._with_raw_response


class AsyncAccountActivities:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountActivitiesWithRawResponse(client, server, auth)

    async def get_account_activities(
        self,
        *,
        date: RFC3339DateTime | None = None,
        until: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        direction: DirectionOrStr | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        activity_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V2AccountActivitiesResponse]:
        """Returns account activity entries for many types of activities.

        Args:
            date: The date for which you want to see activities.
            until: The response will contain only activities submitted before this date. (Cannot be used with date.)
            after: The response will contain only activities submitted after this date. (Cannot be used with date.)
            direction: asc or desc (default desc if unspecified.)
            page_size: The maximum number of entries to return in the response. (See the section on paging above.)
            page_token: The ID of the end of your current page of results.
            activity_types: A comma-separated list of the activity types to include in the response. If unspecified,
                activities of all types will be returned. See ActivityType model for values
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            returns an array of Account activities

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_account_activities(
                date=date,
                until=until,
                after=after,
                direction=direction,
                page_size=page_size,
                page_token=page_token,
                activity_types=activity_types,
                request_options=request_options,
            )
        ).unwrap()

    async def get_account_activities_by_activity_type(
        self,
        activity_type: str,
        *,
        date: RFC3339DateTime | None = None,
        until: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        direction: DirectionOrStr | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V2AccountActivitiesResponse1]:
        """Returns account activity entries for a specific type of activity.

        Args:
            activity_type: The activity type you want to view entries for. A list of valid activity types can be found
                at the bottom of this page.
            date: The date for which you want to see activities.
            until: The response will contain only activities submitted before this date. (Cannot be used with date.)
            after: The response will contain only activities submitted after this date. (Cannot be used with date.)
            direction: asc or desc (default desc if unspecified.)
            page_size: The maximum number of entries to return in the response. (See the section on paging above.)
            page_token: The ID of the end of your current page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            returns an array of Account activities

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_account_activities_by_activity_type(
                activity_type,
                date=date,
                until=until,
                after=after,
                direction=direction,
                page_size=page_size,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountActivitiesWithRawResponse:
        return self._with_raw_response


class AccountActivitiesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_activities(
        self,
        *,
        date: RFC3339DateTime | None = None,
        until: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        direction: DirectionOrStr | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        activity_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V2AccountActivitiesResponse], RawError]:
        """Returns account activity entries for many types of activities.

        Args:
            date: The date for which you want to see activities.
            until: The response will contain only activities submitted before this date. (Cannot be used with date.)
            after: The response will contain only activities submitted after this date. (Cannot be used with date.)
            direction: asc or desc (default desc if unspecified.)
            page_size: The maximum number of entries to return in the response. (See the section on paging above.)
            page_token: The ID of the end of your current page of results.
            activity_types: A comma-separated list of the activity types to include in the response. If unspecified,
                activities of all types will be returned. See ActivityType model for values
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account/activities"),
            query_params=[
                param[RFC3339DateTime | None]("date", date),
                param[RFC3339DateTime | None]("until", until),
                param[RFC3339DateTime | None]("after", after),
                param[DirectionOrStr | None]("direction", direction),
                param[int | None]("page_size", page_size),
                param[str | None]("page_token", page_token),
                param[str | None]("activity_types", activity_types),
            ],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[V2AccountActivitiesResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_account_activities_by_activity_type(
        self,
        activity_type: str,
        *,
        date: RFC3339DateTime | None = None,
        until: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        direction: DirectionOrStr | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V2AccountActivitiesResponse1], RawError]:
        """Returns account activity entries for a specific type of activity.

        Args:
            activity_type: The activity type you want to view entries for. A list of valid activity types can be found
                at the bottom of this page.
            date: The date for which you want to see activities.
            until: The response will contain only activities submitted before this date. (Cannot be used with date.)
            after: The response will contain only activities submitted after this date. (Cannot be used with date.)
            direction: asc or desc (default desc if unspecified.)
            page_size: The maximum number of entries to return in the response. (See the section on paging above.)
            page_token: The ID of the end of your current page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account/activities/{activity_type}"),
            path_params=[param[str]("activity_type", activity_type)],
            query_params=[
                param[RFC3339DateTime | None]("date", date),
                param[RFC3339DateTime | None]("until", until),
                param[RFC3339DateTime | None]("after", after),
                param[DirectionOrStr | None]("direction", direction),
                param[int | None]("page_size", page_size),
                param[str | None]("page_token", page_token),
            ],
            auth_scheme=AllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[V2AccountActivitiesResponse1]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAccountActivitiesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_account_activities(
        self,
        *,
        date: RFC3339DateTime | None = None,
        until: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        direction: DirectionOrStr | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        activity_types: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V2AccountActivitiesResponse], RawError]:
        """Returns account activity entries for many types of activities.

        Args:
            date: The date for which you want to see activities.
            until: The response will contain only activities submitted before this date. (Cannot be used with date.)
            after: The response will contain only activities submitted after this date. (Cannot be used with date.)
            direction: asc or desc (default desc if unspecified.)
            page_size: The maximum number of entries to return in the response. (See the section on paging above.)
            page_token: The ID of the end of your current page of results.
            activity_types: A comma-separated list of the activity types to include in the response. If unspecified,
                activities of all types will be returned. See ActivityType model for values
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account/activities"),
            query_params=[
                param[RFC3339DateTime | None]("date", date),
                param[RFC3339DateTime | None]("until", until),
                param[RFC3339DateTime | None]("after", after),
                param[DirectionOrStr | None]("direction", direction),
                param[int | None]("page_size", page_size),
                param[str | None]("page_token", page_token),
                param[str | None]("activity_types", activity_types),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[V2AccountActivitiesResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_account_activities_by_activity_type(
        self,
        activity_type: str,
        *,
        date: RFC3339DateTime | None = None,
        until: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        direction: DirectionOrStr | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V2AccountActivitiesResponse1], RawError]:
        """Returns account activity entries for a specific type of activity.

        Args:
            activity_type: The activity type you want to view entries for. A list of valid activity types can be found
                at the bottom of this page.
            date: The date for which you want to see activities.
            until: The response will contain only activities submitted before this date. (Cannot be used with date.)
            after: The response will contain only activities submitted after this date. (Cannot be used with date.)
            direction: asc or desc (default desc if unspecified.)
            page_size: The maximum number of entries to return in the response. (See the section on paging above.)
            page_token: The ID of the end of your current page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/account/activities/{activity_type}"),
            path_params=[param[str]("activity_type", activity_type)],
            query_params=[
                param[RFC3339DateTime | None]("date", date),
                param[RFC3339DateTime | None]("until", until),
                param[RFC3339DateTime | None]("after", after),
                param[DirectionOrStr | None]("direction", direction),
                param[int | None]("page_size", page_size),
                param[str | None]("page_token", page_token),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.api_key, self._auth.api_secret),
            decoder=json_decoder[list[V2AccountActivitiesResponse1]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
