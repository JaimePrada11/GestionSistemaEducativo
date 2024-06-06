from Manejo_datos import cargar_datos, guardar_datos
from Datos import Informacion
from Validaciones import validar_cedula, validar_email

import Consulta_Informacion_personal as validar

def Registro_candidato():
    cargar_datos()
    Aspirante = {}

    print("***********")
    print("Informacion basica del candidato")
    print("***********")

    while True:
        cedula = input("Ingresa la cedula: ")
        if cedula.lower() == 'cancelar':
            print("Registro cancelado.")
            return        
        if cedula.isdigit():  
            if not validar_cedula(cedula):  
                break
            else:
                print("La cédula ya existe.")
        else:
            print("Cédula no válida. Debe contener solo números.")

    Aspirante["Nombre"] = input("Ingresa el nombre: ")
    Aspirante["Apellidos"] = input("Ingresa el apellido: ")
    Aspirante["Direccion"] = input("Ingresa la dirección: ")
    
    while True:
        email = input("Ingresa el email: ")
        if validar_email(email):
            Aspirante["Email"] = email
            break
        else:
            print("Email no válido. Por favor, ingresa un email correcto.")
    
    Aspirante["Acudiente"] = input("Ingresa el nombre de acudiente: ")

    while True:
        telefono_fijo = input("Ingresa telefono fijo: ")
        if telefono_fijo.isdigit():
            Aspirante["Telefono"] = {"Fijo": telefono_fijo}
            break
        else:
            print("El teléfono fijo debe contener solo números.")
    
    while True:
        telefono_movil = input("Ingresa el celular: ")
        if telefono_movil.isdigit():
            Aspirante["Telefono"]["Movil"] = telefono_movil
            break
        else:
            print("El teléfono móvil debe contener solo números.")
    
    Aspirante["Estado"] = "Inscrito"
    Informacion["Candidato"][cedula] = Aspirante
    guardar_datos()

    print("Informacion Guardada")
    print("***********")


def Ver_Estado():
    cargar_datos()
    cedula = input("Ingresa la cedula: ")
    if cedula in Informacion["Candidato"] or cedula in Informacion["Camper"] :
        print("Tu estado actual es: ")
        if cedula in Informacion["Candidato"]:
            print(Informacion["Candidato"][cedula]["Estado"])
        else:
            print(Informacion["Camper"][cedula]["Estado"])
    else: 
        print("El aspirante no existe")
