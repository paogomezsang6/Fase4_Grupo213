
# Importar herramientas para crear clases abstractas
from abc import ABC, abstractmethod


# Clase abstracta que representa las entidades del sistema
class Entidad(ABC):

    def __init__(self, identificador, nombre):
        # Atributos privados de la entidad
        self.__identificador = identificador
        self.__nombre = nombre

    # Metodo para consultar el identificador
    @property
    def identificador(self):
        return self.__identificador

    # Metodo para consultar el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Metodo abstracto que deben implementar las clases hijas
    @abstractmethod
    def validar(self):
        pass
