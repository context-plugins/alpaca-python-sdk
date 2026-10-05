from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteAllOpenPositionsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteAllOpenPositionsError:
    def map(self, status_code: int, content: bytes) -> DeleteAllOpenPositionsErrorBody:
        match status_code:
            case 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_all_open_positions_error_mapper: Final[
    ErrorMapper[DeleteAllOpenPositionsErrorBody]
] = _DeleteAllOpenPositionsError()
