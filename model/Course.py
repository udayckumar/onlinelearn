class Course:
    def __init__(self):
        pass

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        self._course_id = course_id

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, course_name):
        self._course_name = course_name

    @property
    def lessons(self):
        return self._lessons

    @lessons.setter
    def lessons(self, lessons):
        self._lessons = lessons
