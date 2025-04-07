from Gestion_Datos.Manejo_datos import cargar_datos, guardar_datos
from Gestion_Datos.Datos import Informacion


""" def Agregar_Ruta_camper():
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
                Informacion["Camper"][cedula]["Grupo"] = grupo_seleccionado
                Informacion["Camper"][cedula]["Estado"] = "Cursando"
            else:
                print("No se asignó ningún grupo al Camper.")
        else:
            print(f"El Camper de cédula {cedula} ya tenía una ruta asignada.")
        guardar_datos()
    else:
        print("El Camper no existe.")
    print("***********")

def Rutas_asignadas():
    cargar_datos()
    cedula = input("Ingresa tu número de cedula: ")

    if cedula in Informacion["Camper"]:
        camper = Informacion["Camper"][cedula]
        print(f"Camper: {camper['Nombre']} {camper['Apellidos']}")
        print("Rutas y grupos asignados:")
        print(f"Ruta: {camper['Ruta']} 'Grupo:' {camper['Grupo']}")
    else:
        print("No se encontró ningún entrenador con esa cedula.")
 """

