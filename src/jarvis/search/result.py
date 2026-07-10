from dataclasses import dataclass

from jarvis.search.item import SearchItem


@dataclass
class SearchResult:

    item: SearchItem

    score: float
