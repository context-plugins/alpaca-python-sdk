from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from ..core import UrlTemplate
from .environment import Environment


class PaperConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://paper-api.alpaca.markets"


class LiveConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://api.alpaca.markets"


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    paper: PaperConfig = Field(default_factory=PaperConfig)
    live: LiveConfig = Field(default_factory=LiveConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        variant = self.paper if environment == "paper" else self.live
        return UrlTemplate(base_url=variant.base_url, path=path)
