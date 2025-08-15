import datetime

from Application import Application
from ApplicationsList import ApplicationsList
from db import Db

class ApplicationsManager:
    def __init__(self):
        self.applicationsList = ApplicationsList()
        self.db = Db()

    def add_entry(self, job_title: str, date: datetime, company: str, job_board: str):
        entry = Application(job_title=job_title, company=company, date=date, job_board=job_board)
        self.db.add_entry(entry)

    def return_entry_list(self) -> list[Application]:
        return self.applicationsList.return_list()

    def remove_entry(self, application: Application):
        self.db.remove_entry(application)

    def return_entry(self, application_id: int) -> Application | None:
        for application in self.applicationsList.return_list():
            if application.get_id() == application_id:
                return application
        return None

    def load_data(self):
        self.applicationsList.return_list().clear()
        for application in self.db.load_data():
            self.applicationsList.add_entry(Application(
                application_id=application[0],
                job_title=application[1],
                company=application[2],
                date=application[3],
                status=application[4],
                job_board=application[5]
            ))