from t08_flask_mysql.app.my_project.auth.service import terminalCountry_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TerminalCountryController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = terminalCountry_service