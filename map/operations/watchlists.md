<!-- Generated file — do not edit; regenerated with the SDK. -->

# Watchlists — operations

Accessor: `client.watchlists` · Source: `alpaca/apis/watchlists.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.watchlists.add_asset_to_watchlist

- **Route**: `POST /v2/watchlists/{watchlist_id}`
- **Signature**: `def add_asset_to_watchlist(watchlist_id: UUID, *, body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `watchlist_id`
- **Params**: `watchlist_id` — path · `body` — JSON body
- **Returns (parsed)**: `Watchlist`
- **Returns (raw)**: `ApiResult[Watchlist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AddAssetToWatchlistRequest` | `alpaca/models/add_asset_to_watchlist_request.py` |
| `AddAssetToWatchlistRequestDict` | `alpaca/models/add_asset_to_watchlist_request.py` |
| `Watchlist` | `alpaca/models/watchlist.py` |

### client.watchlists.add_asset_to_watchlist_by_name

- **Route**: `POST /v2/watchlists:by_name`
- **Signature**: `def add_asset_to_watchlist_by_name(name: str, *, body: AddAssetToWatchlistRequest | AddAssetToWatchlistRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `name` — query · `body` — JSON body
- **Returns (parsed)**: `Watchlist`
- **Returns (raw)**: `ApiResult[Watchlist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AddAssetToWatchlistRequest` | `alpaca/models/add_asset_to_watchlist_request.py` |
| `AddAssetToWatchlistRequestDict` | `alpaca/models/add_asset_to_watchlist_request.py` |
| `Watchlist` | `alpaca/models/watchlist.py` |

### client.watchlists.delete_watchlist_by_id

- **Route**: `DELETE /v2/watchlists/{watchlist_id}`
- **Signature**: `def delete_watchlist_by_id(watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `watchlist_id`
- **Params**: `watchlist_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.watchlists.delete_watchlist_by_name

- **Route**: `DELETE /v2/watchlists:by_name`
- **Signature**: `def delete_watchlist_by_name(name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `name` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.watchlists.get_watchlist_by_id

- **Route**: `GET /v2/watchlists/{watchlist_id}`
- **Signature**: `def get_watchlist_by_id(watchlist_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `watchlist_id`
- **Params**: `watchlist_id` — path
- **Returns (parsed)**: `Watchlist`
- **Returns (raw)**: `ApiResult[Watchlist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Watchlist` | `alpaca/models/watchlist.py` |

### client.watchlists.get_watchlist_by_name

- **Route**: `GET /v2/watchlists:by_name`
- **Signature**: `def get_watchlist_by_name(name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `name` — query
- **Returns (parsed)**: `Watchlist`
- **Returns (raw)**: `ApiResult[Watchlist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Watchlist` | `alpaca/models/watchlist.py` |

### client.watchlists.get_watchlists

- **Route**: `GET /v2/watchlists`
- **Signature**: `def get_watchlists(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[Watchlist]`
- **Returns (raw)**: `ApiResult[list[Watchlist], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Watchlist` | `alpaca/models/watchlist.py` |

### client.watchlists.post_watchlist

- **Route**: `POST /v2/watchlists`
- **Signature**: `def post_watchlist(body: PostWatchlistRequest | PostWatchlistRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Watchlist`
- **Returns (raw)**: `ApiResult[Watchlist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostWatchlistRequest` | `alpaca/models/post_watchlist_request.py` |
| `PostWatchlistRequestDict` | `alpaca/models/post_watchlist_request.py` |
| `Watchlist` | `alpaca/models/watchlist.py` |

### client.watchlists.remove_asset_from_watchlist

- **Route**: `DELETE /v2/watchlists/{watchlist_id}/{symbol}`
- **Signature**: `def remove_asset_from_watchlist(watchlist_id: UUID, symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `watchlist_id`, `symbol`
- **Params**: `watchlist_id` — path · `symbol` — path
- **Returns (parsed)**: `Watchlist`
- **Returns (raw)**: `ApiResult[Watchlist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Watchlist` | `alpaca/models/watchlist.py` |

### client.watchlists.update_watchlist_by_id

- **Route**: `PUT /v2/watchlists/{watchlist_id}`
- **Signature**: `def update_watchlist_by_id(watchlist_id: UUID, *, body: PostWatchlistRequest | PostWatchlistRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `watchlist_id`
- **Params**: `watchlist_id` — path · `body` — JSON body
- **Returns (parsed)**: `Watchlist`
- **Returns (raw)**: `ApiResult[Watchlist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostWatchlistRequest` | `alpaca/models/post_watchlist_request.py` |
| `PostWatchlistRequestDict` | `alpaca/models/post_watchlist_request.py` |
| `Watchlist` | `alpaca/models/watchlist.py` |

### client.watchlists.update_watchlist_by_name

- **Route**: `PUT /v2/watchlists:by_name`
- **Signature**: `def update_watchlist_by_name(name: str, *, body: PostWatchlistRequest | PostWatchlistRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `name` — query · `body` — JSON body
- **Returns (parsed)**: `Watchlist`
- **Returns (raw)**: `ApiResult[Watchlist, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostWatchlistRequest` | `alpaca/models/post_watchlist_request.py` |
| `PostWatchlistRequestDict` | `alpaca/models/post_watchlist_request.py` |
| `Watchlist` | `alpaca/models/watchlist.py` |

