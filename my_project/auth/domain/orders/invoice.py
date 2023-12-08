from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto




class Invoice(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "Invoice"

    InvoiceID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    InvoiceDate: str = db.Column(db.Date)
    InvoiceCost: str = db.Column(db.Float(precision=2))
    ServiceID = db.Column(db.Integer, db.ForeignKey('Service.ServiceID'))

    # payments = db.relationship('Payment', secondary=invoices_has_payments, backref='related_invoices')

    def __repr__(self) -> str:
        return f"Service({self.InvoiceID}, {self.InvoiceDate}, {self.InvoiceCost}, {self.ServiceID})"

    def get_routes(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "PaymentID": self.PaymentID,
            "PaymentDate": self.PaymentDate,
            "AmountPaid": self.AmountPaid,
            "payments": list(map(lambda a: a.put_into_dto(), self.payments)),
        }

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "InvoiceID": self.InvoiceID,
            "InvoiceDate": self.InvoiceDate,
            "InvoiceCost": self.InvoiceCost,
            "ServiceID": self.ServiceID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> tuple[Invoice, list[int]]:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Invoice(InvoiceDate=dto_dict.get("InvoiceDate"),
                      InvoiceCost=dto_dict.get("InvoiceCost"),
                           ServiceID=dto_dict.get("ServiceID"))

        return obj, dto_dict.get("payments")
