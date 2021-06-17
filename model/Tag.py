class Tag:

    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        self._tag_id = tag_id

    @property
    def tag_name(self):
        return self._tags

    @tag_name.setter
    def tag_name(self, tags):
        self._tags = []
        self._tags.extend(tags)
