# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [TraderApiClient](trader_api/client.py)

## AccountActivities

> Source: [AccountActivities](trader_api/apis/account_activities.py)

<details>
<summary><code>def get_account_activities(*, date: RFC3339DateTime | None = None, until: RFC3339DateTime | None = None, after: RFC3339DateTime | None = None, direction: DirectionOrStr | None = None, page_size: int | None = None, page_token: str | None = None, activity_types: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[V2AccountActivitiesResponse], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns account activity entries for many types of activities.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account_activities.with_raw_response.get_account_activities()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V2AccountActivitiesResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.account_activities.with_raw_response.get_account_activities()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V2AccountActivitiesResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>date</code> | <code>RFC3339DateTime \| None</code> | The date for which you want to see activities.<br>**Default**: <code>None</code> |
| <code>until</code> | <code>RFC3339DateTime \| None</code> | The response will contain only activities submitted before this date. (Cannot be used with date.)<br>**Default**: <code>None</code> |
| <code>after</code> | <code>RFC3339DateTime \| None</code> | The response will contain only activities submitted after this date. (Cannot be used with date.)<br>**Default**: <code>None</code> |
| <code>direction</code> | <code>[DirectionOrStr](trader_api/models/enums/direction.py) \| None</code> | asc or desc (default desc if unspecified.)<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | The maximum number of entries to return in the response. (See the section on paging above.)<br>**Default**: <code>None</code> |
| <code>page_token</code> | <code>str \| None</code> | The ID of the end of your current page of results.<br>**Default**: <code>None</code> |
| <code>activity_types</code> | <code>str \| None</code> | A comma-separated list of the activity types to include in the response. If unspecified, activities of all types will be returned. See ActivityType model for values<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;list&#91;[V2AccountActivitiesResponse](trader_api/models/unions/v2_account_activities_response.py)&#93;, [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[V2AccountActivitiesResponse](trader_api/models/unions/v2_account_activities_response.py)&#93;</code> -- returns an array of Account activities

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_account_activities_by_activity_type(activity_type: str, *, date: RFC3339DateTime | None = None, until: RFC3339DateTime | None = None, after: RFC3339DateTime | None = None, direction: DirectionOrStr | None = None, page_size: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[V2AccountActivitiesResponse1], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns account activity entries for a specific type of activity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account_activities.with_raw_response.get_account_activities_by_activity_type(activity_type)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V2AccountActivitiesResponse1]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.account_activities.with_raw_response.get_account_activities_by_activity_type(activity_type)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V2AccountActivitiesResponse1]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>activity_type</code> | <code>str</code> | The activity type you want to view entries for. A list of valid activity types can be found at the bottom of this page. |
| <code>date</code> | <code>RFC3339DateTime \| None</code> | The date for which you want to see activities.<br>**Default**: <code>None</code> |
| <code>until</code> | <code>RFC3339DateTime \| None</code> | The response will contain only activities submitted before this date. (Cannot be used with date.)<br>**Default**: <code>None</code> |
| <code>after</code> | <code>RFC3339DateTime \| None</code> | The response will contain only activities submitted after this date. (Cannot be used with date.)<br>**Default**: <code>None</code> |
| <code>direction</code> | <code>[DirectionOrStr](trader_api/models/enums/direction.py) \| None</code> | asc or desc (default desc if unspecified.)<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | The maximum number of entries to return in the response. (See the section on paging above.)<br>**Default**: <code>None</code> |
| <code>page_token</code> | <code>str \| None</code> | The ID of the end of your current page of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;list&#91;[V2AccountActivitiesResponse1](trader_api/models/unions/v2_account_activities_response1.py)&#93;, [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[V2AccountActivitiesResponse1](trader_api/models/unions/v2_account_activities_response1.py)&#93;</code> -- returns an array of Account activities

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AccountConfigurationsApi

> Source: [AccountConfigurationsApi](trader_api/apis/account_configurations_api.py)

