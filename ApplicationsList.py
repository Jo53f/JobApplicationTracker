from Application import Application


class ApplicationsList:
    """
    Holds a list of applications.

    Attributes
    ----------
    applicationsList: list[Application]
        List of job applications.

    Methods
    -------
    return_list() -> list[Application]
    add_entry(application: Application)
    remove_entry(application: Application)
    """

    def __init__(self):
        """
        Create an empty list, to be filled with applications later.
        """
        self.applicationsList = []

    def return_list(self) -> list[Application]:
        """
        Returns
        -------
        applicationsList: list[Application]
            return the list of applications.
        """
        return self.applicationsList

    def add_entry(self, application: Application):
        """
        Adds an application to Applications List.

        Parameters
        ----------
        application: Application

        """
        self.applicationsList.append(application)

    def remove_entry(self, application: Application):
        """
        Removes an application from Applications List.

        Parameters
        ----------
        application
        """
        self.applicationsList.remove(application)
