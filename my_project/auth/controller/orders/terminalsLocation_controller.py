from t08_flask_mysql.app.my_project.auth.service import terminalsLocation_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TerminalsLocationController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = terminalsLocation_service