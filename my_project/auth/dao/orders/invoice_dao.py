from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Invoice
from t08_flask_mysql.app.my_project.auth.domain.orders.payment import Payment, Payment_has_Invoice


class InvoiceDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Invoice

    def find_payments(self, InvoiceID: int) -> List[Payment]:
        """
        Find buses associated with a specific driver.
        :param driver_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the driver
        payment_ids = (
            session.query(Payment_has_Invoice.c.PaymentID)
            .filter(Payment_has_Invoice.c.InvoiceID == InvoiceID)
            .all()
        )

        # Extract bus IDs from the result
        payment_ids = [payment_id for (payment_id,) in payment_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        payments = session.query(Payment).filter(Payment.id.in_(payment_ids)).all()

        return [payment.put_into_dto() for payment in payments]

