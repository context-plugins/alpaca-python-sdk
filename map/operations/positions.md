<!-- Generated file — do not edit; regenerated with the SDK. -->

# Positions — operations

Accessor: `client.positions` · Source: `trader_api/apis/positions.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.positions.delete_all_open_positions

- **Route**: `DELETE /v2/positions`
- **Auth**: `api_key` AND `api_secret`
- **Signature**: `def delete_all_open_positions(*, cancel_orders: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cancel_orders` — query
- **Returns (parsed)**: `list[PositionClosedReponse]`
- **Returns (raw)**: `ApiResult[list[PositionClosedReponse], DeleteAllOpenPositionsErrorBody]`
- **Error**: `DeleteAllOpenPositionsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [500, anything unmapped]

| Type | Source |
| --- | --- |
| `PositionClosedReponse` | `trader_api/models/position_closed_reponse.py` |
| `DeleteAllOpenPositionsErrorBody` | `trader_api/errors/delete_all_open_positions_error.py` |

### client.positions.delete_open_position

- **Route**: `DELETE /v2/positions/{symbol_or_asset_id}`
- **Auth**: `api_key` AND `api_secret`
- **Signature**: `def delete_open_position(symbol_or_asset_id: str, *, qty: float | None = None, percentage: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol_or_asset_id`
- **Params**: `symbol_or_asset_id` — path · `qty` — query · `percentage` — query
- **Returns (parsed)**: `Order`
- **Returns (raw)**: `ApiResult[Order, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order` | `trader_api/models/order.py` |

### client.positions.get_all_open_positions

- **Route**: `GET /v2/positions`
- **Auth**: `api_key` AND `api_secret`
- **Signature**: `def get_all_open_positions(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[Position]`
- **Returns (raw)**: `ApiResult[list[Position], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Position` | `trader_api/models/position.py` |

### client.positions.get_open_position

- **Route**: `GET /v2/positions/{symbol_or_asset_id}`
- **Auth**: `api_key` AND `api_secret`
- **Signature**: `def get_open_position(symbol_or_asset_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol_or_asset_id`
- **Params**: `symbol_or_asset_id` — path
- **Returns (parsed)**: `Position`
- **Returns (raw)**: `ApiResult[Position, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Position` | `trader_api/models/position.py` |

