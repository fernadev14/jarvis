from jarvis.core.intent import Intent
from jarvis.platforms.linux import LinuxPlatform


class ActionManager:

    def __init__(self):

        self.platform = LinuxPlatform()

    def execute(self, intent, message):

        if intent == Intent.OPEN_APP:

            app = message.replace("abre", "").strip()

            ok = self.platform.open_application(app)

            if ok:
                return f"He abierto {app}."

            return f"No encontré la aplicación {app}."

        return "Acción no implementada."
