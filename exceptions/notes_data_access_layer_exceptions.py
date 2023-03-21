# Copyright (c) 2023 Daniel Gabay

from exceptions.note_service_exception import NoteServiceException


class DataAccessLayerException(NoteServiceException):
    def __init__(self, message):
        self.message = message


class ServiceInternalException(DataAccessLayerException):
    def __str__(self):
        return f"ServiceInternalException: {self.message}"


class NoteIdIsNotFoundException(NoteServiceException):
    def __init__(self, message):
        self.message = message


class NoNotesForUserId(NoteServiceException):
    def __init__(self, message):
        self.message = message
