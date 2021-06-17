class Lesson:
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def lesson_name(self):
        return self._lesson_name

    @lesson_name.setter
    def lesson_name(self, lesson_name):
        self._lesson_name = lesson_name

    @property
    def videos(self):
        return self._videos

    @videos.setter
    def videos(self, videos):
        self._videos = videos
