from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

PostOrderErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _PostOrderError:
    def map(self, response: HttpResponse) -> PostOrderErrorBody:
        match response.status_code:
            case 403 | 422:
                return RawError(response)
            case _:
                return RawError(response)


post_order_error_mapper: Final[ErrorMapper[PostOrderErrorBody]] = _PostOrderError()
