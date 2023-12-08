from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Terminals(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "Terminals"

    TerminalID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    GPSCoordinates: str = db.Column(db.String(100))
    DateInService = db.Column(db.Date)

    def __repr__(self) -> str:
        return f"Terminals({self.TerminalID}, {self.GPSCoordinates}, {self.DateInService})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "TerminalID": self.TerminalID,
            "GPSCoordinates": self.GPSCoordinates,
            "DateInService": self.DateInService,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Terminals:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Terminals(GPSCoordinates=dto_dict.get("GPSCoordinates"),
                    DateInService=dto_dict.get("DateInService"))

        return obj
