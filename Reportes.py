from Manejo_datos import cargar_datos, guardar_datos
from Rutas import mostrar_grupo_ruta
from Datos import Informacion

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


def Camper_Trainer_Misma_Ruta_Grupo():
    print("***********")
    cargar_datos()

    ruta, grupo = mostrar_grupo_ruta()

    trainers_misma_ruta_grupo = []
    camper_misma_ruta_grupo = []

    for cedula_trainer, trainer_info in Informacion["Trainer"].items():
        ruta_trainer = trainer_info["Ruta"]
        grupo_trainer = trainer_info["Grupo"]

        if ruta_trainer == ruta and grupo_trainer == grupo:
            trainers_misma_ruta_grupo.append(cedula_trainer)

    for cedula_camper, camper_info in Informacion["Camper"].items():
        if (camper_info["Ruta"] == ruta) and (camper_info["Grupo"] == grupo):
            camper_misma_ruta_grupo.append(cedula_camper)

    if trainers_misma_ruta_grupo:
        print("Trainers y Camper en la misma ruta y grupo:")
        for trainer, camper in zip(trainers_misma_ruta_grupo, camper_misma_ruta_grupo):
            print(f"Trainer: {trainer}, Camper: {camper}")
    else:
        print("No se encontraron Trainer y Camper en la misma ruta y grupo.")

    print("***********")

Candidatos_Inscritos()
Campers_Aprobados()
listar_trainers_activos()