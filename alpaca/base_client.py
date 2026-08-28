from __future__ import annotations

from typing import Generic

from .core import RawClientT
from .server.environment import Environment, validate_environment
from .server.server import Server
from .server.server_config import LiveConfig, PaperConfig, ServerConfig

DEFAULT_TIMEOUT = 30.0


class BaseAlpacaClient(Generic[RawClientT]):
    _raw_client: RawClientT

    def __init__(
        self, *, environment: Environment = "paper", base_url: str | None = None, timeout: float = DEFAULT_TIMEOUT
    ) -> None:
        if not timeout > 0:
            raise ValueError(f"timeout must be greater than 0; got {timeout!r}")
        self._server = Server(
            validate_environment(environment),
            (
                ServerConfig(paper=PaperConfig(base_url=base_url), live=LiveConfig(base_url=base_url))
                if base_url is not None
                else ServerConfig()
            ),
        )
