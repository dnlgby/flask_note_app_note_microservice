# Copyright (c) 2023 Daniel Gabay

class NotesPageResponse:

    def __init__(self, notes, total, page, pages):
        self._notes = notes
        self._total = total
        self._page = page
        self._pages = pages

    @property
    def notes(self):
        return self._notes

    @property
    def total(self):
        return self._total

    @property
    def page(self):
        return self._page

    @property
    def pages(self):
        return self._pages
