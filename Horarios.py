from Manejo_datos import cargar_datos, guardar_datos
from Datos import *

from Rutas import mostrar_grupo_ruta
from datetime import datetime, timedelta


salon_horas_disponibles = {salon: Horas.copy() for salon in Salon}


def solicitar_fechas():
    while True:
        fecha = input("Ingresa la fecha en formato YYYY-MM-DD: ")
        try:
            fecha_inicio = datetime.strptime(fecha, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato de fecha inválido. Debe ser YYYY-MM-DD.")

    while True:
        try:
            duracion = int(input("Ingresa la duración en meses: "))
            if duracion <= 0:
                print("La duración debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido para la duración.")
        
    fecha_final = fecha_inicio + timedelta(days=duracion * 30.44)
    print()
    return fecha_inicio.strftime("%Y-%m-%d"), fecha_final.strftime("%Y-%m-%d"), duracion
        


def Horario_Salon():
    cargar_datos()

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
    cargar_datos()

    ruta, grupo = mostrar_grupo_ruta()
    if ruta:
        print("***********")
        print("Selecciona el salón y hora para el grupo:")
        salon_seleccionado, hora_seleccionada = Horario_Salon()
        if grupo:
            if grupo not in Informacion["Rutas"][ruta]:
                Informacion["Rutas"][ruta][grupo] = {}
            Informacion["Rutas"][ruta][grupo]["Salon"] = salon_seleccionado
            Informacion["Rutas"][ruta][grupo]["Hora"] = hora_seleccionada
            guardar_datos()
    else:
        print("No se seleccionó ninguna ruta.")

def asignar_fecha():
    cargar_datos()

    ruta, grupo = mostrar_grupo_ruta()
    if ruta:
        fecha_inicio, fecha_final, duracion = solicitar_fechas()
        if grupo:
            if grupo not in Informacion["Rutas"][ruta]:
                Informacion["Rutas"][ruta][grupo] = {}
            Informacion["Rutas"][ruta][grupo]["Fecha de Inicio"] = fecha_inicio
            Informacion["Rutas"][ruta][grupo]["Fecha de Fin"] = fecha_final
            Informacion["Rutas"][ruta][grupo]["Duracion"] = duracion
            guardar_datos()
        else:
            print("No se seleccionó un grupo válido.")
    else:
        print("No se seleccionó una ruta válida.")


