from Manejo_datos import cargar_datos, guardar_datos
from Datos import Informacion

def ver_informacion(rol):
    print("********")
    cargar_datos()
    cedula = input("Ingresa la cedula")
    print("********")
    if cedula in Informacion[rol]:
        participante = Informacion[rol][cedula]
        print(f"Información general:")
        print("********")
        print(f"Cedula: {cedula}")
        print(f"Nombre: {participante['Nombre']}")
        print(f"Apellidos: {participante['Apellidos']}")
        print(f"Email: {participante['Email']}")
        print(f"Telefono Movil: {participante['Telefono']['Movil'] }")
        print(f"Telefono Fijo: {participante['Telefono']['Fijo'] }")
        print(f"Rol: {rol}")
        print("********")

    else:
        print("Participante no encontrado.")
        print("********")