<details>
<summary><code>def get_account_config(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountConfigurations, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

gets the current account configuration values

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account_configurations_api.with_raw_response.get_account_config()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountConfigurations
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.account_configurations_api.with_raw_response.get_account_config()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountConfigurations
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[AccountConfigurations](trader_api/models/account_configurations.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountConfigurations](trader_api/models/account_configurations.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def patch_account_config(*, body: AccountConfigurations | AccountConfigurationsDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountConfigurations, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates and returns the current account configuration values

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account_configurations_api.with_raw_response.patch_account_config()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountConfigurations
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.account_configurations_api.with_raw_response.patch_account_config()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountConfigurations
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountConfigurations](trader_api/models/account_configurations.py) \| [AccountConfigurationsDict](trader_api/models/account_configurations.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[AccountConfigurations](trader_api/models/account_configurations.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountConfigurations](trader_api/models/account_configurations.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Accounts

> Source: [Accounts](trader_api/apis/accounts.py)

<details>
<summary><code>def get_account(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Account, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the account associated with the API key.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.accounts.with_raw_response.get_account()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Account
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.accounts.with_raw_response.get_account()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Account
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Account](trader_api/models/account.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Account](trader_api/models/account.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CalendarApi

> Source: [CalendarApi](trader_api/apis/calendar_api.py)

<details>
<summary><code>def get_calendar(*, start: RFC3339DateTime | None = None, end: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Calendar], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the market calendar.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.calendar_api.with_raw_response.get_calendar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Calendar]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.calendar_api.with_raw_response.get_calendar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Calendar]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>start</code> | <code>RFC3339DateTime \| None</code> | The first date to retrieve data for (inclusive)<br>**Default**: <code>None</code> |
| <code>end</code> | <code>RFC3339DateTime \| None</code> | The last date to retrieve data for (inclusive)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;list&#91;[Calendar](trader_api/models/calendar.py)&#93;, [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Calendar](trader_api/models/calendar.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ClockApi

> Source: [ClockApi](trader_api/apis/clock_api.py)

<details>
<summary><code>def get_clock(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Clock, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The clock API serves the current market timestamp, whether or not the market is currently open, as well as the times of the next market open and close.

Returns the market clock.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.clock_api.with_raw_response.get_clock()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Clock
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.clock_api.with_raw_response.get_clock()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Clock
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Clock](trader_api/models/clock.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Clock](trader_api/models/clock.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Orders

> Source: [Orders](trader_api/apis/orders.py)

<details>
<summary><code>def delete_all_orders(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[CanceledOrderResponse], DeleteAllOrdersErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Attempts to cancel all open orders. A response will be provided for each order that is attempted to be cancelled. If an order is no longer cancelable, the server will respond with status 500 and reject the request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.delete_all_orders()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CanceledOrderResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteAllOrdersErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.delete_all_orders()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CanceledOrderResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteAllOrdersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;list&#91;[CanceledOrderResponse](trader_api/models/canceled_order_response.py)&#93;, [DeleteAllOrdersErrorBody](trader_api/errors/delete_all_orders_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[CanceledOrderResponse](trader_api/models/canceled_order_response.py)&#93;</code> -- Multi-Status with body.

an array of objects that include the order id and http status code for each status request.

**On `Failure`**: `error` is <code>[DeleteAllOrdersErrorBody](trader_api/errors/delete_all_orders_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 500 | <code>[RawError](trader_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](trader_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_order_by_order_id(order_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteOrderByOrderIdErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Attempts to cancel an Open Order. If the order is no longer cancelable, the request will be rejected with status 422; otherwise accepted with return status 204.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.delete_order_by_order_id(order_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteOrderByOrderIdErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.delete_order_by_order_id(order_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteOrderByOrderIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>UUID</code> | order id |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;None, [DeleteOrderByOrderIdErrorBody](trader_api/errors/delete_order_by_order_id_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteOrderByOrderIdErrorBody](trader_api/errors/delete_order_by_order_id_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[RawError](trader_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](trader_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_orders(*, status: Status1OrStr | None = None, limit: int | None = None, after: str | None = None, until: str | None = None, direction: DirectionOrStr | None = None, nested: bool | None = None, symbols: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Order], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of orders for the account, filtered by the supplied query parameters.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.get_all_orders()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Order]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.get_all_orders()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Order]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>status</code> | <code>[Status1OrStr](trader_api/models/enums/status1.py) \| None</code> | Order status to be queried. open, closed or all. Defaults to open.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of orders in response. Defaults to 50 and max is 500.<br>**Default**: <code>None</code> |
| <code>after</code> | <code>str \| None</code> | The response will include only ones submitted after this timestamp (exclusive.)<br>**Default**: <code>None</code> |
| <code>until</code> | <code>str \| None</code> | The response will include only ones submitted until this timestamp (exclusive.)<br>**Default**: <code>None</code> |
| <code>direction</code> | <code>[DirectionOrStr](trader_api/models/enums/direction.py) \| None</code> | The chronological order of response based on the submission time. asc or desc. Defaults to desc.<br>**Default**: <code>None</code> |
| <code>nested</code> | <code>bool \| None</code> | If true, the result will roll up multi-leg orders under the legs field of primary order.<br>**Default**: <code>None</code> |
| <code>symbols</code> | <code>str \| None</code> | A comma-separated list of symbols to filter by (ex. “AAPL,TSLA,MSFT”). A currency pair is required for crypto orders (ex. “BTCUSD,BCHUSD,LTCUSD,ETCUSD”).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;list&#91;[Order](trader_api/models/order.py)&#93;, [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Order](trader_api/models/order.py)&#93;</code> -- Successful response

An array of Order objects

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_order_by_order_id(order_id: UUID, *, nested: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Order, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a single order for the given order_id.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.get_order_by_order_id(order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.get_order_by_order_id(order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>UUID</code> | order id |
| <code>nested</code> | <code>bool \| None</code> | If true, the result will roll up multi-leg orders under the legs field of primary order.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Order](trader_api/models/order.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Order](trader_api/models/order.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def patch_order_by_order_id(order_id: UUID, body: PatchOrderRequest | PatchOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Order, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Replaces a single order with updated parameters. Each parameter overrides the corresponding attribute of the existing order. The other attributes remain the same as the existing order.

A success return code from a replaced order does NOT guarantee the existing open order has been replaced. If the existing open order is filled before the replacing (new) order reaches the execution venue, the replacing (new) order is rejected, and these events are sent in the trade_updates stream channel. 

While an order is being replaced, buying power is reduced by the larger of the two orders that have been placed (the old order being replaced, and the newly placed order to replace it). If you are replacing a buy entry order with a higher limit price than the original order, the buying power is calculated based on the newly placed order. If you are replacing it with a lower limit price, the buying power is calculated based on the old order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.patch_order_by_order_id(order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.patch_order_by_order_id(order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>UUID</code> | order id |
| <code>body</code> | <code>[PatchOrderRequest](trader_api/models/patch_order_request.py) \| [PatchOrderRequestDict](trader_api/models/patch_order_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Order](trader_api/models/order.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Order](trader_api/models/order.py)</code> -- Successful response

The new Order object with the new order ID.

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def post_order(body: Order | OrderDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Order, PostOrderErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Places a new order for the given account. An order request may be rejected if the account is not authorized for trading, or if the tradable balance is insufficient to fill the order..

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.post_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostOrderErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.post_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[Order](trader_api/models/order.py) \| [OrderDict](trader_api/models/order.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Order](trader_api/models/order.py), [PostOrderErrorBody](trader_api/errors/post_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Order](trader_api/models/order.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostOrderErrorBody](trader_api/errors/post_order_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[RawError](trader_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](trader_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## PortfolioHistoryApi

> Source: [PortfolioHistoryApi](trader_api/apis/portfolio_history_api.py)

<details>
<summary><code>def get_account_portfolio_history(*, period: str | None = None, timeframe: str | None = None, date_end: Date | None = None, extended_hours: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PortfolioHistory, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns timeseries data about equity and profit/loss (P/L) of the account in requested timespan.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.portfolio_history_api.with_raw_response.get_account_portfolio_history()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortfolioHistory
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.portfolio_history_api.with_raw_response.get_account_portfolio_history()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortfolioHistory
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>period</code> | <code>str \| None</code> | The duration of the data in <number> + <unit>, such as 1D, where <unit> can be D for day, W for week, M for month and A for year. Defaults to 1M.<br>**Default**: <code>None</code> |
| <code>timeframe</code> | <code>str \| None</code> | The resolution of time window. 1Min, 5Min, 15Min, 1H, or 1D. If omitted, 1Min for less than 7 days period, 15Min for less than 30 days, or otherwise 1D.<br>**Default**: <code>None</code> |
| <code>date_end</code> | <code>Date \| None</code> | The date the data is returned up to, in “YYYY-MM-DD” format. Defaults to the current market date (rolls over at the market open if extended_hours is false, otherwise at 7am ET)<br>**Default**: <code>None</code> |
| <code>extended_hours</code> | <code>str \| None</code> | If true, include extended hours in the result. This is effective only for timeframe less than 1D.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[PortfolioHistory](trader_api/models/portfolio_history.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PortfolioHistory](trader_api/models/portfolio_history.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Positions

> Source: [Positions](trader_api/apis/positions.py)

<details>
<summary><code>def delete_all_open_positions(*, cancel_orders: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[PositionClosedReponse], DeleteAllOpenPositionsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Closes (liquidates) all of the account’s open long and short positions. A response will be provided for each order that is attempted to be cancelled. If an order is no longer cancelable, the server will respond with status 500 and reject the request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.positions.with_raw_response.delete_all_open_positions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PositionClosedReponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteAllOpenPositionsErrorBody
```

**Async**

```python
result = await async_client.positions.with_raw_response.delete_all_open_positions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PositionClosedReponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteAllOpenPositionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cancel_orders</code> | <code>bool \| None</code> | If true is specified, cancel all open orders before liquidating all positions.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;list&#91;[PositionClosedReponse](trader_api/models/position_closed_reponse.py)&#93;, [DeleteAllOpenPositionsErrorBody](trader_api/errors/delete_all_open_positions_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[PositionClosedReponse](trader_api/models/position_closed_reponse.py)&#93;</code> -- Multi-Status with body.

an array of PositionClosed responses

**On `Failure`**: `error` is <code>[DeleteAllOpenPositionsErrorBody](trader_api/errors/delete_all_open_positions_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 500 | <code>[RawError](trader_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](trader_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_open_position(symbol_or_asset_id: str, *, qty: float | None = None, percentage: float | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Order, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Closes (liquidates) the account’s open position for the given symbol. Works for both long and short positions.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.positions.with_raw_response.delete_open_position(symbol_or_asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.positions.with_raw_response.delete_open_position(symbol_or_asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol_or_asset_id</code> | <code>str</code> | symbol or assetId |
| <code>qty</code> | <code>float \| None</code> | the number of shares to liquidate. Can accept up to 9 decimal points. Cannot work with percentage<br>**Default**: <code>None</code> |
| <code>percentage</code> | <code>float \| None</code> | percentage of position to liquidate. Must be between 0 and 100. Would only sell fractional if position is originally fractional. Can accept up to 9 decimal points. Cannot work with qty<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Order](trader_api/models/order.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Order](trader_api/models/order.py)</code> -- Successful response

Returns the order created to close out this position

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_open_positions(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Position], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The positions API provides information about an account’s current open positions. The response will include information such as cost basis, shares traded, and market value, which will be updated live as price information is updated. Once a position is closed, it will no longer be queryable through this API

Retrieves a list of the account’s open positions

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.positions.with_raw_response.get_all_open_positions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Position]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.positions.with_raw_response.get_all_open_positions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Position]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;list&#91;[Position](trader_api/models/position.py)&#93;, [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Position](trader_api/models/position.py)&#93;</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_open_position(symbol_or_asset_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Position, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the account’s open position for the given symbol or assetId.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.positions.with_raw_response.get_open_position(symbol_or_asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Position
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.positions.with_raw_response.get_open_position(symbol_or_asset_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Position
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol_or_asset_id</code> | <code>str</code> | symbol or assetId |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Position](trader_api/models/position.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Position](trader_api/models/position.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Watchlists

> Source: [Watchlists](trader_api/apis/watchlists.py)

<details>
<summary><code>def add_asset_to_watchlist(watchlist_id: UUID, *, body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Watchlist, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Append an asset for the symbol to the end of watchlist asset list

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.add_asset_to_watchlist(watchlist_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.add_asset_to_watchlist(watchlist_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>watchlist_id</code> | <code>UUID</code> | watchlist id |
| <code>body</code> | <code>[AddAssetToWatchlistRequest](trader_api/models/add_asset_to_watchlist_request.py) \| [AddAssetToWatchlistRequestDict](trader_api/models/add_asset_to_watchlist_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Watchlist](trader_api/models/watchlist.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Watchlist](trader_api/models/watchlist.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def add_asset_to_watchlist_by_name(name: str, *, body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Watchlist, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Append an asset for the symbol to the end of watchlist asset list

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.add_asset_to_watchlist_by_name(name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.add_asset_to_watchlist_by_name(name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str</code> | name of the watchlist |
| <code>body</code> | <code>[AddAssetToWatchlistRequest](trader_api/models/add_asset_to_watchlist_request.py) \| [AddAssetToWatchlistRequestDict](trader_api/models/add_asset_to_watchlist_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Watchlist](trader_api/models/watchlist.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Watchlist](trader_api/models/watchlist.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_watchlist_by_id(watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete a watchlist. This is a permanent deletion.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.delete_watchlist_by_id(watchlist_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.delete_watchlist_by_id(watchlist_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>watchlist_id</code> | <code>UUID</code> | watchlist id |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;None, [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_watchlist_by_name(name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete a watchlist. This is a permanent deletion.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.delete_watchlist_by_name(name)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.delete_watchlist_by_name(name)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str</code> | name of the watchlist |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;None, [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_watchlist_by_id(watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Watchlist, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a watchlist identified by the ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.get_watchlist_by_id(watchlist_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.get_watchlist_by_id(watchlist_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>watchlist_id</code> | <code>UUID</code> | watchlist id |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Watchlist](trader_api/models/watchlist.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Watchlist](trader_api/models/watchlist.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_watchlist_by_name(name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Watchlist, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a watchlist by name

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.get_watchlist_by_name(name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.get_watchlist_by_name(name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str</code> | name of the watchlist |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Watchlist](trader_api/models/watchlist.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Watchlist](trader_api/models/watchlist.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_watchlists(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Watchlist], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the list of watchlists registered under the account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.get_watchlists()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Watchlist]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.get_watchlists()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Watchlist]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;list&#91;[Watchlist](trader_api/models/watchlist.py)&#93;, [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Watchlist](trader_api/models/watchlist.py)&#93;</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def post_watchlist(body: PostWatchlistRequest | PostWatchlistRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Watchlist, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new watchlist with initial set of assets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.post_watchlist(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.post_watchlist(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PostWatchlistRequest](trader_api/models/post_watchlist_request.py) \| [PostWatchlistRequestDict](trader_api/models/post_watchlist_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Watchlist](trader_api/models/watchlist.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Watchlist](trader_api/models/watchlist.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_asset_from_watchlist(watchlist_id: UUID, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Watchlist, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete one entry for an asset by symbol name

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.remove_asset_from_watchlist(watchlist_id, symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.remove_asset_from_watchlist(watchlist_id, symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>watchlist_id</code> | <code>UUID</code> | Watchlist ID |
| <code>symbol</code> | <code>str</code> | symbol name to remove from the watchlist content |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Watchlist](trader_api/models/watchlist.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Watchlist](trader_api/models/watchlist.py)</code> -- Returns the updated watchlist

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_watchlist_by_id(watchlist_id: UUID, *, body: PostWatchlistRequest | PostWatchlistRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Watchlist, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the name and/or content of watchlist

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.update_watchlist_by_id(watchlist_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.update_watchlist_by_id(watchlist_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>watchlist_id</code> | <code>UUID</code> | watchlist id |
| <code>body</code> | <code>[PostWatchlistRequest](trader_api/models/post_watchlist_request.py) \| [PostWatchlistRequestDict](trader_api/models/post_watchlist_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Watchlist](trader_api/models/watchlist.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Watchlist](trader_api/models/watchlist.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_watchlist_by_name(name: str, *, body: PostWatchlistRequest | PostWatchlistRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Watchlist, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the name and/or content of watchlist

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.watchlists.with_raw_response.update_watchlist_by_name(name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.watchlists.with_raw_response.update_watchlist_by_name(name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Watchlist
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str</code> | name of the watchlist |
| <code>body</code> | <code>[PostWatchlistRequest](trader_api/models/post_watchlist_request.py) \| [PostWatchlistRequestDict](trader_api/models/post_watchlist_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](trader_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](trader_api/core/results.py)&#91;[Watchlist](trader_api/models/watchlist.py), [RawError](trader_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Watchlist](trader_api/models/watchlist.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](trader_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

