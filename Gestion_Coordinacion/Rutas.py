from Gestion_Datos.Manejo_datos import *
from Gestion_Datos.Datos import *

def Mostrar_rutas_entrenamiento():
    cargar_datos()

    print("\n" + "="*40)
    print("Las actuales rutas de entrenamiento son:")
    print("="*40)

    print(f"| {'#':<4} | {'Ruta':<30} |")
    print("="*40)

    for i, ruta in enumerate(Informacion["Rutas"].keys(), 1):
        print(f"| {i:<4} | {ruta:<30} |")

    print("="*40)

def seleccion_Ruta_entrenamiento():
    Mostrar_rutas_entrenamiento()
    try:
        Opc = int(input("Selecciona la ruta: "))
        lista_rutas = list(Informacion["Rutas"].keys())
        if 1 <= Opc <= len(lista_rutas):
            ruta_seleccionada = lista_rutas[Opc - 1]
            print(f"✅ Ruta seleccionada: {ruta_seleccionada}")
            return ruta_seleccionada
        else:
            print("❌ Opción inválida. Elige un número dentro del rango de rutas disponibles.")

    except ValueError:
        print("❌ Opción inválida. Debe ser un número.")
    except Exception as error:
        print(f"🚨 Error inesperado : {error} ")
        return None

def Nueva_Ruta_entrenamiento():
    cargar_datos()
    Mostrar_rutas_entrenamiento()

    opc = input("¿Desea Crear nueva ruta de entrenamiento? (s/n): ").lower()

    if opc == "s":
        nombre = input("Ingresa el nombre de la nueva ruta: ")
        if nombre not in Informacion["Rutas"]:
            Informacion["Rutas"][nombre] = {}
            print(f"\n✔ La nueva ruta de entrenamiento '{nombre}' ha sido creada exitosamente.")
            guardar_datos()
        else:
            print("\n❌ La ruta ya estaba creada.")
    elif opc == "n":
        return
    else:
        print("\n⚠️ Opción inválida. Por favor, ingresa 's' para sí o 'n' para no.")

def Crear_grupo_Ruta():
    cargar_datos()
    
    ruta_seleccionada = seleccion_Ruta_entrenamiento()
    
    if ruta_seleccionada:
        grupo = input("Ingresa el nombre del grupo: ").strip()
        
        if not grupo:
            print("❌ El nombre del grupo no puede estar vacío.")
            return
        
        if grupo in Informacion["Rutas"][ruta_seleccionada]:
            print(f"❌ El grupo '{grupo}' ya existe en la ruta '{ruta_seleccionada}'.")
            return
        
        Informacion["Rutas"][ruta_seleccionada][grupo] = {"Módulos": {}}
        guardar_datos()
        
        print(f"\n✔ El grupo '{grupo}' ha sido creado exitosamente en la ruta '{ruta_seleccionada}'.")
    else:
        print("❌ No se seleccionó ninguna ruta para crear el grupo.")

def mostrar_grupos_ruta():
    ruta_seleccionada = seleccion_Ruta_entrenamiento()
    if ruta_seleccionada:
        print(f"Los Grupos en la ruta '{ruta_seleccionada}':")
        grupos = Informacion["Rutas"][ruta_seleccionada].keys()

        if not grupos:
            print("No hay grupos en esta ruta.")
            return None
        
        print("\n" + "="*40)
        print(f"| {'#':<4} | {'Grupo':<30} |")
        print("="*40)

        for i, grupo in enumerate(grupos, 1):
            print(f"| {i:<4} | {grupo:<30} |")

        print("="*40)
        return grupos, ruta_seleccionada

    else:
        print("No se seleccionó ninguna ruta.")
        return None, None

def seleccionar_grupo():
    grupos, ruta_seleccionada  = mostrar_grupos_ruta()

    if grupos:
        try:
            opc_grupo = int(input("Selecciona el número del grupo: "))
            if 1 <= opc_grupo <= len(grupos):
                grupo_seleccionado = list(grupos)[opc_grupo - 1]
                return grupo_seleccionado, ruta_seleccionada
            else:
                print("❌ Opción inválida. Elige un número dentro del rango de grupos disponibles.")
        except ValueError:
            print("❌ Entrada inválida. Debe ingresar un número.")
        
    print("❌ No se seleccionó ningún grupo.")
    return None, None

def mostrar_opciones_SGDB(tipo):
    SGDB_lista = modulos_skills["Bases de datos"].copy()
    print("\n" + "="*40)
    print(f"Selecciona el SGDB {tipo}:")
    print("="*40)
    
    for i, valor in enumerate(SGDB_lista, 1):
        print(f"{i}. {valor}")
    print("="*40)

    return SGDB_lista

