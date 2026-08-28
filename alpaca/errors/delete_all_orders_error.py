from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteAllOrdersErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteAllOrdersError:
    def map(self, response: HttpResponse) -> DeleteAllOrdersErrorBody:
        match response.status_code:
            case 500:
                return RawError(response)
            case _:
                return RawError(response)


delete_all_orders_error_mapper: Final[ErrorMapper[DeleteAllOrdersErrorBody]] = _DeleteAllOrdersError()
