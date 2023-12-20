from t08_flask_mysql.app.my_project.auth.dao import service_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ServiceService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = service_dao
