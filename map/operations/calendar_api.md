<!-- Generated file — do not edit; regenerated with the SDK. -->

# CalendarApi — operations

Accessor: `client.calendar_api` · Source: `trader_api/apis/calendar_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.calendar_api.get_calendar

- **Route**: `GET /v2/calendar`
- **Auth**: `api_key` AND `api_secret`
- **Signature**: `def get_calendar(*, start: RFC3339DateTime | None = None, end: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `start` — query · `end` — query
- **Returns (parsed)**: `list[Calendar]`
- **Returns (raw)**: `ApiResult[list[Calendar], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Calendar` | `trader_api/models/calendar.py` |

