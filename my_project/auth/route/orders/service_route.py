from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import service_controller
from t08_flask_mysql.app.my_project.auth.domain import Service

service_bp = Blueprint('service', __name__, url_prefix='/service')

@service_bp.get('')
def get_all_service() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(service_controller.find_all()), HTTPStatus.OK)


@service_bp.post('')
def create_services() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    services = Service.create_from_dto(content)
    service_controller.create(services)
    return make_response(jsonify(services.put_into_dto()), HTTPStatus.CREATED)


@service_bp.get('/<int:services_id>')
def get_services(services_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(service_controller.find_by_id(services_id)), HTTPStatus.OK)


@service_bp.put('/<int:services_id>')
def update_services(services_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    services = Service.create_from_dto(content)
    service_controller.update(services_id, services)
    return make_response("Service updated", HTTPStatus.OK)


@service_bp.patch('/<int:service_id>')
def patch_service(service_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    service_controller.patch(service_id, content)
    return make_response("service updated", HTTPStatus.OK)


@service_bp.delete('/<int:service_id>')
def delete_services(service_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    service_controller.delete(service_id)
    return make_response("service deleted", HTTPStatus.OK)
