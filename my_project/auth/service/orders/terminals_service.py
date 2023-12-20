from t08_flask_mysql.app.my_project.auth.dao import terminals_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TerminalsService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = terminals_dao
