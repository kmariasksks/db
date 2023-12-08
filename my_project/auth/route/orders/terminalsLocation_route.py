from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import terminalsLocation_controller
from t08_flask_mysql.app.my_project.auth.domain import TerminalsLocation

terminalsLocation_bp = Blueprint('terminalsLocations', __name__, url_prefix='/terminalsLocations')

@terminalsLocation_bp.get('')
def get_all_terminalsLocation() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(terminalsLocation_controller.find_all()), HTTPStatus.OK)


@terminalsLocation_bp.post('')
def create_terminalLocation() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response objectLocation
    """
    content = request.get_json()
    terminalLocation = TerminalsLocation.create_from_dto(content)
    terminalsLocation_controller.create(terminalLocation)
    return make_response(jsonify(terminalLocation.put_into_dto()), HTTPStatus.CREATED)


@terminalsLocation_bp.get('/<int:terminalLocation_id>')
def get_terminalLocation(terminalLocation_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response objectLocation
    """
    return make_response(jsonify(terminalsLocation_controller.find_by_id(terminalLocation_id)), HTTPStatus.OK)


@terminalsLocation_bp.put('/<int:terminalLocation_id>')
def update_terminalLocation(terminalLocation_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    terminalLocation = TerminalsLocation.create_from_dto(content)
    terminalsLocation_controller.update(terminalLocation_id, terminalLocation)
    return make_response("TerminalLocation updated", HTTPStatus.OK)


@terminalsLocation_bp.patch('/<int:terminalLocation_id>')
def patch_terminalLocation(terminalLocation_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    terminalsLocation_controller.patch(terminalLocation_id, content)
    return make_response("TerminalLocation updated", HTTPStatus.OK)


@terminalsLocation_bp.delete('/<int:terminalLocation_id>')
def delete_terminalLocation(terminalLocation_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    terminalsLocation_controller.delete(terminalLocation_id)
    return make_response("TerminalLocation deleted", HTTPStatus.OK)
