
class ReservaError(Exception):
    """Excepcion general para los errores de reservas."""
    pass


class EstadoReservaError(ReservaError):
    """Excepcion para operaciones no permitidas."""
    pass
