from pathlib import Path


class CandidateFilter:

    def filter(
        self,
        query: str,
        files: list[Path],
    ) -> list[Path]:

        query = query.lower().strip()

        candidates = []

        for file in files:

            stem = file.stem.lower()
            full = file.name.lower()

            if stem.startswith(query):

                candidates.append(file)

                continue

            if query in stem:

                candidates.append(file)

                continue

            if full.startswith(query):

                candidates.append(file)

                continue

            if query in full:

                candidates.append(file)

        return candidates
