from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import TerminalsLocation


class TerminalsLocationDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = TerminalsLocation