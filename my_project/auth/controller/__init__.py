
from .orders.terminalCity_controller import TerminalCityController
from .orders.terminals_controller import TerminalsController
from .orders.technicalsManufacturers_controller import TechnicalsManufacturersController
from .orders.terminalsLocation_controller import TerminalsLocationController
from .orders.terminalCountry_controller import TerminalCountryController
from .orders.service_controller import ServiceController
from .orders.serviceTypes_controller import ServiceTypesController
from .orders.technicians_controller import TechniciansController
from .orders.invoice_controller import InvoiceController
from .orders.payment_controller import PaymentController

technicalsManufacturers_controller = TechnicalsManufacturersController()
terminals_controller = TerminalsController()
terminalsLocation_controller = TerminalsLocationController()
terminalCity_controller = TerminalCityController()
terminalCountry_controller = TerminalCountryController()
service_controller = ServiceController()
serviceTypes_controller = ServiceTypesController()
technicians_controller = TechniciansController()
invoice_controller = InvoiceController()
payment_controller = PaymentController()