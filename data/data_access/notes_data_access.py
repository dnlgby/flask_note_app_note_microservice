# Copyright (c) 2023 Daniel Gabay

from http import HTTPStatus

from flask_injector import inject

from data.data_access.crud_handler import RequestHandler
from di.wrappers import DatabaseServiceUrlStringWrapper


class NotesDataAccess:

    @inject
    def __init__(self, database_service_url: DatabaseServiceUrlStringWrapper):
        self._database_service_url = database_service_url.value

    def create_note(self, user_id: int, note_title: str, note_content: str):
        payload = {"user_id": user_id, "note_title": note_title, "note_content": note_content}
        response = RequestHandler.perform_post_request(
            url=self._database_service_url,
            endpoint='note',
            payload=payload)

        if response.status_code == HTTPStatus.CREATED:
            return response.json()

    def get_user_id_notes(self, user_id: int):
        response = RequestHandler.perform_get_request(
            url=self._database_service_url,
            endpoint=f'note/user/{user_id}',)
        return response.json()

    def get_note_id(self, note_id: int):
        response = RequestHandler.perform_get_request(
            url=self._database_service_url,
            endpoint=f'note/{note_id}')
        return response.json()

    def update_note_id(self, note_id: int, note_title: str, note_content: str):
        payload = {"note_title": note_title, "note_content": note_content}
        response = RequestHandler.perform_patch_request(
            url=self._database_service_url,
            endpoint=f'note/{note_id}',
            payload=payload)
        return response

    def delete_note_id(self, note_id: int):
        RequestHandler.perform_delete_request(
            url=self._database_service_url,
            endpoint=f'note/{note_id}')
