from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class TerminalsLocation(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "TerminalsLocation"

    LocationID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    StreetName: str = db.Column(db.String(45))
    BuildingNumber: str = db.Column(db.String(45))
    PostalCode: str = db.Column(db.String(45))
    TerminalID = db.Column(db.Integer, db.ForeignKey('Terminals.TerminalID'))

    def __repr__(self) -> str:
        return f"TerminalsLocation({self.LocationID}, {self.StreetName}, {self.BuildingNumber}, {self.PostalCode}, {self.TerminalID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "LocationID": self.LocationID,
            "StreetName": self.StreetName,
            "BuildingNumber": self.BuildingNumber,
            "PostalCode": self.PostalCode,
            "TerminalID": self.TerminalID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TerminalsLocation:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = TerminalsLocation(StreetName=dto_dict.get("StreetName"),
                    BuildingNumber=dto_dict.get("BuildingNumber"),
                                PostalCode=dto_dict.get("PostalCode"),
                    TerminalID=dto_dict.get("TerminalID"))

        return obj
