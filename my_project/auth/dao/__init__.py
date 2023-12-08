
# orders DB
from .orders.terminals_dao import TerminalsDAO
from .orders.technicalsManufacturers_dao import TechnicalsManufacturersDAO
from .orders.terminalsLocation_dao import TerminalsLocationDAO
from .orders.terminalCity_dao import TerminalCityDAO
from .orders.terminalCountry_dao import TerminalCountryDAO
from .orders.service_dao import ServiceDAO
from .orders.serviceTypes_dao import ServiceTypesDAO
from .orders.technicians_dao import TechniciansDAO
from .orders.invoice_dao import InvoiceDAO
from .orders.payment_dao import PaymentDAO


technicalsManufacturers_dao = TechnicalsManufacturersDAO()
terminals_dao = TerminalsDAO()
terminalsLocation_dao = TerminalsLocationDAO()
terminalCity_dao = TerminalCityDAO()
terminalCountry_dao = TerminalCountryDAO()
service_dao = ServiceDAO()
serviceTypes_dao = ServiceTypesDAO()
technicians_dao = TechniciansDAO()
invoice_dao = InvoiceDAO()
payment_dao = PaymentDAO()