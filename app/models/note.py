# Copyright (c) 2023 Daniel Gabay


class Note:
    def __init__(self, note_id: int, user_id: int, note_title: str, note_content: str):
        self._note_id = note_id
        self._user_id = user_id
        self._note_title = note_title
        self._note_content = note_content

    @staticmethod
    def from_json(json_data) -> 'Note':
        note_id = json_data.get('id')
        user_id = json_data.get('user_id')
        note_title = json_data.get('note_title')
        note_content = json_data.get('note_content')
        return Note(note_id, user_id, note_title, note_content)

    def to_json(self) -> dict:
        return {
            'id': self._note_id,
            'user_id': self._user_id,
            'note_title': self._note_title,
            'note_content': self._note_content
        }
