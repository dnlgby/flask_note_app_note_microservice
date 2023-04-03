# Copyright (c) 2023 Daniel Gabay

from marshmallow import Schema, fields


class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    note_title = fields.String(required=True)
    note_content = fields.String(required=True)


class NoteUpdateSchema(Schema):
    note_title = fields.String(required=True)
    note_content = fields.String(required=True)


class NotePageSchema(Schema):
    notes = fields.List(fields.Nested(NoteSchema), required=True)
    total = fields.Integer(required=True)
    page = fields.Integer(required=True)
    pages = fields.Integer(required=True)
