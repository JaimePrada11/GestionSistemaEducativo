from Gestion_Datos.Datos import *
from Gestion_Datos.Manejo_datos import *
import Utilidades.Validaciones as validar
from Utilidades.Consulta_Informacion_personal import *
from Gestion_Coordinacion.Rutas import mostrar_grupo_ruta


def Agregar_Ruta_trainer():
    print("***********")
    cargar_datos()

    cedula = input("Ingresa la cédula del Trainer: ")
    
    if cedula  in Informacion["Trainer"]:       
        if Informacion["Trainer"][cedula]["Ruta"] == "No asignado":
            Ruta, grupo_seleccionado = mostrar_grupo_ruta()
            if grupo_seleccionado:
                Informacion["Trainer"][cedula]["Ruta"] = Ruta
                Informacion["Trainer"][cedula]["Grupo"] = grupo_seleccionado
                print(f"El Trainer de cédula {cedula} se asignó al grupo {grupo_seleccionado} en la ruta {Ruta}.")
            else:
                print("No se asignó ningún grupo al Camper.")
        else:
            print(f"El Trainer de cédula {cedula} ya tenía una ruta asignada.")
        guardar_datos()
    else:
        print("El Trainer no existe.")
    print("***********")

def Rutas_asignadas():
    cargar_datos()
    cedula = input("Ingresa tu número de cedula: ")

    if cedula in Informacion["Trainer"]:
        trainer = Informacion["Trainer"][cedula]
        print(f"Entrenador: {trainer['Nombre']} {trainer['Apellidos']}")
        print("Rutas y grupos asignados:")
        print(f"Ruta: {trainer['Ruta']} 'Grupo:' {trainer['Grupo']}")
    else:
        print("No se encontró ningún entrenador con esa cedula.")
