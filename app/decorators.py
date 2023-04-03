# Copyright (c) 2023 Daniel Gabay

from functools import wraps
from http import HTTPStatus

from flask_smorest import abort

from app.exceptions.notes_data_access_layer_exceptions import *


def view_exception_handler(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ServiceInternalException as ex:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=str(ex))
        except (NoteIdIsNotFoundException, NoNotesForUserId) as ex:
            abort(HTTPStatus.NOT_FOUND, message=str(ex))

    return decorated_function
