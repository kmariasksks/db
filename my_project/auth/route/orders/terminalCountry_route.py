from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import terminalCountry_controller
from t08_flask_mysql.app.my_project.auth.domain import TerminalCountry

terminalCountry_bp = Blueprint('terminalCountry', __name__, url_prefix='/terminalCountry')

@terminalCountry_bp.get('')
def get_all_terminalCountry() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(terminalCountry_controller.find_all()), HTTPStatus.OK)


@terminalCountry_bp.post('')
def create_terminalCountrys() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    terminalCountrys = TerminalCountry.create_from_dto(content)
    terminalCountry_controller.create(terminalCountrys)
    return make_response(jsonify(terminalCountrys.put_into_dto()), HTTPStatus.CREATED)


@terminalCountry_bp.get('/<int:terminalCountrys_id>')
def get_terminalCountrys(terminalCountrys_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(terminalCountry_controller.find_by_id(terminalCountrys_id)), HTTPStatus.OK)


@terminalCountry_bp.put('/<int:terminalCountrys_id>')
def update_terminalCountrys(terminalCountrys_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response obCountry
    """
    content = request.get_json()
    terminalCountrys = TerminalCountry.create_from_dto(content)
    terminalCountry_controller.update(terminalCountrys_id, terminalCountrys)
    return make_response("TerminalCountry updated", HTTPStatus.OK)


@terminalCountry_bp.patch('/<int:terminalCountrys_id>')
def patch_terminalCountrys(terminalCountrys_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    terminalCountry_controller.patch(terminalCountrys_id, content)
    return make_response("TerminalCountry updated", HTTPStatus.OK)


@terminalCountry_bp.delete('/<int:terminalCountrys_id>')
def delete_terminalCountrys(terminalCountrys_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    terminalCountry_controller.delete(terminalCountrys_id)
    return make_response("TerminalCountry deleted", HTTPStatus.OK)
