
# Importar los servicios
from servicios import ReservaSala
from servicios import AlquilerEquipo
from servicios import AsesoriaEspecializada

# Crear una sala
sala = ReservaSala("S01", "Sala de reuniones", 50000, 20)

# Crear un equipo
equipo = AlquilerEquipo("E01", "Video Beam", 30000, 5)

# Crear una asesoria
asesoria = AsesoriaEspecializada(
    "A01", "Asesoria tecnica", 80000, "Programacion"
)

# Mostrar los servicios y sus costos
print("SERVICIOS DISPONIBLES")
print("------------------------------")

print(sala.describir())
print("Costo:", sala.calcular_costo(2))

print("------------------------------")

print(equipo.describir())
print("Costo:", equipo.calcular_costo(3, 10))

print("------------------------------")

print(asesoria.describir())
print("Costo:", asesoria.calcular_costo(2, 0, 19))

# Validar los parametros de los servicios
print("------------------------------")
print("Validacion de servicios:")

print(sala.validar_parametros(personas=10))
print(equipo.validar_parametros(cantidad=2))
print(asesoria.validar_parametros(horas=2))
