# Copyright (c) 2023 Daniel Gabay

from typing import List
from http import HTTPStatus

from flask_injector import inject

from data.data_access.crud_handler import RequestHandler
from di.wrappers import DatabaseServiceUrlStringWrapper
from exceptions.notes_data_access_layer_exceptions import NoteIdIsNotFoundException, ServiceInternalException, \
    NoNotesForUserId
from models.note import Note


class NotesDataAccess:

    @inject
    def __init__(self, database_service_url: DatabaseServiceUrlStringWrapper):
        self._database_service_url = database_service_url.value

    def create_note(self, user_id: int, note_title: str, note_content: str) -> Note:
        payload = {"user_id": user_id, "note_title": note_title, "note_content": note_content}
        response = RequestHandler.perform_post_request(
            url=self._database_service_url,
            endpoint='note',
            payload=payload)
        if response.status_code == HTTPStatus.CREATED:
            return Note.from_json(response.json())
        elif response.status_code == HTTPStatus.NOT_FOUND:
            raise NoNotesForUserId("User with the id {user_id} is not found.".format(user_id=user_id))

    def get_user_id_notes(self, user_id: int) -> List[Note]:
        response = RequestHandler.perform_get_request(
            url=self._database_service_url,
            endpoint=f'note/user/{user_id}', )
        if response.status_code == HTTPStatus.OK:
            return [Note.from_json(note_json_item) for note_json_item in response.json()]
        elif response.status_code == HTTPStatus.NOT_FOUND:
            raise NoNotesForUserId("Cannot find notes for user id {user_id}.".format(user_id=user_id))
        else:
            raise ServiceInternalException(response.json().get("message"))

    def get_note_id(self, note_id: int) -> Note:
        response = RequestHandler.perform_get_request(
            url=self._database_service_url,
            endpoint=f'note/{note_id}')
        if response.status_code == HTTPStatus.OK:
            return Note.from_json(response.json())
        elif response.status_code == HTTPStatus.NOT_FOUND:
            raise NoteIdIsNotFoundException(f"Note with the id {note_id} is not found.")
        else:
            raise ServiceInternalException(response.json().get("message"))

    def update_note_id(self, note_id: int, note_title: str, note_content: str) -> Note:
        payload = {"note_title": note_title, "note_content": note_content}
        response = RequestHandler.perform_patch_request(
            url=self._database_service_url,
            endpoint=f'note/{note_id}',
            payload=payload)
        if response.status_code == HTTPStatus.OK:
            return Note.from_json(response.json())
        elif response.status_code == HTTPStatus.NOT_FOUND:
            raise NoteIdIsNotFoundException(f"Note with the id {note_id} is not found.")
        else:
            raise ServiceInternalException(response.json().get("message"))

    def delete_note_id(self, note_id: int) -> None:
        response = RequestHandler.perform_delete_request(
            url=self._database_service_url,
            endpoint=f'note/{note_id}')
        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NoteIdIsNotFoundException(f"Note with the id {note_id} is not found.")
        else:
            raise ServiceInternalException(response.json().get("message"))
