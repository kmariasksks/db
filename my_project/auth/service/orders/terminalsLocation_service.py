from t08_flask_mysql.app.my_project.auth.dao import terminalsLocation_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TerminalsLocationService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = terminalsLocation_dao
