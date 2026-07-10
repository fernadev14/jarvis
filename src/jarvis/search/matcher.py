from difflib import SequenceMatcher

from jarvis.search.item import SearchItem


class Matcher:

    def score(
        self,
        query: str,
        item: SearchItem,
    ) -> float:

        query = query.lower().strip()

        name = item.name.lower()

        #
        # Coincidencia exacta
        #

        if query == name:

            return 100

        #
        # Alias exacto
        #

        if query in [a.lower() for a in item.aliases]:

            return 98

        #
        # Contenido
        #

        if query in name:

            return 90

        #
        # Contenido en alias
        #

        for alias in item.aliases:

            if query in alias.lower():

                return 88

        #
        # Similaridad difusa
        #

        best = SequenceMatcher(
            None,
            query,
            name,
        ).ratio()

        for alias in item.aliases:

            ratio = SequenceMatcher(
                None,
                query,
                alias.lower(),
            ).ratio()

            best = max(best, ratio)

        return best * 80
