from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class TerminalCity(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "TerminalCity"

    TerminalCityID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    City: str = db.Column(db.String(45))
    LocationID = db.Column(db.Integer, db.ForeignKey('TerminalsLocation.LocationID'))

    def __repr__(self) -> str:
        return f"TerminalCity({self.TerminalCityID}, {self.City}, {self.LocationID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "TerminalCityID": self.TerminalCityID,
            "City": self.City,
            "LocationID": self.LocationID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TerminalCity:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = TerminalCity(City=dto_dict.get("City"),
                           LocationID=dto_dict.get("LocationID"))

        return obj
