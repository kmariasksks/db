from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Technicians(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "Technicians"

    TechnicianID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TechnicianSurname: str = db.Column(db.String(45))
    TechnicianName: str = db.Column(db.String(45))
    TechnicianFathersname: str = db.Column(db.String(45))
    TechnicianContact: str = db.Column(db.String(45))

    def __repr__(self) -> str:
        return f"Technicians({self.TechnicianID}, {self.TechnicianSurname}, {self.TechnicianName}, {self.TechnicianFathersname}, {self.TechnicianContact})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "TechnicianID": self.TechnicianID,
            "TechnicianSurname": self.TechnicianSurname,
            "TechnicianName": self.TechnicianName,
            "TechnicianFathersname": self.TechnicianFathersname,
            "TechnicianContact": self.TechnicianContact,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Technicians:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Technicians(TechnicianSurname=dto_dict.get("TechnicianSurname"),
                          TechnicianName=dto_dict.get("TechnicianName"),
                          TechnicianFathersname=dto_dict.get("TechnicianFathersname"),
                          TechnicianContact=dto_dict.get("TechnicianContact"))

        return obj
