from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteAllOrdersErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteAllOrdersError:
    def map(self, status_code: int, content: bytes) -> DeleteAllOrdersErrorBody:
        match status_code:
            case 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_all_orders_error_mapper: Final[ErrorMapper[DeleteAllOrdersErrorBody]] = _DeleteAllOrdersError()
