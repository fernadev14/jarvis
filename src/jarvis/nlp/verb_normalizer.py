class VerbNormalizer:

    def __init__(self):

        self.verbs = {

            "abreme": "abre",
            "abrime": "abre",
            "abrelo": "abre",
            "abrela": "abre",

            "ejecutame": "ejecuta",
            "ejecutalo": "ejecuta",
            "ejecutala": "ejecuta",

            "iniciame": "inicia",
            "inicialo": "inicia",
            "iniciala": "inicia",

            "lanzame": "lanza",
            "lanzalo": "lanza",
            "lanzala": "lanza",
        }

    def normalize(
        self,
        text,
    ):

        words = text.split()

        if not words:
            return text

        words[0] = self.verbs.get(
            words[0],
            words[0],
        )

        return " ".join(
            words,
        )
