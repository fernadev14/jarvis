from pathlib import Path

from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType

from jarvis.resources.launcher import ResourceLauncher

launcher = ResourceLauncher()

launcher.open(
    Resource(
        id="1",
        name="Documents",
        resource_type=ResourceType.FOLDER,
        path=str(
            Path.home() / "Documents"
        ),
    )
)

launcher.open(
    Resource(
        id="1",
        name="prueba.txt",
        resource_type=ResourceType.FILE,
        path=str(
            Path.home() / "Documents" / "prueba.txt"
        ),
    )
)
