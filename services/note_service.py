# Copyright (c) 2023 Daniel Gabay

from typing import List

from injector import inject

from data.data_access.notes_data_access import NotesDataAccess
from models.note import Note


class NoteService:

    @inject
    def __init__(self, notes_data_access: NotesDataAccess):
        self._notes_data_access = notes_data_access

    def create_note(self, user_id: int, note_title: str, note_content: str) -> Note:
        return self._notes_data_access.create_note(
            user_id=user_id,
            note_title=note_title,
            note_content=note_content)

    def get_user_id_notes(self, user_id: int) -> List[Note]:
        return self._notes_data_access.get_user_id_notes(user_id=user_id)

    def get_note_id(self, note_id: int) -> Note:
        return self._notes_data_access.get_note_id(
            note_id=note_id)

    def update_note_id(self, note_id: int, note_title: str, note_content: str) -> Note:
        return self._notes_data_access.update_note_id(
            note_id=note_id,
            note_title=note_title,
            note_content=note_content)

    def delete_note_id(self, note_id: int) -> None:
        return self._notes_data_access.delete_note_id(
            note_id=note_id)
