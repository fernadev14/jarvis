import subprocess

from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class ResourceLauncher:

    def open(
        self,
        resource: Resource,
    ):

        if resource.resource_type == ResourceType.APPLICATION:

            self._open_application(
                resource,
            )

        elif resource.resource_type == ResourceType.FILE:

            self._open_file(
                resource,
            )

        elif resource.resource_type == ResourceType.FOLDER:

            self._open_folder(
                resource,
            )

        elif resource.resource_type == ResourceType.WEBSITE:

            self._open_website(
                resource,
            )

    def _open_application(
        self,
        resource: Resource,
    ):

        if not resource.executable:
            return

        subprocess.Popen(
            [resource.executable],
        )

    def _open_file(
        self,
        resource: Resource,
    ):

        if not resource.path:
            return

        subprocess.Popen(
            [
                "xdg-open",
                resource.path,
            ],
        )

    def _open_folder(
        self,
        resource: Resource,
    ):

        if not resource.path:
            return

        subprocess.Popen(
            [
                "xdg-open",
                resource.path,
            ],
        )

    def _open_website(
        self,
        resource: Resource,
    ):

        if not resource.url:
            return

        subprocess.Popen(
            [
                "xdg-open",
                resource.url,
            ],
        )
