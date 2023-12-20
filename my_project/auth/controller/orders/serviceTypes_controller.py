from t08_flask_mysql.app.my_project.auth.service import serviceTypes_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ServiceTypesController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = serviceTypes_service