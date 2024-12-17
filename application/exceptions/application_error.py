# application/exceptions/application_error.py
class ApplicationError(Exception):
    """Clase base para errores de la capa de aplicación."""
    pass

class NotFoundError(ApplicationError):
    """Excepción para entidades no encontradas."""
    def __init__(self, message: str):
        super().__init__(message)
