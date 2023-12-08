from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import terminals_controller
from t08_flask_mysql.app.my_project.auth.domain import Terminals

terminals_bp = Blueprint('terminals', __name__, url_prefix='/terminals')

@terminals_bp.get('')
def get_all_terminals() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(terminals_controller.find_all()), HTTPStatus.OK)


@terminals_bp.post('')
def create_terminal() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    terminal = Terminals.create_from_dto(content)
    terminals_controller.create(terminal)
    return make_response(jsonify(terminal.put_into_dto()), HTTPStatus.CREATED)


@terminals_bp.get('/<int:terminal_id>')
def get_terminal(terminal_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(terminals_controller.find_by_id(terminal_id)), HTTPStatus.OK)


@terminals_bp.put('/<int:terminal_id>')
def update_terminal(terminal_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    terminal = Terminals.create_from_dto(content)
    terminals_controller.update(terminal_id, terminal)
    return make_response("Terminal updated", HTTPStatus.OK)


@terminals_bp.patch('/<int:terminal_id>')
def patch_terminal(terminal_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    terminals_controller.patch(terminal_id, content)
    return make_response("Terminal updated", HTTPStatus.OK)


@terminals_bp.delete('/<int:terminal_id>')
def delete_terminal(terminal_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    terminals_controller.delete(terminal_id)
    return make_response("Terminal deleted", HTTPStatus.OK)
