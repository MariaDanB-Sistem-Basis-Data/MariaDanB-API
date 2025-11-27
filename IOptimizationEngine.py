from __future__ import annotations
from abc import ABC, abstractmethod
from .IParsedQuery import IParsedQuery
__all__ = ["IOptimizationEngine"]


class IOptimizationEngine(ABC):
    @abstractmethod
    def parse_query(self, query: str) -> IParsedQuery:
        ...

    @abstractmethod
    def optimize_query(self, parsed_query: IParsedQuery) -> IParsedQuery:
        ...

    @abstractmethod
    def optimize_query_non_join(self, parsed_query: IParsedQuery) -> IParsedQuery:
        ...

    @abstractmethod
    def get_cost(self, parsed_query: IParsedQuery) -> int:
        ...

