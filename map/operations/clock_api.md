<!-- Generated file — do not edit; regenerated with the SDK. -->

# ClockApi — operations

Accessor: `client.clock_api` · Source: `alpaca/apis/clock_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.clock_api.get_clock

- **Route**: `GET /v2/clock`
- **Signature**: `def get_clock(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `Clock`
- **Returns (raw)**: `ApiResult[Clock, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Clock` | `alpaca/models/clock.py` |

