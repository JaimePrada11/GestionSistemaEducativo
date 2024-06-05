import Cargar_Guardar_datos as Datos

def validar_cedula(cedula, tipo_registro):
    if tipo_registro in Datos.Informacion:
        return cedula in Datos.Informacion[tipo_registro]
    else:
        raise ValueError("Tipo de registro no válido")

def ver_informacion(rol):
    print("*****")
    Datos.cargar_datos()
    cedula = input("Ingresa la cedula")
    if cedula in Datos.Informacion[rol]:
        participante = Datos.Informacion[rol][cedula]
        print(f"Información general:")
        print(f"Cedula: {cedula}")
        print(f"Nombre: {participante['Nombre']}")
        print(f"Apellidos: {participante['Apellidos']}")
        print(f"Rol: {rol}")
    else:
        print("Participante no encontrado.")