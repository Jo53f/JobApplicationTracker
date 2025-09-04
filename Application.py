import datetime

from Status import Status


class Application:
    """
    A class to represent a single job application.

    Attributes
    ----------
    job_title: str, required
        the title of the job
    status: Status
        the status of the application (default APPLIED)
    date: datetime.date
        the date application was submitted (default datetime.date.today())
    company: str
        the name of the company the application was submitted to (default None)
    application_id: int
        application id (default None)
    job_board: str
        job board application was found on (default None)

    Methods
    -------
    get_job_title(self) -> str
        returns the job title
    get_company(self) ->str
        returns the company name
    get_date(self) -> datetime.date
        returns the date the application was submitted
    get_status(self) -> Status
        returns the status of the application
    get_id(self) -> int
        returns the application id
    get_job_board(self) -> str
        returns the job board the application was found on
    """

    def __init__(
            self,
            job_title: str,
            status: Status = Status.APPLIED,
            date: datetime.date | None = None,
            company=None,
            application_id=None,
            job_board=None
    ):
        """
        Initialize a new Application object.

        Parameters
        ----------
        job_title: str, required
        status : Status
        date : datetime.date
        company : str
        application_id : int
        job_board : str
        """
        self.job_title = job_title
        self.status = status
        if date is None:
            date = datetime.date.today()
        self.date = date
        self.company = company
        self.application_id = application_id
        self.job_board = job_board

    def get_job_title(self) -> str:
        """Get the application job title."""
        return self.job_title

    def get_company(self) -> str|None:
        """Get the application company name."""
        return self.company

    def get_date(self) -> datetime.date:
        """
        Get the application date.

        Returns
        -------
        self.date : datetime.date
        """
        return self.date

    def get_status(self) -> Status:
        """Get the application status."""
        return self.status

    def get_id(self) -> int:
        """Get the application id."""
        return self.application_id

    def get_job_board(self) -> str|None:
        """Get the application job board."""
        return self.job_board
