import Cargar_Guardar_datos as datos

def modificar_Estado_candidato():
    print("***********")
    datos.cargar_datos()

    cedula = input("Ingresa cedula de candidato: ")
    if cedula not in datos.Informacion["Candidato"]:
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
                datos.Informacion["Candidato"][cedula]["Estado"] = "Aprobado"
                datos.Informacion["Candidato"][cedula]["Ruta"] = "No asignada"
                datos.Informacion["Candidato"][cedula]["Riesgo"] = "Nulo"
                    
                datos.Informacion["Camper"][cedula] = datos.Informacion["Candidato"].pop(cedula)
            else:
                datos.Informacion["Candidato"][cedula]["Estado"] = "No Aprobado"
            
            datos.guardar_datos()
            print("***********")

def actualizar_estado_camper():
    print("***********")
    datos.cargar_datos()
    cedula = input("Ingresa cedula de candidato: ")
    if cedula not in datos.Informacion["Camper"]:
        print("El candidato no existe ")
    else:
        if datos.Informacion["Camper"][cedula]["Ruta"] != "No asignada":
            datos.Informacion["Camper"][cedula]["Estado"] = "cursando"
            datos.guardar_datos()
            print("***********")
