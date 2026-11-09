
# Importar la clase abstracta Entidad
from entidades import Entidad


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        # Inicializar los atributos de la clase padre
        super().__init__(identificacion, nombre)

        # Atributos privados del cliente
        self.__correo = correo
        self.__telefono = telefono

        # Validar los datos del cliente
        self.validar()

    # Consultar el correo electronico
    @property
    def correo(self):
        return self.__correo

    # Consultar el telefono
    @property
    def telefono(self):
        return self.__telefono

    # Validar la informacion del cliente
    def validar(self):

        if not self.identificador or not str(self.identificador).strip():
            raise ValueError("La identificacion es obligatoria.")

        if not self.nombre or not self.nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio.")

        if not self.correo or "@" not in self.correo:
            raise ValueError("El correo electronico no es valido.")

        if not self.telefono or not str(self.telefono).isdigit():
            raise ValueError("El telefono debe contener solamente numeros.")

        if len(str(self.telefono)) < 7:
            raise ValueError("El telefono debe tener minimo 7 digitos.")

        return True

    # Mostrar la informacion del cliente
    def mostrar_informacion(self):

        return (
            "Identificacion: " + str(self.identificador) +
            "\nNombre: " + self.nombre +
            "\nCorreo: " + self.correo +
            "\nTelefono: " + str(self.telefono)
        )
