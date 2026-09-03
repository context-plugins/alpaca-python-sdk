<!-- Generated file — do not edit; regenerated with the SDK. -->

# Accounts — operations

Accessor: `client.accounts` · Source: `trader_api/apis/accounts.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.accounts.get_account

- **Route**: `GET /v2/account`
- **Auth**: `api_key` AND `api_secret`
- **Signature**: `def get_account(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `Account`
- **Returns (raw)**: `ApiResult[Account, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Account` | `trader_api/models/account.py` |

