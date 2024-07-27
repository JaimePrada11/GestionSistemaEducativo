from Utilidades.Manejo_datos import cargar_datos, guardar_datos
from Coordinacion.Rutas import mostrar_grupo_ruta
from Utilidades.Datos import Informacion

def Candidatos_Inscritos():
    cargar_datos()
    print("*** Campers Inscritos ***")
    for cedula, candidato in Informacion["Candidato"].items():
        if candidato["Estado"] == "Inscrito":
            print("----")


def Campers_Aprobados():
    print("*** Campers Aprobados en el Examen Inicial ***")
    for cedula, camper in Informacion["Camper"].items():
            if camper["Estado"] == "Aprobado":
                print(f"Cédula: {cedula}, Nombre: {camper['Nombre']} {camper['Apellidos']}")


def listar_trainers_activos():
    print("*** Trainers Activos ***")
    for cedula, trainer in Informacion["Trainer"].items():
        print(f"Cédula: {cedula}, Nombre: {trainer['Nombre']} {trainer['Apellidos']}")



def camper_trainer_misma_ruta():
    ruta_grupo = mostrar_grupo_ruta()
    if ruta_grupo:
        ruta, grupo = ruta_grupo
        print("*** Trainers  ***")
        for cedula, trainer in Informacion["Trainer"].items():
            if trainer["Ruta"] == ruta and trainer["Grupo"] == grupo:
                print(f"Nombre: {trainer['Nombre']} {trainer['Apellidos']} / Cedula: {cedula}, ")

        print("*** Trainers  ***")
        for cedula, camper in Informacion["Camper"].items():
            if camper["Ruta"] == ruta and camper["Grupo"] == grupo:
                print(f"Nombre: {camper['Nombre']} {camper['Apellidos']} / Cedula: {cedula}, ")

def camper_bajo_rendimiento():
    for cedula, camper in Informacion["Camper"].items():
        if "Notas" in camper and any(modulo.get("Nota Final", 0) < 60 for modulo in camper["Notas"].values()):
            print(f"Cédula: {cedula}, Nombre: {camper['Nombre']} {camper['Apellidos']}")


def reporte_por_modulo():
    modulos = set()
    for camper in Informacion["Camper"].values():
        if "Notas" in camper:
            modulos.update(camper["Notas"].keys())

    for modulo in modulos:
        print(f"Reporte para el módulo '{modulo}':")
        for cedula, camper in Informacion["Camper"].items():
            if "Notas" in camper and modulo in camper["Notas"]:
                notas_modulo = camper["Notas"][modulo]
                for tecnologia, notas_tecnologia in notas_modulo.items():
                    if tecnologia != "Nota Final":
                        nota_final = notas_tecnologia.get("Nota Final", "Nota Final no encontrada")
                        print(f"Cédula: {cedula}, Nombre: {camper['Nombre']} {camper['Apellidos']}, Tecnología: {tecnologia}, Nota Final: {nota_final}")
        print("\n")
