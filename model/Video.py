class Video:

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags

    @property
    def video_url(self):
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        self._video_url = video_url
