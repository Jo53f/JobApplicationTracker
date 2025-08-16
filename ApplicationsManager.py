import datetime

from Application import Application
from ApplicationsList import ApplicationsList
from Status import Status
from db import Db

class ApplicationsManager:
    def __init__(self):
        self.applicationsList = ApplicationsList()
        self.db = Db()

    def add_entry(
            self,
            job_title: str,
            date: datetime,
            company: str,
            job_board: str,
            status: Status = Status.APPLIED
    ):
        entry = Application(
            job_title=job_title,
            company=company,
            date=date,
            job_board=job_board,
            status=status
        )
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

    def update_entry(self, application: Application, job_title, company, date, job_board, status):
        application.job_title = job_title
        application.company = company
        application.date = date
        application.job_board = job_board
        application.status = status
        self.db.update_entry(application)

    def load_data(self):
        self.applicationsList.return_list().clear()
        for application in self.db.load_data():
            self.applicationsList.add_entry(Application(
                application_id=application[0],
                job_title=application[1],
                company=application[2],
                date=application[3],
                status=Status(application[4]),
                job_board=application[5]
            ))

    def Date_filter(self, date: datetime.date):
        filtered_applications = []
        for application in self.applicationsList.return_list():
            if application.get_date() == date:
                filtered_applications.append(application)
        return filtered_applications

    def Job_board_filter(self, job_board: str):
        filtered_applications = []
        for application in self.applicationsList.return_list():
            if application.get_job_board() == job_board:
                filtered_applications.append(application)
        return filtered_applications

    def Status_filter(self, status: str):
        filtered_applications = []
        for application in self.applicationsList.return_list():
            if application.get_status() == status:
                filtered_applications.append(application)
        return filtered_applications

    def Company_filter(self, company: str):
        filtered_applications = []
        for application in self.applicationsList.return_list():
            if application.get_company() == company:
                filtered_applications.append(application)
        return filtered_applications