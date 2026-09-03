from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteAllOpenPositionsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteAllOpenPositionsError:
    def map(self, response: HttpResponse) -> DeleteAllOpenPositionsErrorBody:
        match response.status_code:
            case 500:
                return RawError(response)
            case _:
                return RawError(response)


delete_all_open_positions_error_mapper: Final[
    ErrorMapper[DeleteAllOpenPositionsErrorBody]
] = _DeleteAllOpenPositionsError()
