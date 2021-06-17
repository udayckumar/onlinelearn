class OnlineLearing:

    def __init__(self):
        pass

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, courses):
        self._courses = []
        self._courses.extend(courses)

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, users):
        self._users = []
        self._users.extend(users)
