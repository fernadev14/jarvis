from jarvis.search.confidence import Confidence
from jarvis.search.item import SearchItem
from jarvis.search.result import SearchResult
from jarvis.search.selectors.candidate_selector import CandidateSelector


selector = CandidateSelector()


def result(name, score):

    return SearchResult(

        item=SearchItem(

            resource_id=name,

            name=name,

            aliases=[],
        ),

        score=score,

        confidence=Confidence.HIGH,
    )


tests = [

    [

        result("chrome", 100),

        result("chromium", 98),

        result("firefox", 70),

    ],

    [

        result("contrato.pdf", 95),

        result("contrato empresa.docx", 94),

        result("contrato viejo.docx", 93),

    ],

    [

        result("github", 100),

    ],

]

for results in tests:

    print("-" * 40)

    selected = selector.select(results)

    for candidate in selected:

        print(candidate.item.name, candidate.score)
