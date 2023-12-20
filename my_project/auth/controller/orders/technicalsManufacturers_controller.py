from t08_flask_mysql.app.my_project.auth.service import technicalsManufacturers_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.domain import TechnicalsManufacturers
from flask import current_app
from typing import List



class TechnicalsManufacturersController(GeneralController):
    """
    Realization of Client controller.
    """
    _service = technicalsManufacturers_service
