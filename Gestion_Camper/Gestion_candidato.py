from Gestion_Datos.Manejo_datos import cargar_datos, guardar_datos
from Gestion_Datos.Datos import Informacion
from Utilidades.Validaciones import validar_cedula, validar_email

import Utilidades.Consulta_Informacion_personal as validar


def Ver_Estado():
    cargar_datos()
    cedula = input("Ingresa la cedula: ")
    if cedula in Informacion["Candidato"] or cedula in Informacion["Camper"] :
        print("Tu estado actual es: ")
        if cedula in Informacion["Candidato"]:
            print(Informacion["Candidato"][cedula]["Estado"])
        else:
            print(Informacion["Camper"][cedula]["Estado"])
    else: 
        print("El aspirante no existe")
