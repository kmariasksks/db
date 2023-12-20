from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.terminals_route import terminals_bp
    from .orders.technicalsManufacturers_route import technicalsManufacturers_bp
    from .orders.terminalsLocation_route import terminalsLocation_bp
    from .orders.terminalCity_route import terminalCity_bp
    from .orders.terminalCountry_route import terminalCountry_bp
    from .orders.service_route import service_bp
    from .orders.serviceTypes_route import serviceTypes_bp
    from .orders.technicians_route import technicians_bp
    from .orders.invoice_route import invoice_bp
    from .orders.payment_route import payment_bp

    app.register_blueprint(terminals_bp)
    app.register_blueprint(technicalsManufacturers_bp)
    app.register_blueprint(terminalsLocation_bp)
    app.register_blueprint(terminalCity_bp)
    app.register_blueprint(terminalCountry_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(serviceTypes_bp)
    app.register_blueprint(technicians_bp)
    app.register_blueprint(invoice_bp)
    app.register_blueprint(payment_bp)