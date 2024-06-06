from Manejo_datos import cargar_datos, guardar_datos
from Datos import Informacion

from Rutas import  mostrar_grupo_ruta

def Agregar_Ruta_camper():
    print("***********")
    cargar_datos()

    contador_camper = sum(1 for camper_info in Informacion["Camper"].values() if camper_info["Ruta"] == "No asignada")
    if contador_camper >= 33:
        print("Ya se han asignado el máximo de 33 Camper a esta ruta. No se pueden asignar más.")
        return
    cedula = input("Ingresa la cédula del Camper: ")
    
    if cedula  in Informacion["Camper"]:       
        if Informacion["Camper"][cedula]["Ruta"] == "No asignada":
            Ruta, grupo_seleccionado = mostrar_grupo_ruta()
            if grupo_seleccionado:
                Informacion["Camper"][cedula]["Ruta"] = Ruta
                Informacion["Camper"][cedula]["Grupo"] = grupo_seleccionado
                Informacion["Camper"][cedula]["Estado"] = "Cursando"
                print(f"El Camper de cédula {cedula} se asignó al grupo {grupo_seleccionado} en la ruta {Ruta}.")
            else:
                print("No se asignó ningún grupo al Camper.")
        else:
            print(f"El Camper de cédula {cedula} ya tenía una ruta asignada.")
        guardar_datos()
    else:
        print("El Camper no existe.")
    print("***********")

Agregar_Ruta_camper()