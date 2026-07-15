from jarvis.models.resource_type import ResourceType
from jarvis.resources.repository import ResourceRepository

from jarvis.search.factories.resource_factory import (
    ResourceFactory,
)


repository = ResourceRepository()

factory = ResourceFactory()

record = type(
    "Record",
    (),
    {
        "name": "contrato",
        "path": "/tmp/contrato.pdf",
    },
)()

resource = factory.build(
    record,
)

print(
    repository.contains(
        resource.id,
    )
)

repository.add(
    resource,
)

print(
    repository.contains(
        resource.id,
    )
)

print(
    repository.get(
        resource.id,
    )
)

repository.remove(
    resource.id,
)

print(
    repository.contains(
        resource.id,
    )
)
