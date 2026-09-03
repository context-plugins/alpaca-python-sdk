from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CanceledOrderResponse(SdkBaseModel):
    """Represents the result of a request to cancel and order"""

    id: Optional[UUID] = UNSET
    """orderId"""

    status: Optional[int] = UNSET
    """http response code"""


class CanceledOrderResponseDict(TypedDict):
    id: NotRequired[UUID]
    status: NotRequired[int]
