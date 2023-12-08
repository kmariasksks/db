from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class TerminalCountry(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "TerminalCountry"

    CountryID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Country = db.Column(db.String(45))
    TerminalCityID = db.Column(db.Integer, db.ForeignKey('TerminalCity.TerminalCityID'))

    def __repr__(self) -> str:
        return f"TerminalCountry({self.CountryID}, {self.Country}, {self.TerminalCityID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without a relationship
        :return: DTO object as a dictionary
        """
        return {
            "CountryID": self.CountryID,
            "Country": self.Country,
            "TerminalCityID": self.TerminalCityID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TerminalCountry:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = TerminalCountry(Country=dto_dict.get("Country"),
                              TerminalCityID=dto_dict.get("TerminalCityID"))

        return obj

