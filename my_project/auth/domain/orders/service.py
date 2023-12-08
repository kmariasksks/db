from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Service(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "Service"

    ServiceID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ServiceDate: str = db.Column(db.Date)
    DurationDays: str = db.Column(db.String(45))
    ServiceCost: str = db.Column(db.Float(precision=2))
    TerminalID = db.Column(db.Integer, db.ForeignKey('Terminals.TerminalID'))
    ServiceTypeID = db.Column(db.Integer, db.ForeignKey('ServiceTypes.ServiceTypeID'))
    TechnicianID = db.Column(db.Integer, db.ForeignKey('Technicians.TechnicianID'))

    def __repr__(self) -> str:
        return f"Service({self.ServiceID}, {self.ServiceDate}, {self.DurationDays}, {self.ServiceCost}, {self.TerminalID}, {self.ServiceTypeID}, {self.TechnicianID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ServiceID": self.ServiceID,
            "ServiceDate": self.ServiceDate,
            "DurationDays": self.DurationDays,
            "ServiceCost": self.ServiceCost,
            "TerminalID": self.TerminalID,
            "ServiceTypeID": self.ServiceTypeID,
            "TechnicianID": self.TechnicianID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Service:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Service(ServiceDate=dto_dict.get("ServiceDate"),
                      DurationDays=dto_dict.get("DurationDays"),
                      ServiceCost=dto_dict.get("ServiceCost"),
                      TerminalID=dto_dict.get("TerminalID"),
                      ServiceTypeID=dto_dict.get("ServiceTypeID"),
                           TechnicianID=dto_dict.get("TechnicianID"))

        return obj
