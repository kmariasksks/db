from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class TechnicalsManufacturers(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "technicalsManufacturers"

    TechnicalsManufacturersID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Manufacturername: str = db.Column(db.String(60))
    ManufacturerContact: str = db.Column(db.String(15))
    TerminalID = db.Column(db.Integer, db.ForeignKey('Terminals.TerminalID'))

    def __repr__(self) -> str:
        return f"TechnicalsManufacturers({self.TechnicalsManufacturersID}, {self.Manufacturername}, {self.ManufacturerContact}, {self.TerminalID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "TechnicalsManufacturersID": self.TechnicalsManufacturersID,
            "Manufacturername": self.Manufacturername,
            "ManufacturerContact": self.ManufacturerContact,
            "TerminalID": self.TerminalID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TechnicalsManufacturers:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = TechnicalsManufacturers(Manufacturername=dto_dict.get("Manufacturername"),
                    ManufacturerContact=dto_dict.get("ManufacturerContact"),
                    TerminalID=dto_dict.get("TerminalID"))

        return obj
