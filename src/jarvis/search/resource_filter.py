from jarvis.models.resource_type import ResourceType


class ResourceFilter:

    MAP = {

        "aplicacion": ResourceType.APPLICATION,
        "app": ResourceType.APPLICATION,

        "archivo": ResourceType.FILE,
        "documento": ResourceType.FILE,

        "carpeta": ResourceType.FOLDER,
        "directorio": ResourceType.FOLDER,

        "sitio": ResourceType.WEBSITE,
        "pagina": ResourceType.WEBSITE,
        "web": ResourceType.WEBSITE,
    }

    @classmethod
    def from_context(cls, context: str):

        if not context:
            return None

        return cls.MAP.get(context.lower())
