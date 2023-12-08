from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import technicalsManufacturers_controller
from t08_flask_mysql.app.my_project.auth.domain import TechnicalsManufacturers

technicalsManufacturers_bp = Blueprint('technicalsManufacturers', __name__, url_prefix='/technicalsManufacturers')

@technicalsManufacturers_bp.get('')
def get_all_technicalsManufacturers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(technicalsManufacturers_controller.find_all()), HTTPStatus.OK)


@technicalsManufacturers_bp.post('')
def create_technicalsManufacture() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    technicalsManufacture = TechnicalsManufacturers.create_from_dto(content)
    technicalsManufacturers_controller.create(technicalsManufacture)
    return make_response(jsonify(technicalsManufacture.put_into_dto()), HTTPStatus.CREATED)


@technicalsManufacturers_bp.get('/<int:technicalsManufacture_id>')
def get_technicalsManufacture(technicalsManufacture_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(technicalsManufacturers_controller.find_by_id(technicalsManufacture_id)), HTTPStatus.OK)


@technicalsManufacturers_bp.put('/<int:technicalsManufacture_id>')
def update_technicalsManufacture(technicalsManufacture_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    technicalsManufacture = TechnicalsManufacturers.create_from_dto(content)
    technicalsManufacturers_controller.update(technicalsManufacture_id, technicalsManufacture)
    return make_response("TechnicalsManufacturers updated", HTTPStatus.OK)


@technicalsManufacturers_bp.patch('/<int:technicalsManufacture_id>')
def patch_technicalsManufacture(technicalsManufacture_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    technicalsManufacturers_controller.patch(technicalsManufacture_id, content)
    return make_response("TechnicalsManufacturers updated", HTTPStatus.OK)


@technicalsManufacturers_bp.delete('/<int:technicalsManufacture_id>')
def delete_technicalsManufacture(technicalsManufacture_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    technicalsManufacturers_controller.delete(technicalsManufacture_id)
    return make_response("TechnicalsManufacturers deleted", HTTPStatus.OK)
