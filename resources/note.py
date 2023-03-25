# Copyright (c) 2023 Daniel Gabay

from http import HTTPStatus
from flask_jwt_extended import jwt_required

from flask.views import MethodView
from flask_injector import inject
from flask_smorest import Blueprint

from decorators import view_exception_handler
from schemes import NoteSchema, NoteUpdateSchema
from services.note_service import NoteService

blp = Blueprint("notes", __name__, description="Notes operations")


class NoteView(MethodView):

    @inject
    def __init__(self, note_service: NoteService):
        super().__init__()
        self._note_service = note_service


@blp.route("/note")
class NoteCreationView(NoteView):

    @jwt_required()
    @blp.arguments(NoteSchema)
    @blp.response(HTTPStatus.CREATED)
    @view_exception_handler
    def post(self, note_data: dict) -> dict:
        return self._note_service.create_note(**note_data).to_json()


@blp.route("/note/<int:note_id>")
class NoteItemView(NoteView):

    @jwt_required()
    @blp.response(HTTPStatus.OK, NoteSchema)
    @view_exception_handler
    def get(self, note_id: int) -> dict:
        return self._note_service.get_note_id(note_id=note_id).to_json()

    @jwt_required()
    @blp.arguments(NoteUpdateSchema)
    @blp.response(HTTPStatus.OK, NoteSchema)
    @view_exception_handler
    def patch(self, note_data: dict, note_id: int) -> dict:
        return self._note_service.update_note_id(note_id=note_id, **note_data).to_json()

    @jwt_required()
    @blp.response(HTTPStatus.NO_CONTENT)
    @view_exception_handler
    def delete(self, note_id: int) -> None:
        self._note_service.delete_note_id(note_id=note_id)


@blp.route("/note/user/<int:user_id>")
class NoteListView(NoteView):

    @jwt_required()
    @blp.response(HTTPStatus.OK, NoteSchema(many=True))
    @view_exception_handler
    def get(self, user_id: int) -> list:
        return [note.to_json() for note in self._note_service.get_user_id_notes(user_id=user_id)]
