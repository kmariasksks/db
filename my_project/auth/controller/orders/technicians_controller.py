from t08_flask_mysql.app.my_project.auth.service import technicians_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TechniciansController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = technicians_service