<!-- Generated file — do not edit; regenerated with the SDK. -->

# PortfolioHistoryApi — operations

Accessor: `client.portfolio_history_api` · Source: `trader_api/apis/portfolio_history_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.portfolio_history_api.get_account_portfolio_history

- **Route**: `GET /v2/account/portfolio/history`
- **Auth**: `api_key` AND `api_secret`
- **Signature**: `def get_account_portfolio_history(*, period: str | None = None, timeframe: str | None = None, date_end: Date | None = None, extended_hours: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `period` — query · `timeframe` — query · `date_end` — query · `extended_hours` — query
- **Returns (parsed)**: `PortfolioHistory`
- **Returns (raw)**: `ApiResult[PortfolioHistory, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PortfolioHistory` | `trader_api/models/portfolio_history.py` |

