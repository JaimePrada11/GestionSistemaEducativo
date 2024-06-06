from Manejo_datos import guardar_datos, cargar_datos
from Datos import Informacion, modulos_skills
from Rutas import mostrar_grupo_ruta

notas_trabajos = {}
notas = {}

def Trabajos_Clase():
    global notas_trabajos
    print("Notas de trabajo en clase")
    try:
        Cant_Notas = int(input("Ingresa la cantidad de notas: "))
    except ValueError:
        print("Error de Dato: Por favor ingrese un número válido.")

    Nota_parcial = 0

    if Cant_Notas > 1:
        for i in range(Cant_Notas):
            nombre = input("Ingresa el nombre del trabajo: ")
            
            try:
                Nota = int(input(f"Ingresa el valor de la nota para {nombre}: "))
                if not (0 <= Nota <= 100):
                    print("La nota debe estar entre 0 y 100.")

            except ValueError:
                print("Error de Dato: Por favor ingrese un número válido.")


            try:
                porcentaje = int(input(f"Ingresa el porcentaje de {nombre}: "))
                if not (0 <= porcentaje <= 100):
                    print("El porcentaje debe estar entre 0 y 100.")
            except ValueError:
                print("Error de Dato: Por favor ingrese un número válido.")

            notas_trabajos[nombre] = {"Nota": Nota, "Porcentaje": porcentaje}
            nota_porcentual = Nota * (porcentaje / 100)
            Nota_parcial += nota_porcentual

        return Nota_parcial
    else:
        nombre = input("Ingresa el nombre del trabajo: ")
        try:
            Nota = int(input(f"Ingresa el valor de la nota de {nombre} : "))
            if not (0 <= Nota <= 100):
                print("La nota debe estar entre 0 y 100.")
                return
        except ValueError:
            print("Error de Dato: Por favor ingrese un número válido.")
            return

        notas_trabajos[nombre] = {"Nota": Nota}
        return Nota

def Ingresar_Nota(skill):
    global notas
    print("*****")
    try:
        nota_teoria = int(input("Ingresa nota teorica: "))
        nota_practica = int(input("Ingresa nota practica: "))
        if not (0 <= nota_teoria <= 100) or not (0 <= nota_practica <= 100):
            print("Las notas deben estar entre 0 y 100.")
            return
    except ValueError:
        print("Error de Dato: Por favor ingrese un número válido para las notas.")
        return
    nota_trabajos = Trabajos_Clase()

    final = nota_teoria*.3 + nota_practica*0.6 + nota_trabajos*0.1
    notas["Nota Teorica"] = nota_teoria
    notas["Nota Practica"] = nota_practica
    notas["Nota Trabajos"] = notas_trabajos
    notas["Nota Final"] = final

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
                modulo_camper = Informacion["Rutas"][ruta_camper][grupo_camper]["Módulos"]
                for modulo, tecnologias in modulo_camper.items():
                    print(f"Modulo: {modulo}")
                    for skill in tecnologias:
                        print(f"- {skill}") 
                        if not Ingresar_Nota(skill):
                            return
    else:
        print("Cédula de camper no encontrada o no está cursando.")


calificar_camper()