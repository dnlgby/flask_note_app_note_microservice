from flask_injector import inject

from crud_handler import RequestHandler
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

        return response.json()

    def get_all_notes(self):
        response = RequestHandler.perform_get_request(self._database_service_url, 'note')
        return response.json()

    def get_note_id(self, note_id: int):
        response = RequestHandler.perform_get_request(self._database_service_url, f'note/{note_id}')
        return response.json()
