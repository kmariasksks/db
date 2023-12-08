from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

Payment_has_Invoice = db.Table('Payment_has_Invoice',
    db.Column('PaymentID', db.Integer, db.ForeignKey('Payment.PaymentID'), primary_key=True),
    db.Column('InvoiceID', db.Integer, db.ForeignKey('Invoice.InvoiceID'), primary_key=True),
    extend_existing = True
)
class Payment(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "Payment"

    PaymentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PaymentDate: str = db.Column(db.Date)
    AmountPaid: str = db.Column(db.Float(precision=2))
    InvoiceID = db.Column(db.Integer, db.ForeignKey('Invoice.InvoiceID'))

    invoices = db.relationship('Invoice', secondary=Payment_has_Invoice, backref=db.backref('payments_associated', lazy='dynamic'))
    def __repr__(self) -> str:
        return f"Service({self.PaymentID}, {self.PaymentDate}, {self.AmountPaid}, {self.InvoiceID})"



    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "PaymentID": self.PaymentID,
            "PaymentDate": self.PaymentDate,
            "AmountPaid": self.AmountPaid,
            "InvoiceID": self.InvoiceID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> tuple[Payment, list[int]]:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Payment(PaymentDate=dto_dict.get("PaymentDate"),
                      AmountPaid=dto_dict.get("AmountPaid"),
                           InvoiceID=dto_dict.get("InvoiceID"))

        return obj
