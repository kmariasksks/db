from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import technicians_controller
from t08_flask_mysql.app.my_project.auth.domain import Technicians

technicians_bp = Blueprint('technicians', __name__, url_prefix='/technicians')

@technicians_bp.get('')
def get_all_technicians() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(technicians_controller.find_all()), HTTPStatus.OK)


@technicians_bp.post('')
def create_technician() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    technician = Technicians.create_from_dto(content)
    technicians_controller.create(technician)
    return make_response(jsonify(technician.put_into_dto()), HTTPStatus.CREATED)


@technicians_bp.get('/<int:technician_id>')
def get_technician(technician_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(technicians_controller.find_by_id(technician_id)), HTTPStatus.OK)


@technicians_bp.put('/<int:technician_id>')
def update_technician(technician_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    technician = Technicians.create_from_dto(content)
    technicians_controller.update(technician_id, technician)
    return make_response("technician updated", HTTPStatus.OK)


@technicians_bp.patch('/<int:technician_id>')
def patch_technician(technician_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    technicians_controller.patch(technician_id, content)
    return make_response("technician updated", HTTPStatus.OK)


@technicians_bp.delete('/<int:technician_id>')
def delete_technician(technician_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    technicians_controller.delete(technician_id)
    return make_response("technician deleted", HTTPStatus.OK)
