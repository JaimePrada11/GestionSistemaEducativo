import Cargar_Guardar_datos as Datos
import Horarios
import datetime

def rutas():
    Datos.cargar_datos()
    print("***********")
    print("Las actuales rutas de entrenamiento son: ")
    for i, ruta in enumerate(Datos.Informacion["Rutas"].keys(), 1):
        print(f"{i}. {ruta}")
    try:
        opc = int(input("Selecciona la Ruta que desea agregar sus modulos: "))
        lista_rutas = list(Datos.Informacion["Rutas"].keys())
        if 1 <= opc <= len(lista_rutas):
            ruta_seleccionada = lista_rutas[opc - 1]
            return ruta_seleccionada
        else:
            print("Opcion Invalida")
    except ValueError:
        print("Entrada invalida, Solo pueden ser numeros")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrar_grupo_ruta():
    ruta_seleccionada = rutas()
    if ruta_seleccionada:
        print(f"Los Grupos en la ruta '{ruta_seleccionada}':")
        grupos = Datos.Informacion["Rutas"][ruta_seleccionada].keys()
        if not grupos:
            print("No hay grupos en esta ruta.")
            return None
            
        grupo_seleccionado = None
        for i, grupo in enumerate(grupos, 1):
            print(f"{i}. {grupo}")

        try:
            opc_grupo = int(input("Selecciona el número del grupo: "))
            if 1 <= opc_grupo <= len(grupos):
                grupo_seleccionado = list(grupos)[opc_grupo - 1]
            else:
                print("Opción inválida")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")
        
        if grupo_seleccionado:
            return ruta_seleccionada, grupo_seleccionado
        else:
            print("No se seleccionó ningún grupo.")
            return None

def Nueva_Ruta():
    Datos.cargar_datos()
    for i, ruta in enumerate(Datos.Informacion["Rutas"].keys(), 1):
        print(f"{i}. {ruta}")
    opc =input("Desea Crear nueva ruta de entrenamiento? (s/n)").lower()
    if opc =="s":
        nombre= input("Ingresa el nombre de la nueva ruta")
        if nombre not in Datos.Informacion["Rutas"].keys():
            Datos.Informacion["Rutas"][nombre]={}
            print(f"La nueva ruta de entrenamiento '{nombre}' ha sido creada exitosamente.")
            Datos.guardar_datos()
        else:
            print("La ruta ya estaba creada")
    elif opc == "n":
        return
    else:
        print("Opcion Invalida")


def Crear_grupo_Ruta():
    Datos.cargar_datos()
    nv_ruta = {"Módulos": {}}
    ruta_seleccionada = rutas()

    if ruta_seleccionada:
        grupo = input("Ingresa el nombre del grupo: ")
        if grupo:
            for ruta, grupos in Datos.Informacion["Rutas"].items():
                if grupo in grupos:
                    print(f"El grupo {grupo} ya existe en la ruta '{ruta}' ")
                    return
                
            Datos.Informacion["Rutas"][ruta_seleccionada][grupo] = nv_ruta
            Datos.guardar_datos()
        else:
            print("El nombre del grupo no puede estar vacío.")
    else:
        print("No se seleccionó ninguna ruta.")


def ver_modulos():
    print("*********")
    print("Módulos disponibles---->")
    for i, mod in enumerate(Datos.modulos_skills, 1):
        for llave in mod:
            print(f"{i}. {llave}")
    
    try:
        opc = int(input("Selecciona el módulo: "))
    except ValueError:
        print("Ingresa un número válido")
        return None
    else:
        if not (1 <= opc <= len(Datos.modulos_skills)):
            print("Opción inválida")
            return None
    
    for i, mod in enumerate(Datos.modulos_skills, 1):
        if i == opc:
            mod_seleccionado = {}
            for modulo_nombre, info_modulo in mod.items():
                print(f"Modulo: {modulo_nombre}")
                print("Tecnologías:")
                if modulo_nombre == "Bases de datos":
                    sgdb_seleccionados = Seleccionar_SGDB()
                    mod_seleccionado[modulo_nombre] = sgdb_seleccionados
                else:
                    for tecnologia in info_modulo["Tecnologías"]:
                        print(f"- {tecnologia}")
                    
                    inicio, fin = Horarios.solicitar_fechas()
                    info_modulo["Inicio"] = inicio.strftime("%Y-%m-%d")
                    info_modulo["Fin"] = fin.strftime("%Y-%m-%d")
                    
                    mod_seleccionado[modulo_nombre] = info_modulo
            
            return mod_seleccionado
    
    return None

def Agregar_modulos_ruta():
    Datos.cargar_datos()
    print("***")
    print("Las actuales rutas de entrenamiento son: ")
    for i, ruta in enumerate(Datos.Informacion["Rutas"].keys(), 1):
        print(f"{i}. {ruta}")

    try:
        opc = int(input("Selecciona la Ruta a la que deseas agregar sus módulos: "))
        lista_rutas = list(Datos.Informacion["Rutas"].keys())
        if 1 <= opc <= len(lista_rutas):
            ruta_seleccionada = lista_rutas[opc - 1]
        else:
            print("Opción inválida")
            return
    except ValueError:
        print("Ingresa un número válido")
        return

    identificador = input("Ingresa el nombre del grupo dentro de la ruta: ")
    if identificador not in Datos.Informacion["Rutas"][ruta_seleccionada]:
        print(f"No se encontró el grupo '{identificador}' en la ruta seleccionada.")
        return

    if "Módulos" not in Datos.Informacion["Rutas"][ruta_seleccionada][identificador]:
        Datos.Informacion["Rutas"][ruta_seleccionada][identificador]["Módulos"] = {}
        Datos.Informacion["Rutas"][ruta_seleccionada][identificador]["Horario"] = None
        Datos.Informacion["Rutas"][ruta_seleccionada][identificador]["Salon"] = None

    while True:
        mod = ver_modulos()
        if mod:
            Datos.Informacion["Rutas"][ruta_seleccionada][identificador]["Módulos"].update(mod)
            Datos.guardar_datos()
        continuar = input("¿Deseas agregar otro módulo a esta ruta? (s/n): ").lower()
        if continuar != 's':
            break


def Seleccionar_SGDB():
    Datos.cargar_datos()
    Base_Datos = []
    SGDB_lista = Datos.modulos_skills[3]["Bases de datos"].copy()

    for tipo in ["Principal", "Alternativo"]:
        while True:
            print(f"Selecciona el SGDB {tipo}:")
            for i, valor in enumerate(SGDB_lista, 1):
                print(f"{i}. {valor}")
            
            try:
                opc_SGDB = int(input(f"Ingrese el número del SGDB {tipo}: "))
            except ValueError:
                print("Error: Por favor ingresa un número válido.")
                continue

            if 1 <= opc_SGDB <= len(SGDB_lista):
                SGDB_seleccionado = SGDB_lista.pop(opc_SGDB - 1)
                Base_Datos.append(SGDB_seleccionado)
                print(f"SGDB {tipo} seleccionado: {SGDB_seleccionado}")
                break
            else:
                print("Opción inválida. Por favor selecciona una opción dentro del rango.")
    return Base_Datos


