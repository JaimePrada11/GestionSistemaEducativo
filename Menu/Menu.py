from Gestion_Camper.Gestion_candidato import *
import Utilidades.Consulta_Informacion_personal as info
import Gestion_Coordinacion.Estado as Estado 
import Gestion_Trainer.Gestion_Trainer as trainer
import Gestion_Coordinacion.Rutas as Rutas
import Gestion_Camper.Gestion_Camper as camper
import Gestion_Reportes.Reportes as Reportes 
import Gestion_Coordinacion.Horarios as Horarios
import Gestion_Trainer.Trainer_notas as notas

Opc_Roles = ("1. Candidato", "2. Camper", "3. Trainer", "4. Coordinador", "5. Cerrar sesion")

Opc_Candidato =("1. Registarse", "2. Informacion Personal", "3. Ver Estado", "4. Volver al Menu principal")
Opc_Camper =("1. Informacion Personal", "2. Informacion del curso", "3. Estado de Riesgo", "4. Volver al Menu principal")
Opc_Trainer =("1. Ver Datos", "2. Rutas asignadas", "3. Notas", "4. Menu Anterior")
Opc_Coordinador =("1. Modificar estado", "2. Matricula", "3. Reportes", "4. Menu anterior")
Opc_matricula=("1. Registrar trainer", "2. Crear ruta de entrenamiento", "3. Crear grupo", "4. Asignar Ruta/Grupo ", "5. Asignar modulos ", "6. Asignar Salon y horario", "7. Menu Anterior")
opc_asignar = ("1. Camper", "2. Trainer", "3. Menu anterior")
opc_reportes =("1. Campers inscritos", "2. Campers aprobados", "3. Trainers activos", "4. Campers bajo rendimiento", "5. Campers y trainer por ruta", "6. Reporte del modulo", "7. Menu Anterior")
opc_estado = ("1. Cambiar Estado Candidato", "2. Retirar Camper", "3. Expulsar", "4. Menu Anterior")
def menu_coordinador():
    print("********")
    print("Bienvenidao Coordinador")
    while True:
        print("Selecciona ----->")
        for i in Opc_Coordinador:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(Opc_Coordinador):
                return menu_principal()
            elif opc_c == 1:
                menu_Estado()
            elif opc_c == 2:
                menu_matricula()
            elif opc_c == 3:
                menu_reportes()
            else:
                print("Opcion Invalida")
            print("*********")

def menu_matricula():
    print("********")
    while True:
        print("Selecciona ----->")
        for i in Opc_matricula:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(Opc_matricula):
                return
            elif opc_c == 1:
                trainer.registro("Trainer")
            elif opc_c == 2:
                Rutas.Nueva_Ruta_entrenamiento()
            elif opc_c == 3:
                Rutas.Crear_grupo_Ruta()   
            elif opc_c == 4:
                menu_asignar()    
            elif opc_c == 5:
                Rutas.Agregar_modulos_ruta() 
            elif opc_c == 6:
                Horarios.asignar_fecha()                                    
            else:
                print("Opcion Invalida")
            print("*********")

def menu_asignar():
    print("********")
    while True:
        print("Selecciona ----->")
        for i in opc_asignar:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(opc_asignar):
                return menu_matricula()
            elif opc_c == 1:
                camper.Agregar_Ruta_camper()
            elif opc_c == 2:
                trainer.Agregar_Ruta_trainer()              
            else:
                print("Opcion Invalida")
            print("*********")

def menu_reportes():
    while True:
        print("Selecciona ----->")
        for i in opc_reportes:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(Opc_matricula):
                return menu_coordinador()
            elif opc_c == 1:
                Reportes.Candidatos_Inscritos()
            elif opc_c == 2:
                Reportes.Campers_Aprobados()
            elif opc_c == 3:
                Reportes.listar_trainers_activos()   
            elif opc_c == 4:
                Reportes.camper_bajo_rendimiento()   
            elif opc_c == 5:
                Reportes.camper_trainer_misma_ruta() 
            elif opc_c == 6:
                Reportes.reporte_por_modulo()                                  
            else:
                print("Opcion Invalida")
            print("*********")

def menu_candidato():
    print("********")
    print("Bienvenidao Candidato")
    print("********")
    while True:
        print("Selecciona ----->")
        for i in Opc_Candidato:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(Opc_Candidato):
                return
            elif opc_c == 1:
                trainer.registro("Candidato")
            elif opc_c == 2:
                info.ver_informacion("Candidato")
            elif opc_c == 3:
                Ver_Estado()                
            else:
                print("Opcion Invalida")
            print("*********")

def menu_Estado():
    print("********")
    while True:
        print("Selecciona ----->")
        for i in opc_estado:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(Opc_Candidato):
                return menu_coordinador()
            elif opc_c == 1:
                Estado.modificar_estado_candidato()
            elif opc_c == 2:
                Estado.retirar_Camper()
            elif opc_c == 3:
                Estado.expulsar_camper()                
            else:
                print("Opcion Invalida")
            print("*********")

def menu_camper():
    print("********")
    print("Bienvenidao Camper")
    print("********")

    while True:
        print("Selecciona ----->")
        for i in Opc_Camper:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(Opc_Camper):
                return
            elif opc_c == 1:
                info.ver_informacion("Camper")
            elif opc_c == 2:
                Ver_Estado()
            else:
                print("Opcion Invalida")
            print("*********")    

def menu_trainer():
    print("********")
    print("Bienvenidao Trainer")
    print("********")

    while True:
        print("Selecciona ----->")
        for i in Opc_Trainer:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(Opc_Trainer):
                return
            elif opc_c == 1:
                info.ver_informacion("Trainer")
            elif opc_c == 2:
                trainer.Rutas_asignadas()
            elif opc_c==3:
                notas.calificar_camper()
            else:
                print("Opcion Invalida")
            print("*********")  

def menu():
    print("***********")
    cargar_datos()
    print("Selecciona")
    print("***********")

    for i in Opc_Roles:
        print(i)
    try:
        opc = int(input("Ingresa la opcion deseada: "))
        return opc
    except ValueError:
        print("Opcion Invalida")

def menu_principal():
    while True:
        opc = menu()
        if opc ==len(Opc_Roles):    
            print("Saliendo")
            break
        elif opc ==1:
            menu_candidato()
        elif opc==2:
            menu_camper()
        elif opc==3:
            print("")
            menu_trainer()
        elif opc ==4:
            print("")
            menu_coordinador()
        else:
            print("Invalido")

