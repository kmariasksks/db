from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import invoice_controller
from t08_flask_mysql.app.my_project.auth.service import payment_service
from t08_flask_mysql.app.my_project.auth.domain import Invoice

invoice_bp = Blueprint('invoice', __name__, url_prefix='/invoice')

@invoice_bp.get('')
def get_all_invoice() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(invoice_controller.find_all()), HTTPStatus.OK)


@invoice_bp.get('/payment')
def get_all_payment() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(invoice_controller.find_all_payment()), HTTPStatus.OK)


@invoice_bp.post('')
def create_invoices() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    invoices, payment = Invoice.create_from_dto(content)
    invoice_controller.create(invoices)
    return make_response(jsonify(invoices.put_into_dto()), HTTPStatus.CREATED)


@invoice_bp.get('/<int:invoices_id>')
def get_invoices(invoices_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(invoice_controller.find_by_id(invoices_id)), HTTPStatus.OK)


@invoice_bp.get('/payment/<int:invoice_id>')
def get_payment(invoice_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(invoice_controller.find_by_id_with_payment(invoice_id)), HTTPStatus.OK)


@invoice_bp.put('/<int:invoices_id>')
def update_invoices(invoices_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Responseinvoice
    """
    content = request.get_json()
    invoices = Invoice.create_from_dto(content)
    invoice_controller.update(invoices_id, invoices)
    return make_response("invoice updated", HTTPStatus.OK)


@invoice_bp.patch('/<int:invoice_id>')
def patch_invoice(invoice_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    invoice_controller.patch(invoice_id, content)
    return make_response("invoice updated", HTTPStatus.OK)


@invoice_bp.delete('/<int:invoice_id>')
def delete_invoices(invoice_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    invoice_controller.delete(invoice_id)
    return make_response("invoice deleted", HTTPStatus.OK)
