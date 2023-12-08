from t08_flask_mysql.app.my_project.auth.service import invoice_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from http import HTTPStatus
from flask import abort
from typing import List

class InvoiceController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = invoice_service

    def find_payments(self, PaymentID: int):
        """
        Find buses associated with a specific driver.
        :param driver_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Call the find_buses method from the DAO
        return self._service.find_payments(PaymentID)
