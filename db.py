import mysql.connector

from Application import Application


class Db:
    """
    A class to handle database operations.

    Methods
    -------
    load_data(): list[tuple]
        Return all data from database table, application.
    add_entry(self, application: Application)
        Add an application to database table.
    remove_entry(self, application: Application)
        Remove an application from database table.
    update_entry(self, application: Application)
        Update an application in database table.
    """
    def __init__(self):
        """
        Initialize database connection and cursor
        """
        self.db = mysql.connector.connect(
            host="localhost",
            user="dev",
            password="dev_pass",
            database="jobs_db",
            port=3306
        )
        self.cursor = self.db.cursor()

    def load_data(self) -> list[tuple]:
        """
        Load all data from database table, application.

        Returns
        -------
        cursor.fetchall(): list[tuple]
        """
        self.cursor.execute("SELECT * FROM application")
        return self.cursor.fetchall()

    def add_entry(self, application: Application):
        """
        Add an application to database table.

        Parameters
        ----------
        application: Application
            The application to be added to the database.
        """
        self.cursor.execute(
            "INSERT INTO application (job_title, company, date, status, job_board) VALUES (%s, %s, %s, %s, %s)",
            (application.get_job_title(), application.get_company(), application.get_date(), application.get_status().value, application.get_job_board())
        )
        self.db.commit()

    def remove_entry(self, application: Application):
        """
        Remove an application from database table using application_id.

        Parameters
        ----------
        application: Application
            The application to be removed.
        """
        id = application.get_id()
        self.cursor.execute(
            "DELETE FROM application WHERE application_id = %s",
            (id,)
        )
        self.db.commit()

    def update_entry(self, application: Application):
        """
        Update an existing entry in the database using application_id, and new values.

        Parameters
        ----------
        application: Application
            The application to be updated.
        """
        application_id = application.get_id()
        self.cursor.execute(
            "UPDATE application SET job_title = %s, company = %s, date = %s, status = %s, job_board = %s WHERE application_id = %s",
            (application.get_job_title(), application.get_company(), application.get_date(), application.get_status(), application.get_job_board(), application_id)
        )
        self.db.commit()