
from .orders.terminalCountry_service import TerminalCountryService
from .orders.terminals_service import TerminalsService
from .orders.technicalsManufacturers_service import TechnicalsManufacturersService
from .orders.terminalsLocation_service import TerminalsLocationService
from .orders.terminalCity_service import TerminalCityService
from .orders.service_service import ServiceService
from .orders.serviceTypes_service import ServiceTypesService
from .orders.technicians_service import TechniciansService
from .orders.invoice_service import InvoiceService
from .orders.payment_service import PaymentService

technicalsManufacturers_service = TechnicalsManufacturersService()
terminals_service = TerminalsService()
terminalsLocation_service = TerminalsLocationService()
terminalCity_service = TerminalCityService()
terminalCountry_service = TerminalCountryService()
service_service = ServiceService()
serviceTypes_service = ServiceTypesService()
technicians_service = TechniciansService()
invoice_service = InvoiceService()
payment_service = PaymentService()