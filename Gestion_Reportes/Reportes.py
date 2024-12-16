from Gestion_Datos.Manejo_datos import cargar_datos, guardar_datos
from Gestion_Coordinacion.Rutas import mostrar_grupo_ruta
from Gestion_Datos.Datos import Informacion

def Candidatos_Inscritos():
    cargar_datos()

    print("\n" + "="*40)
    print("Candidatos Inscritos")
    print("="*40)

    print(f"| {'#':<4} | {'Cédula':<15} | {'Nombre':<25} | {'Estado':<10} |")
    print("="*40)

    inscritos = [cedula for cedula, 
                 candidato in Informacion["Candidato"].items() 
                 if candidato["Estado"] == "Inscrito"]

    for i, cedula in enumerate(inscritos, 1):
        candidato = Informacion["Candidato"][cedula]
        nombre = candidato.get('Nombre', 'N/A')
        estado = candidato.get('Estado', 'N/A')
        print(f"| {i:<4} | {cedula:<15} | {nombre:<25} | {estado:<10} |")

    print("="*40)


def Campers_Aprobados():
    cargar_datos()

    print("\n" + "="*40)
    print("Campers Aprobados en el Examen Inicial")
    print("="*40)

    print(f"| {'#':<4} | {'Cédula':<15} | {'Nombre':<25} |")
    print("="*40)

    aprobados = [cedula for cedula, camper in Informacion["Camper"].items() if camper["Estado"] == "Aprobado"]
    
    for i, cedula in enumerate(aprobados, 1):
        camper = Informacion["Camper"][cedula]
        nombre = camper.get('Nombre', 'N/A')
        apellidos = camper.get('Apellidos', 'N/A')
        print(f"| {i:<4} | {cedula:<15} | {nombre} {apellidos:<25} |")

    print("="*40)



def listar_trainers_activos():
    cargar_datos()

    print("\n" + "="*40)
    print("Trainers Activos")
    print("="*40)

    print(f"| {'#':<4} | {'Cédula':<15} | {'Nombre':<25} |")
    print("="*40)

    activos = [cedula for cedula, trainer in Informacion["Trainer"].items() if trainer["Estado"] == True] 
    
    for i, cedula in enumerate(activos, 1):
        trainer = Informacion["Trainer"][cedula]
        nombre = trainer.get('Nombre', 'N/A')
        apellidos = trainer.get('Apellidos', 'N/A')
        print(f"| {i:<4} | {cedula:<15} | {nombre} {apellidos:<25} |")

    print("="*40)



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
