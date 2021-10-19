class Entry():
    """
    Property class to set Entry object
    """
    def __init__(self):
        self._title = ''
        self._link = ''
        self._summary = ''
        self._source = ''
        self._tags = []
        self._published = ''

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, summary):
        self._summary = summary

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        self._source = source

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags

    @property
    def published(self):
        return self._published

    @published.setter
    def published(self, published):
        self._published = published
