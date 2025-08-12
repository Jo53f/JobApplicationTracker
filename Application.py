import datetime

class Application:
    def __init__(self, job_title: str, status = "applied", date = datetime.date.today(), company=None):
        self.job_title = job_title
        self.status = status
        self.date = date
        self.company = company

    def get_job_title(self):
        return self.job_title

    def get_company(self):
        return self.company

    def get_date(self):
        return self.date

    def get_status(self):
        return self.status

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