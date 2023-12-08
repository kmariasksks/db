from t08_flask_mysql.app.my_project.auth.dao import terminalCity_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TerminalCityService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = terminalCity_dao
