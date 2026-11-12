from clientes import Cliente
from servicios import ReservaSala
from reservas import Reserva

# Crear un cliente
cliente1 = Cliente(
    "123456789",
    "Carlos Perez",
    "carlos@gmail.com",
    "3001234567"
)

# Crear un servicio
sala = ReservaSala(
    "S01",
    "Sala de reuniones",
    50000,
    20
)

# Crear una reserva
reserva1 = Reserva(
    "R001",
    cliente1,
    sala,
    2,
    parametros={"personas": 10}
)

print("SISTEMA DE RESERVAS")
print("--------------------------")
print(reserva1.mostrar_informacion())

# Confirmar reserva
reserva1.confirmar()
print("\nEstado despues de confirmar:", reserva1.estado)

# Procesar reserva
reserva1.procesar()
print("Estado despues de procesar:", reserva1.estado)
