<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountConfigurationsApi — operations

Accessor: `client.account_configurations_api` · Source: `alpaca/apis/account_configurations_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_configurations_api.get_account_config

- **Route**: `GET /v2/account/configurations`
- **Signature**: `def get_account_config(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `AccountConfigurations`
- **Returns (raw)**: `ApiResult[AccountConfigurations, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountConfigurations` | `alpaca/models/account_configurations.py` |

### client.account_configurations_api.patch_account_config

- **Route**: `PATCH /v2/account/configurations`
- **Signature**: `def patch_account_config(*, body: AccountConfigurations | AccountConfigurationsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountConfigurations`
- **Returns (raw)**: `ApiResult[AccountConfigurations, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountConfigurations` | `alpaca/models/account_configurations.py` |
| `AccountConfigurationsDict` | `alpaca/models/account_configurations.py` |

