import Gestion_Datos.Manejo_datos as Datos
import Utilidades.Validaciones as validar
import Utilidades.Validaciones
from Gestion_Coordinacion.Rutas import mostrar_grupo_ruta

def registro(rol):

    Datos.cargar_datos()
    persona = {}

    print("="*40)
    print(f"📝 Registro de {rol} 📝")
    print("="*40)

    while True:
        cedula = input("\n🆔 Ingresa la cédula: ")
        if not cedula.isdigit():
            print("❌ La cédula debe contener solo números.\n")
            continue

        if validar.validar_cedula(cedula):
            print(f"❌ La cédula ingresada ya está en uso para un {rol.lower()}.\n")
            return
        
        if Datos.Informacion[rol].get(cedula) is not None:
            print(f"⚠️ La cédula ya existe en el sistema como {rol.lower()}. Por favor, verifica los datos.\n")
            return
        break

    # Solicitar información básica
    persona["Nombre"] = input("\n👤 Ingresa el nombre: ")
    persona["Apellidos"] = input("👤 Ingresa los apellidos: ")
    persona["Direccion"] = input("🏠 Ingresa la dirección: ")

    # Validar email
    while True:
        email = input("📧 Ingresa el email: ")
        if validar.validar_email(email):
            persona["Email"] = email
            break
        else:
            print("❌ Email no válido. Por favor, ingresa un email correcto.\n")

    # Validar teléfono fijo
    while True:
        telefono_fijo = input("☎️ Ingresa el teléfono fijo: ")
        if telefono_fijo.isdigit():
            persona["Telefono"] = {"Fijo": telefono_fijo}
            break
        else:
            print("❌ El teléfono fijo debe contener solo números.\n")

    # Validar teléfono móvil
    while True:
        telefono_movil = input("📱 Ingresa el teléfono móvil: ")
        if telefono_movil.isdigit():
            persona["Telefono"]["Movil"] = telefono_movil
            break
        else:
            print("❌ El teléfono móvil debe contener solo números.\n")

    # Configuración específica según el tipo de persona
    if rol == "Candidato":
        persona["Acudiente"] = input("👨‍👩‍👦 Ingresa el nombre del acudiente: ")
        persona["Estado"] = "Inscrito"
    elif rol == "Trainer":
        persona["Ruta"] = "No asignado"
        persona["Grupo"] = "No asignado"

    # Guardar datos
    Datos.Informacion[rol][cedula] = persona
    Datos.guardar_datos()

    # Confirmación final
    print("\n" + "="*40)
    print(f"✅ 📄 Información del {rol.lower()} guardada exitosamente. ✅")
    print("="*40)



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
