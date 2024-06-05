import Cargar_Guardar_datos as datos
from Rutas import rutas, mostrar_grupo_ruta
from datetime import datetime, timedelta


Salon = ("Sputnik", "Apollo", "Artemis")

Horas = ["6am-10am", "10am-2pm", "2pm-6pm", "6pm-10pm"]

salon_horas_disponibles = {salon: Horas.copy() for salon in Salon}


def solicitar_fechas():
    while True:
        inicio = input("Ingresa la fecha de inicio (YYYY-MM-DD): ")
        fin = input("Ingresa la fecha de fin (YYYY-MM-DD): ")

        try:
            inicio = datetime.datetime.strptime(inicio, "%Y-%m-%d")
            fin = datetime.datetime.strptime(fin, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto. Inténtalo de nuevo.")
            continue
        
        if inicio >= fin:
            print("La fecha de inicio debe ser anterior a la fecha de fin. Inténtalo de nuevo.")
            continue
        
        return inicio, fin

def Horario_Salon():
    datos.cargar_datos()

    while True:
        print("***********")
        print("Selecciona el salón")

        for i, salon in enumerate(Salon, 1):
            print(f"{i}. {salon}")

        try:
            opc_salon = int(input("Ingresa la opción: "))
            if opc_salon < 1 or opc_salon > len(Salon):
                print("Opción inválida. Selecciona un salón válido.")
                continue
        except ValueError:
            print("Entrada inválida. Ingresa un número.")
            continue

        salon_seleccionado = Salon[opc_salon - 1]

        print(f"Selecciona el horario para el salón {salon_seleccionado}")
        horas_disponibles = salon_horas_disponibles[salon_seleccionado]

        for i, hora in enumerate(horas_disponibles, 1):
            print(f"{i}. {hora}")

        try:
            opc_horas = int(input("Ingresa la opción: "))
            if opc_horas < 1 or opc_horas > len(horas_disponibles):
                print("Opción inválida. Selecciona un horario válido.")
                continue
        except ValueError:
            print("Entrada inválida. Ingresa un número.")
            continue

        hora_seleccionada = horas_disponibles.pop(opc_horas - 1)

        print(f"Horarios disponibles después de la selección para el salón {salon_seleccionado}:")
        print(horas_disponibles)
        return salon_seleccionado, hora_seleccionada

def asignar_hora_salon():
    datos.cargar_datos()

    ruta, grupo = mostrar_grupo_ruta()
    if ruta:
        print("***********")
        print("Selecciona el salón y hora para el grupo:")
        salon_seleccionado, hora_seleccionada = Horario_Salon()
        if grupo:
            if grupo not in datos.Informacion["Rutas"][ruta]:
                datos.Informacion["Rutas"][ruta][grupo] = {}
            datos.Informacion["Rutas"][ruta][grupo]["Salon"] = salon_seleccionado
            datos.Informacion["Rutas"][ruta][grupo]["Hora"] = hora_seleccionada
            datos.guardar_datos()
        else:
            print("El nombre del grupo no puede estar vacío.")
    else:
        print("No se seleccionó ninguna ruta.")