def Seleccionar_SGDB():
    Base_Datos = []
    tipos_SGDB = ["Principal", "Alternativo"]

    print("\n" + "="*40)
    print("Seleccionar SGBD:")
    print("="*40)

    for tipo in tipos_SGDB:
        while True:
            try:
                opciones = mostrar_opciones_SGDB(tipo)
                opc_SGDB = int(input(f"Ingrese el número del SGDB {tipo}: "))
            except ValueError:
                print("❌ Error: Por favor ingresa un número válido.")
                continue
            except Exception:
                print("❌ Error inesperado.")
                continue

            if 1 <= opc_SGDB <= len(opciones):
                SGDB_seleccionado = opciones.pop(opc_SGDB - 1)
                Base_Datos.append(SGDB_seleccionado)
                print(f"SGDB {tipo} seleccionado: {SGDB_seleccionado}")
                break
            else:
                print("❌ Opción inválida. Por favor selecciona una opción dentro del rango.")

    print("\n" + "="*40)
    print("SGBD Seleccionados:")
    print("="*40)

    print(f"| {'#':<4} | {'SGDB':<20} |")
    print("="*28)
    for i, sgdb in enumerate(Base_Datos, 1):
        print(f"| {i:<4} | {sgdb:<20} |")
    print("="*28)

    return Base_Datos

def mostrar_modulos():
    print("\n" + "="*40)
    print("Opciones de módulos:")
    print("="*40)

    for idx, modulo in enumerate(modulos_skills.keys(), 1):
        print(f"{idx}. {modulo}")
    print("="*40)

def tecnologias_modulo():
    mostrar_modulos()
    
    try:
        modulo_seleccionado = int(input("Selecciona el número del módulo: "))

        modulo = list(modulos_skills.keys())[modulo_seleccionado - 1]
        tecnologias = modulos_skills[modulo]
        
        if not tecnologias:
            print(f"No se han encontrado tecnologías para el módulo '{modulo}'.")
            return []
        
        print(f"Tecnologías para el módulo '{modulo}':")
        print("="*40)

        for i, tech in enumerate(tecnologias, 1):
            print(f"{i}. {tech}")
        print("="*40)

        return tecnologias

    except (ValueError, IndexError):
        print("❌ Opción inválida.")
        return []


def seleccionar_modulo():
    print("\n" + "="*40)
    print("Seleccionar Módulo:")
    print("="*40)

    mostrar_modulos()

    try:
        modulo_seleccionado = int(input("Selecciona el número del módulo que deseas: "))

        if 1 <= modulo_seleccionado <= len(modulos_skills):
            modulo = list(modulos_skills.keys())[modulo_seleccionado - 1]
            print(f"Modulación seleccionada: {modulo}")
            return modulo
        else:
            print("❌ Selección inválida. Por favor ingresa un número válido.")
            return None

    except ValueError:
        print("❌ Entrada no válida. Por favor ingresa un número.")
        return None




def Agregar_modulos_ruta():
    cargar_datos()
    grupo_seleccionado, ruta_seleccionada  = seleccionar_grupo()

    if grupo_seleccionado:

        if ruta_seleccionada:
            if ruta_seleccionada not in Informacion["Rutas"]:
                Informacion["Rutas"][ruta_seleccionada] = {}

            if grupo_seleccionado not in Informacion["Rutas"][ruta_seleccionada]:
                Informacion["Rutas"][ruta_seleccionada][grupo_seleccionado] = {"Módulos": {}}

            modulo_seleccionado = seleccionar_modulo()

            if modulo_seleccionado:
                Informacion["Rutas"][ruta_seleccionada][grupo_seleccionado]["Módulos"][modulo_seleccionado] = {}

                print(f"✔ Módulo '{modulo_seleccionado}' agregado al grupo '{grupo_seleccionado}' en la ruta '{ruta_seleccionada}'.")

                tecnologias_seleccionadas = tecnologias_modulo()
            while True:
                if tecnologias_seleccionadas:
                    Informacion["Rutas"][ruta_seleccionada][grupo_seleccionado]["Módulos"][modulo_seleccionado].update(tecnologias_seleccionadas)
                    print("✔ Tecnologías seleccionadas agregadas al módulo.")

                continuar = input("¿Deseas agregar otro módulo a esta ruta? (s/n): ").lower()
                if continuar != 's':
                     break
                else:
                    print("⚠️ No se seleccionaron tecnologías para el módulo.")

                guardar_datos()
            else:
                print("❌ No se seleccionó ningún módulo.")
        else:
            print("❌ No se seleccionó ninguna ruta.")
    else:
        print("❌ No se seleccionó ningún grupo.")
