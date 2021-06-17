class User:

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def is_instructor(self):
        return self._is_instructor

    @is_instructor.setter
    def is_instructor(self, is_instructor):
        self._is_instructor = is_instructor

    # CRUD ops on Course
    def add_course(self, course):
        pass

    def edit_course(self, course):
        pass

    def remove_course(self, course):
        pass

    # CRUD ops on subject
    def add_subject(self, subject):
        pass

    def edit_subject(self, subject):
        pass

    def remove_subject(self, subject):
        pass

    # CRUD ops on tags
    def add_tag(self, tag):
        pass

    def edit_tag(self, tag):
        pass

    def remove_tag(self, tag):
        pass

    # CRUD ops on Video
    def add_video(self, Video):
        pass

    def add_video_with_tag(self, Video, Tag):
        pass

    def add_webinar(self, Webinar):
        pass

    def add_webinar_with_tag(self, Webinar, Tag):
        pass

    def most_viewed_videos(self):
        pass

    def most_viewed_courses(self):
        pass

    def most_viewed_webinars(self):
        pass
