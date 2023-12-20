from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import TerminalCity

class TerminalCityDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = TerminalCity

