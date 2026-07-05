class EntityNormalizer:

    STOP_WORDS = {
        # artículos
        "el",
        "la",
        "los",
        "las",
        "un",
        "una",
        "unos",
        "unas",

        # posesivos
        "mi",
        "mis",
        "tu",
        "tus",
        "su",
        "sus",

        # preposiciones
        "de",
        "del",
        "para",
        "por",
        "con",

        # palabras de ruido
        "carpeta",
        "archivo",
        "archivos",
        "documento",
        "documentos",
        "fichero",
        "ficheros",
        "app",
        "aplicacion",
        "aplicación",
        "programa",
        "sitio",
        "pagina",
        "página",
        "web",
    }

    def normalize(self, entity: str) -> str:

        words = entity.lower().split()

        words = [
            word
            for word in words
            if word not in self.STOP_WORDS
        ]

        return " ".join(words).strip()
