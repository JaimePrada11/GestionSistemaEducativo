from Gestion_Datos.Datos import *
from Gestion_Datos.Manejo_datos import *
from Utilidades.Validaciones import *
from Utilidades.Consulta_Informacion_personal import *


def obtener_rol(cedula):
    cargar_datos()
    for rol, usuarios in Informacion.items():
      if isinstance(usuarios, dict) and cedula in usuarios:
            return rol
    return None 

def registro(rol):

    cargar_datos()
    usuario = {}

    print("="*40)
    print(f"📝 Registro de {rol} 📝")
    print("="*40)

    while True:
        cedula = input("\n🆔 Ingresa la cedula: ")
        if not cedula.isdigit():
            print("❌ La cedula debe contener solo números.\n")
            continue

        rol_asociado = obtener_rol(cedula)
        if rol_asociado:
            print(f"❌ La cedula ya está asociada a un {rol_asociado.lower()}.\n")
            return
        
        if Informacion[rol].get(cedula) is not None:
            print(f"⚠️ La cédula ya existe en el sistema como {rol.lower()}. Por favor, verifica los datos.\n")
            return
        break

    usuario["Nombre"] = input("\n👤 Ingresa el nombre: ")
    usuario["Apellidos"] = input("👤 Ingresa los apellidos: ")
    usuario["Direccion"] = input("🏠 Ingresa la dirección: ")

    while True:
        email = input("📧 Ingresa el email: ")
        if validar_email(email):
            usuario["Email"] = email
            break
        else:
            print("❌ Email no válido. Por favor, ingresa un email correcto.\n")

    while True:
        telefono_fijo = input("☎️ Ingresa el teléfono fijo: ")
        if telefono_fijo.isdigit():
            usuario["Telefono"] = {"Fijo": telefono_fijo}
            break
        else:
            print("❌ El teléfono fijo debe contener solo números.\n")

    while True:
        telefono_movil = input("📱 Ingresa el teléfono móvil: ")
        if telefono_movil.isdigit():
            usuario["Telefono"]["Movil"] = telefono_movil
            break
        else:
            print("❌ El teléfono móvil debe contener solo números.\n")

    if rol == "Candidato":
        usuario["Acudiente"] = input("👨‍👩‍👦 Ingresa el nombre del acudiente: ")
        usuario["Estado"] = "Inscrito"
    elif rol == "Trainer":
        usuario["Estado"] = True
        usuario["Grupo"] = [] 

    Informacion[rol][cedula] = usuario
    guardar_datos()

    print("\n" + "="*40)
    print(f"✅ 📄 Información del {rol.lower()} guardada exitosamente. ✅")
    print("="*40)

def actualizar_usuario(rol):
    print("\n=== Actualización de usuario ===")
    
    cedula = ver_informacion(rol)
    if not cedula:
        print("\n❌ Operación cancelada.")
        return

    usuario = Informacion[rol][cedula]

    print("\n¿Qué desea actualizar?")
    print("1. Nombre")
    print("2. Apellidos")
    print("3. Dirección")
    print("4. Email")
    print("5. Teléfono Fijo")
    print("6. Teléfono Móvil")
    if rol in ["Candidato", "Camper"]:
        print("7. Acudiente")
    print("8. Cancelar")

    opcion = input("\nSeleccione una opción (1-8): ")

    if opcion not in map(str, range(1, 8)):
        print("\n❌ Opción no válida.")
        return

    if opcion == "1":
        usuario["Nombre"] = input("Ingrese el nuevo nombre: ")
    elif opcion == "2":
        usuario["Apellidos"] = input("Ingrese los nuevos apellidos: ")
    elif opcion == "3":
        usuario["Direccion"] = input("Ingrese la nueva dirección: ")
    elif opcion == "4":
        while True:
            email = input("Ingrese el nuevo email: ")
            if validar_email(email):
                usuario["Email"] = email
                break
            else:
                print("❌ Email no válido. Intente de nuevo.")
    elif opcion == "5":
        while True:
            telefono_fijo = input("Ingrese el nuevo teléfono fijo: ")
            if telefono_fijo.isdigit():
                usuario["Telefono"]["Fijo"] = telefono_fijo
                break
            else:
                print("❌ El teléfono fijo debe contener solo números.")
    elif opcion == "6":
        while True:
            telefono_movil = input("Ingrese el nuevo teléfono móvil: ")
            if telefono_movil.isdigit():
                usuario["Telefono"]["Movil"] = telefono_movil
                break
            else:
                print("❌ El teléfono móvil debe contener solo números.")
    elif opcion == "7" and rol in ["Candidato", "Camper"]:
        usuario["Acudiente"] = input("Ingrese el nuevo acudiente: ")
    elif opcion == "8":
        print("\n❌ Actualización cancelada.")
        return

    guardar_datos()
    print("\n✅ Usuario actualizado correctamente.")

    
