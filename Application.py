import datetime

class Application:
    def __init__(self, job_title: str, status = "applied", date: datetime = datetime.date.today(), company=None, application_id=None, job_board=None):
        self.job_title = job_title
        self.status = status
        self.date = date
        self.company = company
        self.application_id = application_id
        self.job_board = job_board

    def get_job_title(self):
        return self.job_title

    def get_company(self):
        return self.company

    def get_date(self):
        if self.date == '':
            self.date = None
        return self.date

    def get_status(self):
        return self.status

    def get_id(self) -> int:
        return self.application_id

    def get_job_board(self) -> str:
        return self.job_board

    def set_applied(self):
        self.status = "applied"

    def set_rejected(self):
        self.status = "rejected"

    def set_accepted(self):
        self.status = "accepted"

    def set_test_stage(self):
        self.status = "test stage"

    def set_interview(self):
        self.status = "interview"