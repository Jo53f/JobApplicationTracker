from Application import Application

class Applications:
    def __init__(self):
        self.applicationsList = []

    def return_list(self) -> list[Application]:
        return self.applicationsList

    def add_entry(self, application: Application):
        self.applicationsList.append(application)

    def remove_entry(self, application: Application):
        self.applicationsList.remove(application)