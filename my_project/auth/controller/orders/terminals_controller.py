from t08_flask_mysql.app.my_project.auth.service import terminals_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TerminalsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = terminals_service