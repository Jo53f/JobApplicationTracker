import datetime

from Application import Application
from Applications import Applications

class ApplicationsManager:
    def __init__(self):
        self.applications = Applications()

    def add_entry(self, job_title: str, date: datetime, company: str):
        entry = Application(job_title=job_title, company=company, date=date)
        self.applications.add_entry(entry)

    def return_entry_list(self) -> list[Application]:
        return self.applications.return_list()