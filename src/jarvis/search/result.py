from dataclasses import dataclass

from jarvis.search.item import SearchItem
from jarvis.search.confidence import Confidence


@dataclass
class SearchResult:

    item: SearchItem

    score: float

    confidence: Confidence
