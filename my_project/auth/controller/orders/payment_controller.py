from t08_flask_mysql.app.my_project.auth.service import payment_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from http import HTTPStatus
from flask import abort
from typing import List


class PaymentController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = payment_service
