class FileIndexUpdater:

    def created(
        self,
        path,
    ):

        print(
            "Añadiendo:",
            path,
        )

    def modified(
        self,
        path,
    ):

        print(
            "Actualizando:",
            path,
        )

    def deleted(
        self,
        path,
    ):

        print(
            "Eliminando:",
            path,
        )
