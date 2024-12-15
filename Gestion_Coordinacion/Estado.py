from Gestion_Datos.Manejo_datos import cargar_datos, guardar_datos
from Gestion_Datos.Datos import Informacion

def modificar_Estado_candidato():
    cargar_datos()

    print("***********")
    cedula = input("Ingresa cedula de candidato: ")
    print("***********")

    if cedula not in Informacion["Candidato"]:
        print("El candidato no existe ")
    else:
        try:
            nota_teorica = int(input("Ingresa la nota teorica: "))
            nota_practica = int(input("Ingresa la nota practica: "))
            if not (0 <= nota_teorica <= 100) or not (0 <= nota_practica <= 100):
                print("La nota maxima es 100.")
                
        except ValueError:
            print("Error de Dato: Por favor ingrese un número válido")
            return
        else:
            promedio = (nota_teorica + nota_practica) / 2
            if promedio >= 60:
                Informacion["Candidato"][cedula]["Estado"] = "Aprobado"
                Informacion["Candidato"][cedula]["Ruta"] = "No asignada"
                Informacion["Candidato"][cedula]["Riesgo"] = "Nulo"
                    
                Informacion["Camper"][cedula] = Informacion["Candidato"].pop(cedula)
            else:
                Informacion["Candidato"][cedula]["Estado"] = "No Aprobado"
            
            guardar_datos()
            print("***********")

def actualizar_estado_camper():
    print("***********")
    cargar_datos()
    cedula = input("Ingresa cedula de candidato: ")
    if cedula not in Informacion["Camper"]:
        print("El candidato no existe ")
    else:
        if Informacion["Camper"][cedula]["Ruta"] != "No asignada":
            Informacion["Camper"][cedula]["Estado"] = "cursando"
            guardar_datos()
            print("***********")

def expulsar_camper():
    print("***********")
    cedula = input("Ingresa cedula de candidato: ")
    print("***********")

    if cedula not in Informacion["Camper"]:
        print("El camper no existe ")
        if Informacion["Camper"][cedula]["Estado"] != "cursando":
            Informacion["Camper"][cedula]["Estado"] = "Expulsado"
            guardar_datos()
            print("***********")

def retirar_Camper():
    print("***********")
    cedula = input("Ingresa cedula de candidato: ")
    print("***********")

    if cedula not in Informacion["Camper"]:
        print("El camper no existe ")
        if Informacion["Camper"][cedula]["Estado"] != "cursando":
            Informacion["Camper"][cedula]["Estado"] = "Retirado"
            guardar_datos()
            print("***********")



