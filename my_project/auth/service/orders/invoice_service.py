from t08_flask_mysql.app.my_project.auth.dao import invoice_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class InvoiceService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = invoice_dao
