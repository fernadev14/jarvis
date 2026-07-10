class ApplicationFilter:

    BLACKLIST_NAMES = {

        "Portal",

        "Visual Studio Code - URL Handler",

        "IBus Wayland",

        "Emoji Choice",

        "Events and Tasks Reminders",

    }

    BLACKLIST_EXECUTABLES = {

        "ibus",

    }

    def allow(self, app):

        if app.name in self.BLACKLIST_NAMES:
            return False

        if app.executable in self.BLACKLIST_EXECUTABLES:
            return False

        return True
