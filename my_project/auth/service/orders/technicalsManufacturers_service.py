from t08_flask_mysql.app.my_project.auth.dao import technicalsManufacturers_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TechnicalsManufacturersService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = technicalsManufacturers_dao
