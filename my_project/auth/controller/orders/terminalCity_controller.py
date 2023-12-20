from t08_flask_mysql.app.my_project.auth.service import terminalCity_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TerminalCityController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = terminalCity_service