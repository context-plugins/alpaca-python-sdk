<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountActivities — operations

Accessor: `client.account_activities` · Source: `trader_api/apis/account_activities.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_activities.get_account_activities

- **Route**: `GET /v2/account/activities`
- **Auth**: `api_key` AND `api_secret`
- **Signature**: `def get_account_activities(*, date: RFC3339DateTime | None = None, until: RFC3339DateTime | None = None, after: RFC3339DateTime | None = None, direction: DirectionOrStr | None = None, page_size: int | None = None, page_token: str | None = None, activity_types: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `date` — query · `until` — query · `after` — query · `direction` — query · `page_size` — query · `page_token` — query · `activity_types` — query
- **Returns (parsed)**: `list[V2AccountActivitiesResponse]`
- **Returns (raw)**: `ApiResult[list[V2AccountActivitiesResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `trader_api/models/enums/direction.py` |
| `V2AccountActivitiesResponse` | `trader_api/models/unions/v2_account_activities_response.py` |

### client.account_activities.get_account_activities_by_activity_type

- **Route**: `GET /v2/account/activities/{activity_type}`
- **Auth**: `api_key` AND `api_secret`
- **Signature**: `def get_account_activities_by_activity_type(activity_type: str, *, date: RFC3339DateTime | None = None, until: RFC3339DateTime | None = None, after: RFC3339DateTime | None = None, direction: DirectionOrStr | None = None, page_size: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `activity_type`
- **Params**: `activity_type` — path · `date` — query · `until` — query · `after` — query · `direction` — query · `page_size` — query · `page_token` — query
- **Returns (parsed)**: `list[V2AccountActivitiesResponse1]`
- **Returns (raw)**: `ApiResult[list[V2AccountActivitiesResponse1], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `trader_api/models/enums/direction.py` |
| `V2AccountActivitiesResponse1` | `trader_api/models/unions/v2_account_activities_response1.py` |

