from Gestion_Datos.Manejo_datos import cargar_datos, guardar_datos
from Gestion_Datos.Datos import Informacion

def modificar_estado_candidato():

    cargar_datos()

    print("\n" + "="*40)
    cedula = input("🆔 Ingresa la cédula del candidato: ")
    print("\n" + "="*40)

    if cedula not in Informacion.get("Candidato", {}):
        print("❌ El candidato no existe en el sistema.")
        return

    try:
        nota_teorica = float(input("📚 Ingresa la nota teórica (0-100): "))
        nota_practica = float(input("🛠️ Ingresa la nota práctica (0-100): "))
        
        if not (0 <= nota_teorica <= 100) or not (0 <= nota_practica <= 100):
            print("⚠️ Las notas deben estar entre 0 y 100.")
            return
    except ValueError:
        print("❌ Error de dato: Por favor, ingresa un número válido para las notas.")
        return

    promedio = (nota_teorica + nota_practica) / 2

    candidato = Informacion["Candidato"][cedula]
    if promedio >= 60:
        candidato["Estado"] = "Aprobado"
        candidato["Ruta"] = "No asignada"
        candidato["Riesgo"] = "Nulo"
        Informacion["Camper"][cedula] = Informacion["Candidato"].pop(cedula)

        print(f"\n🎉 ¡Felicidades! El candidato {candidato['Nombre']} ha sido promovido a Camper.")
    else:
        candidato["Estado"] = "No Aprobado"
        print(f"\n❌ El candidato {candidato['Nombre']} no aprobó. Promedio final: {promedio:.2f}")

    # Guardar los cambios
    guardar_datos()
    print("="*40)
    print("\n✅ Los datos se han actualizado correctamente.")
    print("="*40)



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



