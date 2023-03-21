# Copyright (c) 2023 Daniel Gabay

from http import HTTPStatus

from flask.views import MethodView
from flask_injector import inject
from flask_smorest import Blueprint

from schemes import NoteSchema
from services.note_service import NoteService

blp = Blueprint("notes", __name__, description="Notes operations")


class NoteView(MethodView):

    @inject
    def __init__(self, note_service: NoteService):
        super().__init__()
        self._note_service = note_service


@blp.route("/note/<int:note_id>")
class NoteItemView(NoteView):

    @blp.response(HTTPStatus.OK, NoteSchema)
    def get(self, note_id: int):
        return self._note_service.get_note_id(note_id=note_id)

    @blp.response(HTTPStatus.NO_CONTENT)
    def delete(self, note_id: int):
        return self._note_service.delete_note_id(note_id=note_id)


@blp.route("/note")
class NoteListView(NoteView):

    @blp.arguments(NoteSchema)
    @blp.response(HTTPStatus.CREATED)
    def post(self, note_data: dict):
        return self._note_service.create_note(**note_data)


@blp.route("/note/user/<int:user_id>")
class NoteListView(NoteView):
    @blp.response(HTTPStatus.OK, NoteSchema(many=True))
    def get(self, user_id: int):
        return self._note_service.get_user_id_notes(user_id=user_id)
