from Gestion_Datos.Manejo_datos import cargar_datos, guardar_datos
from Gestion_Datos.Datos import Informacion

def ver_informacion(rol):
    cargar_datos()
    cedula = input(f"\nIngrese la cédula del {rol}: ")
    print("\n" + "="*40)
    
    if cedula in Informacion[rol]:
        participante = Informacion[rol][cedula]

        print(f"\n🌟 Información del {rol} 🌟")
        print("="*40 + "\n")
        print(f"| {'Campo':<20} | {'Información':<28} |")
        print("|" + "="*22 + "|" + "="*30 + "|")
        print(f"| {'Cédula':<20} | {cedula:<28} |")
        print(f"| {'Nombre':<20} | {participante['Nombre']:<28} |")
        print(f"| {'Apellidos':<20} | {participante['Apellidos']:<28} |")
        print(f"| {'Email':<20} | {participante['Email']:<28} |")
        print(f"| {'Teléfono Móvil':<20} | {participante['Telefono']['Movil']:<28} |")
        print(f"| {'Teléfono Fijo':<20} | {participante['Telefono']['Fijo']:<28} |")
        print(f"| {'Rol':<20} | {rol:<28} |")
        print("\n" + "="*40)
    else:
        print("="*40 + "")
        print(f"\n❌ ¡Error! {rol} no encontrado. ❌\n")
        print("="*40 + "\n")
