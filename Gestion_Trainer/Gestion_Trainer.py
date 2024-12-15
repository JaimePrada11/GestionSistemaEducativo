import Gestion_Datos.Manejo_datos as Datos
import Utilidades.Validaciones as validar
from Gestion_Coordinacion.Rutas import mostrar_grupo_ruta

def Registro_trainer():

    Datos.cargar_datos()
    trainer = {}
    print("***********")
    print("Informacion basica del Trainer")
    print("***********")
    cedula = input("Ingresa la cedula: ")
    if cedula.isdigit():
        if not validar.validar_cedula(cedula):
            if Datos.Informacion["Trainer"].get(cedula, None) is None:
                trainer["Nombre"] = input("Ingresa el nombre: ")
                trainer["Apellidos"] = input("Ingresa el apellido: ")
                trainer["Direccion"] = input("Ingresa la direccion: ")
                while True:
                    telefono_fijo = input("Ingresa telefono fijo: ")
                    if telefono_fijo.isdigit():
                        trainer["Telefono"] = {"Fijo": telefono_fijo}
                        break
                    else:
                        print("El teléfono fijo debe contener solo números.")
                        
                while True:
                        telefono_movil = input("Ingresa el celular: ")
                        if telefono_movil.isdigit():
                            trainer["Telefono"]["Movil"] = telefono_movil
                            break
                        else:
                            print("El teléfono móvil debe contener solo números.")
                trainer["Ruta"] = "No asignado"
                trainer["Grupo"] = "No asignado"
                Datos.Informacion["Trainer"][cedula] = trainer
                Datos.guardar_datos()

                print("Informacion Guardada")
                print("***********")
            else:
                print("La cedula ya existe")
        else:
            print("La cédula ingresada ya está en uso.")
    else:
        print("La cédula debe contener solo números.")

def Agregar_Ruta_trainer():
    print("***********")
    Datos.cargar_datos()

    cedula = input("Ingresa la cédula del Trainer: ")
    
    if cedula  in Datos.Informacion["Trainer"]:       
        if Datos.Informacion["Trainer"][cedula]["Ruta"] == "No asignado":
            Ruta, grupo_seleccionado = mostrar_grupo_ruta()
            if grupo_seleccionado:
                Datos.Informacion["Trainer"][cedula]["Ruta"] = Ruta
                Datos.Informacion["Trainer"][cedula]["Grupo"] = grupo_seleccionado
                print(f"El Trainer de cédula {cedula} se asignó al grupo {grupo_seleccionado} en la ruta {Ruta}.")
            else:
                print("No se asignó ningún grupo al Camper.")
        else:
            print(f"El Trainer de cédula {cedula} ya tenía una ruta asignada.")
        Datos.guardar_datos()
    else:
        print("El Trainer no existe.")
    print("***********")

def Rutas_asignadas():
    Datos.cargar_datos()
    cedula = input("Ingresa tu número de cedula: ")

    if cedula in Datos.Informacion["Trainer"]:
        trainer = Datos.Informacion["Trainer"][cedula]
        print(f"Entrenador: {trainer['Nombre']} {trainer['Apellidos']}")
        print("Rutas y grupos asignados:")
        print(f"Ruta: {trainer['Ruta']} 'Grupo:' {trainer['Grupo']}")
    else:
        print("No se encontró ningún entrenador con esa cedula.")
