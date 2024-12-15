from Gestion_Datos.Manejo_datos import cargar_datos, guardar_datos
from Gestion_Datos.Datos import Informacion
from Utilidades.Validaciones import validar_cedula, validar_email

import Utilidades.Consulta_Informacion_personal as validar


def Ver_Estado():

    cargar_datos()
    cedula = input("🆔 Ingresa la cédula: ")
    print("\n" + "="*40)

    if cedula in Informacion.get("Candidato") or cedula in Informacion.get("Camper"):
        print("\n🌟 Información del Estado 🌟")
        print("="*40 + "\n")
        print(f"| {'Campo':<20} | {'Información':<15} |")
        print("|" + "="*22 + "|" + "="*18 + "|")

        if cedula in Informacion["Candidato"]:
            estado = Informacion["Candidato"][cedula]["Estado"]
            rol = "Candidato"
        else:
            estado = Informacion["Camper"][cedula]["Estado"]
            rol = "Camper"

        print(f"| {'Cédula':<20} | {cedula:<15} |")
        print(f"| {'Rol':<20} | {rol:<15} |")
        print(f"| {'Estado':<20} | {estado:<15} |")
        print("="*40 + "\n")
    else:
        print("\n❌ ¡Error! No existe en el sistema. ❌")
        print("="*40 + "\n")
