import datetime

from matplotlib import pyplot as plt

from Application import Application
from ApplicationsList import ApplicationsList
from Status import Status
from db import Db
import pandas as pd


def data_table(dictionary, columns):
    df = pd.DataFrame(dictionary.values() ,index=dictionary.keys(), columns=columns)
    return df.to_html()


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

    def Status_filter(self, status: Status):
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

    def status_insight(self):
        status_insight = {}
        for application in self.applicationsList.return_list():
            status_insight[application.get_status().name] = status_insight.get(application.get_status().name, 0) + 1

        return status_insight

    def status_pie_chart(self):
        status_insight = self.status_insight()
        labels = list(status_insight.keys())
        values = list(status_insight.values())

        figure, ax = plt.subplots(figsize=(4, 4))
        ax.set_xlabel('Status of job applications')
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        figure.tight_layout()
        return figure

    def job_board_insight(self):
        job_board_insight = {}
        for application in self.applicationsList.return_list():
            job_board_insight[application.get_job_board()] = job_board_insight.get(application.get_job_board(), 0) + 1

        if '' in job_board_insight:
            job_board_insight['Unknown'] = job_board_insight.pop('')

        return job_board_insight

    def job_board_pie_chart(self):
        job_board_insight = self.job_board_insight()
        labels = (job_board_insight.keys())
        values = (job_board_insight.values())
        figure, ax = plt.subplots(figsize=(4, 4))
        ax.set_xlabel('Job boards in applications')
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        figure.tight_layout()
        return figure

