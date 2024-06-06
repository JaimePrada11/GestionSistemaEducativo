from Manejo_datos import guardar_datos, cargar_datos
from Datos import Informacion, modulos_skills
from Rutas import mostrar_grupo_ruta

notas_trabajos = {}
notas = {}

notas_trabajos = {}
notas = {}

def Trabajos_Clase():
    global notas_trabajos
    print("Notas de trabajo en clase")
    try:
        Cant_Notas = int(input("Ingresa la cantidad de notas: "))
    except ValueError:
        print("Error de Dato: Por favor ingrese un número válido.")
        return 0

    Nota_parcial = 0
    for i in range(Cant_Notas):
        nombre = input("Ingresa el nombre del trabajo: ")
        try:
            Nota = int(input(f"Ingresa el valor de la nota para {nombre}: "))
            if not (0 <= Nota <= 100):
                print("La nota debe estar entre 0 y 100.")
                continue
        except ValueError:
            print("Error de Dato: Por favor ingrese un número válido.")
            continue

        try:
            porcentaje = int(input(f"Ingresa el porcentaje de {nombre}: "))
            if not (0 <= porcentaje <= 100):
                print("El porcentaje debe estar entre 0 y 100.")
                continue
        except ValueError:
            print("Error de Dato: Por favor ingrese un número válido.")
            continue

        notas_trabajos[nombre] = {"Nota": Nota, "Porcentaje": porcentaje}
        nota_porcentual = Nota * (porcentaje / 100)
        Nota_parcial += nota_porcentual

    return Nota_parcial

def Ingresar_Nota(cedula, modulo, skill):
    global notas
    print(f"***** Calificando {skill} en el módulo {modulo} *****")
    try:
        nota_teoria = int(input("Ingresa nota teorica: "))
        nota_practica = int(input("Ingresa nota practica: "))
        if not (0 <= nota_teoria <= 100) or not (0 <= nota_practica <= 100):
            print("Las notas deben estar entre 0 y 100.")
            return False
    except ValueError:
        print("Error de Dato: Por favor ingrese un número válido para las notas.")
        return False

    nota_trabajos = Trabajos_Clase()

    final = nota_teoria * 0.3 + nota_practica * 0.6 + nota_trabajos * 0.1

    if "Notas" not in Informacion["Camper"][cedula]:
        Informacion["Camper"][cedula]["Notas"] = {}
    if modulo not in Informacion["Camper"][cedula]["Notas"]:
        Informacion["Camper"][cedula]["Notas"][modulo] = {}

    Informacion["Camper"][cedula]["Notas"][modulo][skill] = {
        "Nota Teorica": nota_teoria,
        "Nota Practica": nota_practica,
        "Nota Trabajos": nota_trabajos,
        "Nota Final": final
    }

    # Marcar riesgo y contar tecnologías reprobadas
    if final < 60:
        if "Reprobadas" not in Informacion["Camper"][cedula]:
            Informacion["Camper"][cedula]["Reprobadas"] = 0
        Informacion["Camper"][cedula]["Reprobadas"] += 1
        Informacion["Camper"][cedula]["Riesgo"] = True

    return True

def calificar_camper():
    cargar_datos()
    print("***********")
    print("Módulo de calificaciones")
    print("***********")

    cedula = input("Ingresa la cédula del camper: ")
    if cedula in Informacion["Camper"]:
        if Informacion["Camper"][cedula]["Estado"] == "Cursando":
            ruta_camper = Informacion["Camper"][cedula]["Ruta"]
            grupo_camper = Informacion["Camper"][cedula]["Grupo"]
            if ruta_camper in Informacion["Rutas"] and grupo_camper in Informacion["Rutas"][ruta_camper]:
                modulos_skills = Informacion["Rutas"][ruta_camper][grupo_camper]["Módulos"]
                seguir_progreso_calificacion(cedula, modulos_skills)
                guardar_datos()
    else:
        print("Cédula de camper no encontrada o no está cursando.")

def seguir_progreso_calificacion(cedula, modulos_skills):
    for nombre_modulo, tecnologias in modulos_skills.items():
        print(f"Modulo: {nombre_modulo}")
        for tecnologia in tecnologias:
            print(f"- {tecnologia}")
            if not Ingresar_Nota(cedula, nombre_modulo, tecnologia):
                return
            if input("¿Desea calificar la siguiente tecnología? (s/n): ").lower() != 's':
                return
        if input("¿Desea calificar el siguiente módulo? (s/n): ").lower() != 's':
            return
