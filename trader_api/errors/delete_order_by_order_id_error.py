from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteOrderByOrderIdErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteOrderByOrderIdError:
    def map(self, response: HttpResponse) -> DeleteOrderByOrderIdErrorBody:
        match response.status_code:
            case 422:
                return RawError(response)
            case _:
                return RawError(response)


delete_order_by_order_id_error_mapper: Final[ErrorMapper[DeleteOrderByOrderIdErrorBody]] = _DeleteOrderByOrderIdError()
