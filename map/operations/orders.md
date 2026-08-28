<!-- Generated file — do not edit; regenerated with the SDK. -->

# Orders — operations

Accessor: `client.orders` · Source: `alpaca/apis/orders.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.orders.delete_all_orders

- **Route**: `DELETE /v2/orders`
- **Signature**: `def delete_all_orders(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[CanceledOrderResponse]`
- **Returns (raw)**: `ApiResult[list[CanceledOrderResponse], DeleteAllOrdersErrorBody]`
- **Error**: `DeleteAllOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [500, anything unmapped]

| Type | Source |
| --- | --- |
| `CanceledOrderResponse` | `alpaca/models/canceled_order_response.py` |
| `DeleteAllOrdersErrorBody` | `alpaca/errors/delete_all_orders_error.py` |

### client.orders.delete_order_by_order_id

- **Route**: `DELETE /v2/orders/{order_id}`
- **Signature**: `def delete_order_by_order_id(order_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`
- **Params**: `order_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteOrderByOrderIdErrorBody]`
- **Error**: `DeleteOrderByOrderIdErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [422, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteOrderByOrderIdErrorBody` | `alpaca/errors/delete_order_by_order_id_error.py` |

### client.orders.get_all_orders

- **Route**: `GET /v2/orders`
- **Signature**: `def get_all_orders(*, status: Status1OrStr | None = None, limit: int | None = None, after: str | None = None, until: str | None = None, direction: DirectionOrStr | None = None, nested: bool | None = None, symbols: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query · `limit` — query · `after` — query · `until` — query · `direction` — query · `nested` — query · `symbols` — query
- **Returns (parsed)**: `list[Order]`
- **Returns (raw)**: `ApiResult[list[Order], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Status1OrStr` | `alpaca/models/enums/status1.py` |
| `DirectionOrStr` | `alpaca/models/enums/direction.py` |
| `Order` | `alpaca/models/order.py` |

### client.orders.get_order_by_order_id

- **Route**: `GET /v2/orders/{order_id}`
- **Signature**: `def get_order_by_order_id(order_id: UUID, *, nested: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`
- **Params**: `order_id` — path · `nested` — query
- **Returns (parsed)**: `Order`
- **Returns (raw)**: `ApiResult[Order, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order` | `alpaca/models/order.py` |

### client.orders.patch_order_by_order_id

- **Route**: `PATCH /v2/orders/{order_id}`
- **Signature**: `def patch_order_by_order_id(order_id: UUID, body: PatchOrderRequest | PatchOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`, `body`
- **Params**: `order_id` — path · `body` — JSON body
- **Returns (parsed)**: `Order`
- **Returns (raw)**: `ApiResult[Order, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PatchOrderRequest` | `alpaca/models/patch_order_request.py` |
| `PatchOrderRequestDict` | `alpaca/models/patch_order_request.py` |
| `Order` | `alpaca/models/order.py` |

### client.orders.post_order

- **Route**: `POST /v2/orders`
- **Signature**: `def post_order(body: Order | OrderDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Order`
- **Returns (raw)**: `ApiResult[Order, PostOrderErrorBody]`
- **Error**: `PostOrderErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [403, 422, anything unmapped]

| Type | Source |
| --- | --- |
| `Order` | `alpaca/models/order.py` |
| `OrderDict` | `alpaca/models/order.py` |
| `PostOrderErrorBody` | `alpaca/errors/post_order_error.py` |

