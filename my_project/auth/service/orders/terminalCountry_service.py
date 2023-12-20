from t08_flask_mysql.app.my_project.auth.dao import terminalCountry_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TerminalCountryService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = terminalCountry_dao
