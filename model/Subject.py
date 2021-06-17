class Subject:

    def __init__(self):
        pass

    @property
    def subject_name(self):
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        self._subject_name = subject_name

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def subjects(self, courses):
        self._courses = courses
