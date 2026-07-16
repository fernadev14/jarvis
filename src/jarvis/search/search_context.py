from dataclasses import dataclass

from jarvis.resources.repository import ResourceRepository
from jarvis.search.index import SearchIndex
from jarvis.search.index_service import IndexService


@dataclass(slots=True)
class SearchContext:

    index: SearchIndex

    repository: ResourceRepository

    service: IndexService
