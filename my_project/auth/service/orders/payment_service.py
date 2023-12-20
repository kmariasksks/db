from t08_flask_mysql.app.my_project.auth.dao import payment_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class PaymentService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = payment_dao
