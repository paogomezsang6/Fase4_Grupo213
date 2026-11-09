
# Importar herramientas para clases abstractas
from abc import ABC, abstractmethod

# Importar la clase Entidad
from entidades import Entidad


# Clase abstracta Servicio que hereda de Entidad
class Servicio(Entidad, ABC):

    def __init__(self, identificador, nombre, tarifa_base):

        super().__init__(identificador, nombre)

        # Atributo protegido con la tarifa del servicio
        self._tarifa_base = tarifa_base

    # Consultar la tarifa base
    @property
    def tarifa_base(self):
        return self._tarifa_base

    # Validar los datos generales del servicio
    def validar(self):

        if not self.identificador:
            raise ValueError("El identificador del servicio es obligatorio.")

        if not self.nombre or not self.nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if isinstance(self.tarifa_base, bool) or not isinstance(self.tarifa_base, (int, float)):
            raise ValueError("La tarifa debe ser un numero.")

        if self.tarifa_base <= 0:
            raise ValueError("La tarifa debe ser mayor que cero.")

        return True

    # Metodo abstracto para calcular el costo
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    # Metodo abstracto para describir el servicio
    @abstractmethod
    def describir(self):
        pass

    # Metodo abstracto para validar parametros
    @abstractmethod
    def validar_parametros(self, **parametros):
        pass

    # Calcular el costo con descuento e impuesto
    def calcular_total(self, duracion, descuento=0, impuesto=0):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool) or not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        subtotal = self.tarifa_base * duracion
        valor_descuento = subtotal * descuento / 100
        subtotal_descuento = subtotal - valor_descuento
        valor_impuesto = subtotal_descuento * impuesto / 100

        return subtotal_descuento + valor_impuesto


# Servicio especializado en reserva de salas
class ReservaSala(Servicio):

    def __init__(self, identificador, nombre, tarifa_base, capacidad):

        super().__init__(identificador, nombre, tarifa_base)

        self.__capacidad = capacidad
        self.validar()

    def validar(self):

        super().validar()

        if isinstance(self.__capacidad, bool) or not isinstance(self.__capacidad, int) or self.__capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero mayor que cero.")

        return True

    def validar_parametros(self, **parametros):

        personas = parametros.get("personas")

        if isinstance(personas, bool) or not isinstance(personas, int) or personas <= 0:
            raise ValueError("Debe indicar una cantidad valida de personas.")

        if personas > self.__capacidad:
            raise ValueError("La sala no tiene capacidad suficiente.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        return self.calcular_total(duracion, descuento, impuesto)

    def describir(self):

        return "Reserva de sala: " + self.nombre


# Servicio especializado en alquiler de equipos
class AlquilerEquipo(Servicio):

    def __init__(self, identificador, nombre, tarifa_base, stock):

        super().__init__(identificador, nombre, tarifa_base)

        self.__stock = stock
        self.validar()

    def validar(self):

        super().validar()

        if isinstance(self.__stock, bool) or not isinstance(self.__stock, int) or self.__stock < 0:
            raise ValueError("El stock debe ser un entero igual o mayor que cero.")

        return True

    def validar_parametros(self, **parametros):

        cantidad = parametros.get("cantidad")

        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad de equipos debe ser mayor que cero.")

        if cantidad > self.__stock:
            raise ValueError("No hay suficientes equipos disponibles.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        return self.calcular_total(duracion, descuento, impuesto)

    def describir(self):

        return "Alquiler de equipo: " + self.nombre


# Servicio especializado en asesorias
class AsesoriaEspecializada(Servicio):

    def __init__(self, identificador, nombre, tarifa_base, especialidad):

        super().__init__(identificador, nombre, tarifa_base)

        self.__especialidad = especialidad
        self.validar()

    def validar(self):

        super().validar()

        if not self.__especialidad or not self.__especialidad.strip():
            raise ValueError("La especialidad es obligatoria.")

        return True

    def validar_parametros(self, **parametros):

        horas = parametros.get("horas")

        if isinstance(horas, bool) or not isinstance(horas, (int, float)) or horas <= 0:
            raise ValueError("Las horas de asesoria deben ser mayores que cero.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        return self.calcular_total(duracion, descuento, impuesto)

    def describir(self):

        return "Asesoria especializada en: " + self.__especialidad
