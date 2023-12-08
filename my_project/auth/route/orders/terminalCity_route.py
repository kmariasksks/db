from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import terminalCity_controller
from t08_flask_mysql.app.my_project.auth.domain import TerminalCity

terminalCity_bp = Blueprint('terminalCity', __name__, url_prefix='/terminalCity')

@terminalCity_bp.get('')
def get_all_terminalCity() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(terminalCity_controller.find_all()), HTTPStatus.OK)


@terminalCity_bp.post('')
def create_terminalCitys() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    terminalCitys = TerminalCity.create_from_dto(content)
    terminalCity_controller.create(terminalCitys)
    return make_response(jsonify(terminalCitys.put_into_dto()), HTTPStatus.CREATED)


@terminalCity_bp.get('/<int:terminalCitys_id>')
def get_terminalCitys(terminalCitys_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(terminalCity_controller.find_by_id(terminalCitys_id)), HTTPStatus.OK)


@terminalCity_bp.put('/<int:terminalCitys_id>')
def update_terminalCitys(terminalCitys_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    terminalCitys = TerminalCity.create_from_dto(content)
    terminalCity_controller.update(terminalCitys_id, terminalCitys)
    return make_response("TerminalCity updated", HTTPStatus.OK)


@terminalCity_bp.patch('/<int:terminalCitys_id>')
def patch_terminalCitys(terminalCitys_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    terminalCity_controller.patch(terminalCitys_id, content)
    return make_response("TerminalCity updated", HTTPStatus.OK)


@terminalCity_bp.delete('/<int:terminalCitys_id>')
def delete_terminalCitys(terminalCitys_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    terminalCity_controller.delete(terminalCitys_id)
    return make_response("TerminalCity deleted", HTTPStatus.OK)
