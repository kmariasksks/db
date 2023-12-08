from t08_flask_mysql.app.my_project.auth.dao import serviceTypes_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ServiceTypesService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = serviceTypes_dao
