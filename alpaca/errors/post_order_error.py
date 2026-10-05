from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

PostOrderErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _PostOrderError:
    def map(self, status_code: int, content: bytes) -> PostOrderErrorBody:
        match status_code:
            case 403 | 422:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


post_order_error_mapper: Final[ErrorMapper[PostOrderErrorBody]] = _PostOrderError()
