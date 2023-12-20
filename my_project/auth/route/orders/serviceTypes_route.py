from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import serviceTypes_controller
from t08_flask_mysql.app.my_project.auth.domain import ServiceTypes

serviceTypes_bp = Blueprint('serviceTypes', __name__, url_prefix='/serviceTypes')

@serviceTypes_bp.get('')
def get_all_serviceTypes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(serviceTypes_controller.find_all()), HTTPStatus.OK)


@serviceTypes_bp.post('')
def create_serviceType() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    serviceType = ServiceTypes.create_from_dto(content)
    serviceTypes_controller.create(serviceType)
    return make_response(jsonify(serviceType.put_into_dto()), HTTPStatus.CREATED)


@serviceTypes_bp.get('/<int:serviceType_id>')
def get_serviceType(serviceType_id: int) -> Response:
    """
    Gets city_serviceTypes
    :return: Response object
    """
    return make_response(jsonify(serviceTypes_controller.find_by_id(serviceType_id)), HTTPStatus.OK)


@serviceTypes_bp.put('/<int:serviceType_id>')
def update_serviceType(serviceType_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    serviceType = ServiceTypes.create_from_dto(content)
    serviceTypes_controller.update(serviceType_id, serviceType)
    return make_response("serviceType updated", HTTPStatus.OK)


@serviceTypes_bp.patch('/<int:serviceType_id>')
def patch_serviceType(serviceType_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    serviceTypes_controller.patch(serviceType_id, content)
    return make_response("serviceType updated", HTTPStatus.OK)


@serviceTypes_bp.delete('/<int:serviceType_id>')
def delete_serviceType(serviceType_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    serviceTypes_controller.delete(serviceType_id)
    return make_response("serviceType deleted", HTTPStatus.OK)
