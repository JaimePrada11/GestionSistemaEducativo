from Cargar_Guardar_datos import *
import Consulta_Informacion_personal as validar

def Registro_candidato():
    cargar_datos()
    usuario = {}

    print("Informacion basica del candidato")
    print("***********")

    cedula = input("Ingresa la cedula: ")
    if cedula.isdigit():
        if not validar.validar_cedula(cedula, "Candidato"):
            if Informacion["Candidato"].get(cedula, None) is None:
                usuario["Nombre"] = input("Ingresa el nombre: ")
                usuario["Apellidos"] = input("Ingresa el apellido: ")
                usuario["Direccion"] = input("Ingresa la direccion: ")
                usuario["Acudiente"] = input("Ingresa el nombre de acudiente: ")
                while True:
                    telefono_fijo = input("Ingresa telefono fijo: ")
                    if telefono_fijo.isdigit():
                        usuario["Telefono"] = {"Fijo": telefono_fijo}
                        break
                    else:
                        print("El teléfono fijo debe contener solo números.")
                
                while True:
                    telefono_movil = input("Ingresa el celular: ")
                    if telefono_movil.isdigit():
                        usuario["Telefono"]["Movil"] = telefono_movil
                        break
                    else:
                        print("El teléfono móvil debe contener solo números.")
                
                usuario["Estado"] = "Inscrito"

                Informacion["Candidato"][cedula] = usuario
                guardar_datos()

                print("Informacion Guardada")
                print("***********")
            else:
                print("La cédula ya existe.")
        else:
            print("La cédula ingresada ya está en uso.")
    else:
        print("La cédula debe contener solo números.")


def Ver_Estado():
    cargar_datos()
    cedula = input("Ingresa la cedula: ")
    if cedula in Informacion["Candidato"] or cedula in Informacion["Camper"] :
        print("Tu estado actual es: ")
        if cedula in Informacion["Candidato"]:
            print(Informacion["Candidato"][cedula]["Estado"])
        else:
            print(Informacion["Camper"][cedula]["Estado"])

