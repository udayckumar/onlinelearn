import User


class Student(User):

    def __init__(self):
        pass

    def get_active_courses(self):
        pass

    def get_active_lessons(self, course_id):
        pass

    def get_videos(self, lesson_id):
        # Result can be filtered by Video title and Tag names
        pass

    def get_video_details(self, video_id):
        pass

    def subscribe_course(self, course_list):
        pass

    def unsubscribe_course(self, course_list):
        pass
