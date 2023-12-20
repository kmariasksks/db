from t08_flask_mysql.app.my_project.auth.dao import technicians_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TechniciansService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = technicians_dao
