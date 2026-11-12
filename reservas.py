
from clientes import Cliente
from servicios import Servicio
from excepciones import ReservaError, EstadoReservaError


class Reserva:
    def __init__(self, identificador, cliente, servicio, duracion,
                 parametros=None, descuento=0, impuesto=0):

        self.__identificador = identificador
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__parametros = parametros if parametros is not None else {}
        self.__descuento = descuento
        self.__impuesto = impuesto
        self.__estado = "Pendiente"

        self.validar()
        self.__costo = self.__servicio.calcular_costo(
            self.__duracion, self.__descuento, self.__impuesto
        )

    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def validar(self):
        try:
            if not self.__identificador or not str(self.__identificador).strip():
                raise ValueError("El identificador de la reserva es obligatorio.")

            if not isinstance(self.__cliente, Cliente):
                raise ValueError("Debe registrar un cliente valido.")

            if not isinstance(self.__servicio, Servicio):
                raise ValueError("Debe seleccionar un servicio valido.")

            if isinstance(self.__duracion, bool) or not isinstance(self.__duracion, (int, float)) or self.__duracion <= 0:
                raise ValueError("La duracion debe ser mayor que cero.")

            self.__servicio.validar_parametros(**self.__parametros)

        except (ValueError, TypeError) as error:
            raise ReservaError("No fue posible crear la reserva: " + str(error)) from error

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise EstadoReservaError("Solo se pueden confirmar reservas pendientes.")

        self.__estado = "Confirmada"
        return True

    def cancelar(self):
        if self.__estado == "Procesada":
            raise EstadoReservaError("No se puede cancelar una reserva procesada.")

        if self.__estado == "Cancelada":
            raise EstadoReservaError("La reserva ya se encuentra cancelada.")

        self.__estado = "Cancelada"
        return True

    def procesar(self):
        if self.__estado != "Confirmada":
            raise EstadoReservaError("Primero debe confirmar la reserva.")

        self.__estado = "Procesada"
        return True

    def mostrar_informacion(self):
        return (
            "Reserva: " + str(self.__identificador) +
            "\nCliente: " + self.__cliente.nombre +
            "\nServicio: " + self.__servicio.nombre +
            "\nDuracion: " + str(self.__duracion) +
            "\nCosto: $" + str(round(self.__costo, 2)) +
            "\nEstado: " + self.__estado
        )
