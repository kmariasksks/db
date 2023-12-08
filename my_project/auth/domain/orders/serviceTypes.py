from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class ServiceTypes(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "ServiceTypes"

    ServiceTypeID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ServiceTypesName: str = db.Column(db.String(65))
    TechnicianID = db.Column(db.Integer, db.ForeignKey('Technicians.TechnicianID'))

    def __repr__(self) -> str:
        return f"ServiceTypes({self.ServiceTypeID}, {self.ServiceTypesName}, {self.TechnicianID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ServiceTypeID": self.ServiceTypeID,
            "ServiceTypesName": self.ServiceTypesName,
            "TechnicianID": self.TechnicianID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ServiceTypes:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ServiceTypes(ServiceTypesName=dto_dict.get("ServiceTypesName"),
                    TechnicianID=dto_dict.get("TechnicianID"))

        return obj
