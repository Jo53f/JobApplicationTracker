import datetime

from matplotlib import pyplot as plt

from Application import Application
from ApplicationsList import ApplicationsList
from Status import Status
from db import Db
import pandas as pd


def data_table(dictionary, columns):
    """
    Returns a table from a dictionary with respect to columns in the format of a table for html.

    Parameters
    ----------
    dictionary: dict
        The dictionary to be converted to a table.
    columns: list[str]
        List of column names for the data table.

    Returns
    -------
    str
        A string representation of the table in html format.
    """
    df = pd.DataFrame(dictionary.values(), index=dictionary.keys(), columns=columns)
    return df.to_html()

def pie_chart(data, labels, title: str):
    """
    Generate a pie chart.

    With provided data, labels and a title, generate and return a pyplot figure with a pie chart.

    Parameters
    ----------
    data
        Value of each slice. Preferably a list of numbers.
    labels
        List of labels for each slice in the pie chart.
    title
        The title of the pie chart.

    Returns
    -------
    matplotlib.figure.Figure
        matplotlib figure object containing the pie chart.
    """
    figure, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlabel(title)
    ax.pie(data, labels=labels, autopct='%1.1f%%')
    figure.tight_layout()
    return figure


class ApplicationsManager:
    """
    Manages Applications in ApplicationsList and Database.

    A Class to manage the applications list and its connections to the database, allowing for CRUD operations.

    Attributes
    ----------
    applicationsList: ApplicationsList
        an instance of ApplicationsList to store all applications.
    db: Db
        an instance of Db to connect to the database.
    """

    def __init__(self):
        """
        Initialize the ApplicationsManager with an empty ApplicationsList and a Db instance.

        Creates an applicationsList instance to store applications locally and a Db instance to manage connections to
        the database.
        """
        self.applicationsList = ApplicationsList()
        self.db = Db()

    def add_entry(
            self,
            job_title: str,
            date: datetime.date,
            company: str,
            job_board: str,
            status: Status = Status.APPLIED
    ):
        """
        Add an application to the database.

        Creates a new Application object with the provided parameters and passes it to the Db instance's add_entry method.

        Parameters
        ----------
        job_title: str
            Title of job applied for.
        date: datetime.date
            Date application was submitted.
        company: str
            The company the application was submitted to.
        job_board: str
            Job board the application was found on.
        status: Status
            Status of the application.
        """
        entry = Application(
            job_title=job_title,
            company=company,
            date=date,
            job_board=job_board,
            status=status
        )
        self.db.add_entry(entry)

    def return_entry_list(self) -> list[Application]:
        """
        Returns a list of all applications.

        Method returns a list of Application objects stored in the ApplicationsList instance.

        Returns
        -------
        list[Application]
            List of Application objects.
        """
        return self.applicationsList.return_list()

    def remove_entry(self, application: Application):
        """
        Remove an application from the database.

        Removes an application from the database by passing the application object to the Db instance's remove_entry method.

        Parameters
        ----------
        application: Application
            The application to be removed.
        """
        self.db.remove_entry(application)

    def return_entry(self, application_id: int) -> Application | None:
        """
        Returns an application by its id.

        Searches the ApplicationsList for an application with a matching id to the one provided, and returns it if found.

        Parameters
        ----------
        application_id: int:
            The id of the application to be returned.

        Returns
        -------
        Application | None
            Application object if found, otherwise returns None.
        """
        for application in self.applicationsList.return_list():
            if application.get_id() == application_id:
                return application
        return None

    def update_entry(self, application: Application, job_title, company, date, job_board, status):
        """
        Update an existing application locally and in the database.

        Accepts the application object which is to be updated, and updates its attributes with the provided parameters.
        The updated application is then passed to the Db instance's update_entry method to also be updated in the database.

        Parameters
        ----------
        application: Application
            The application object to be updated.
        job_title: str
            The new job title.
        company: str
            The new company name.
        date: datetime.date
            The new date.
        job_board: str
            The new job board.
        status: Status
            The new status.
        """
        application.job_title = job_title
        application.company = company
        application.date = date
        application.job_board = job_board
        application.status = status
        self.db.update_entry(application)

    def load_data(self):
        """
        Load data from database into ApplicationsList.

        Loads all data from the Db instance Application table and then iterates over it to create an Application object
        for each row. Each application object is then added to the ApplicationsList.
        """
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
        """
        Filter applications by date.

        Filters the ApplicationsList by date and returns a list of Application objects matching the date.

        Parameters
        ----------
        date: datetime.date
            The date to filter by.

        Returns
        -------
        list[Application]
            List of Application objects matching the date.
        """
        filtered_applications = []
        for application in self.applicationsList.return_list():
            if application.get_date() == date:
                filtered_applications.append(application)
        return filtered_applications

    def Job_board_filter(self, job_board: str):
        """
        Filters applications by job board.

        Returns a list of Application objects matching the job board by iterating over the
        ApplicationsList and appending any matches to a new list.

        Parameters
        ----------
        job_board: str
            The job board to filter by.

        Returns
        -------
            list[Application]
                List of Application objects matching the job board.
        """
        filtered_applications = []
        for application in self.applicationsList.return_list():
            if application.get_job_board() == job_board:
                filtered_applications.append(application)
        return filtered_applications

    def Status_filter(self, status: Status):
        """
        Filters applications by status.

        Returns a list of Application objects matching the Status by iterating over the
        ApplicationsList and appending any matches to a new list.

        Parameters
        ----------
        status: str
            The status to filter by.

        Returns
        -------
            list[Application]
                List of Application objects matching the status.
        """
        filtered_applications = []
        for application in self.applicationsList.return_list():
            if application.get_status() == status:
                filtered_applications.append(application)
        return filtered_applications

    def Company_filter(self, company: str):
        """
        Filters applications by company name.

        Returns a list of Application objects matching the company name by iterating over the
        ApplicationsList and appending any matches to a new list.

        Parameters
        ----------
        company: str
            The company name to filter by.

        Returns
        -------
            list[Application]
                List of Application objects matching the company name.
        """
        filtered_applications = []
        for application in self.applicationsList.return_list():
            if application.get_company() == company:
                filtered_applications.append(application)
        return filtered_applications

    def status_insight(self):
        """
        Provides a count of applications by status.

        Counts the number of applications in the ApplicationsList by status and returns a dictionary with the status as
        the key and the count as the value.

        Returns
        -------
        dict
            A dictionary with the status as the key and the count as the value, with empty fields replaced with 'Unknown'.
        """
        status_insight = {}
        for application in self.applicationsList.return_list():
            status_insight[application.get_status().name] = status_insight.get(application.get_status().name, 0) + 1

        return status_insight

    def status_pie_chart(self):
        """
        Generates a pie chart of applications by status.

        Method generates a pie chart of applications by status using the status_insight method and returns the figure.

        Returns
        -------
        figure: matplotlib.figure.Figure
            matplotlib figure object containing the pie chart.
        """
        status_insight = self.status_insight()
        labels = list(status_insight.keys())
        values = list(status_insight.values())

        figure, ax = plt.subplots(figsize=(4, 4))
        ax.set_xlabel('Status of job applications')
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        figure.tight_layout()
        return figure

    def job_board_insight(self):
        """
        Provides a count of applications by job board.

        Method counts the occurrences of job boards and replacing empty fields for job boards to 'Unknown' and returns
        a dictionary with the job board as the key and the count as the value.

        Returns
        -------
        dict
            A dictionary with the job board as the key and the count as the value, with empty fields replaced with 'Unknown'.
        """
        job_board_insight = {}
        for application in self.applicationsList.return_list():
            job_board_insight[application.get_job_board()] = job_board_insight.get(application.get_job_board(), 0) + 1

        if '' in job_board_insight:
            job_board_insight['Unknown'] = job_board_insight.pop('')

        return job_board_insight

    def job_board_pie_chart(self):
        """
        Generates a pie chart of applications by job board.

        Method generates a pie chart of applications by job board using the job_board_insight method and returns the figure.

        Returns
        -------
        figure: matplotlib.figure.Figure
            matplotlib figure object containing the pie chart
        """
        job_board_insight = self.job_board_insight()
        labels = (job_board_insight.keys())
        values = (job_board_insight.values())
        figure, ax = plt.subplots(figsize=(4, 4))
        ax.set_xlabel('Job boards in applications')
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        figure.tight_layout()
        return figure

    def job_boards_status(self, status: Status):
        """
        Returns a dictionary of job boards and their respective counts for a given status.



        Parameters
        ----------
        status: Status
            The status the dictionary will be filtered by.

        Returns
        -------
        job_boards: dict
            A dictionary of job boards and their respective counts for a given status.
        """
        job_boards = {}
        for application in self.applicationsList.return_list():
            if application.get_status() == status:
                job_boards[application.get_job_board()] = job_boards.get(application.get_job_board(), 0) + 1

        if '' in job_boards:
            job_boards['Unknown'] = job_boards.pop('')
        return job_boards
