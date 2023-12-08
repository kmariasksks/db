from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import payment_controller
from t08_flask_mysql.app.my_project.auth.service import invoice_service
from t08_flask_mysql.app.my_project.auth.domain import Payment

payment_bp = Blueprint('payment', __name__, url_prefix='/payment')

@payment_bp.get('')
def get_all_payment() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(payment_controller.find_all()), HTTPStatus.OK)


@payment_bp.get('/<int:PaymentID>/payments')
def get_all_payments_from_invoices(PaymentsID) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(payment_controller.find_payments(PaymentsID)), HTTPStatus.OK)


@payment_bp.post('')
def create_payment() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    payment = Payment.create_from_dto(content)
    payment_controller.create(payment)
    return make_response(jsonify(payment.put_into_dto()), HTTPStatus.CREATED)


@payment_bp.get('/<int:payments_id>')
def get_payments(payments_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(payment_controller.find_by_id(payments_id)), HTTPStatus.OK)

@payment_bp.get('/<int:payment_id>/invoice')
def get_invoices(payment_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(payment_controller.find_by_id(payment_id)), HTTPStatus.OK)


@payment_bp.put('/<int:payments_id>')
def update_payments(payments_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Responseinvoice
    """
    content = request.get_json()
    payments = Payment.create_from_dto(content)
    payment_controller.update(payments_id, payments)
    return make_response("payment updated", HTTPStatus.OK)


@payment_bp.patch('/<int:payment_id>')
def patch_payment(payment_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    payment_controller.patch(payment_id, content)
    return make_response("payment updated", HTTPStatus.OK)


@payment_bp.delete('/<int:payment_id>')
def delete_payments(payment_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    payment_controller.delete(payment_id)
    return make_response("payment deleted", HTTPStatus.OK)
