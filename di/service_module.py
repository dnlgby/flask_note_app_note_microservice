# Copyright (c) 2023 Daniel Gabay

from injector import singleton, Module

from data.data_access.notes_data_access import NotesDataAccess
from di.wrappers import DatabaseServiceUrlStringWrapper
from services.note_service import NoteService


class ServiceModule(Module):
    def configure(self, binder):
        binder.bind(DatabaseServiceUrlStringWrapper, to=DatabaseServiceUrlStringWrapper, scope=singleton)
        binder.bind(NotesDataAccess, to=NotesDataAccess, scope=singleton)
        binder.bind(NoteService, to=NoteService, scope=singleton)
