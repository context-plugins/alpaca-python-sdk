from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteOrderByOrderIdErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteOrderByOrderIdError:
    def map(self, status_code: int, content: bytes) -> DeleteOrderByOrderIdErrorBody:
        match status_code:
            case 422:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_order_by_order_id_error_mapper: Final[ErrorMapper[DeleteOrderByOrderIdErrorBody]] = _DeleteOrderByOrderIdError()
