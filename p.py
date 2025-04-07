import json

# Estructuras de datos iniciales
informacion = {
    "Candidato": {},
    "Camper": {},
    "Trainer": {},
    "Rutas": {
        "NodeJS": {},
        "Java": {},
        "NetCore": {}
    }
}

modulos_skills = {
    "Fundamentos de programación": ["Introducción a la algoritmia", "PSeInt", "Python"],
    "Fundamentos web": ["HTML", "CSS", "Bootstrap"],
    "Programación formal": ["Java", "JavaScript", "C#"],
    "Bases de datos": ["MySQL", "MongoDB", "PostgreSQL"],
    "Backend": ["NetCore", "Spring Boot", "NodeJS", "Express"]
}

ruta_json = "SistemaEducativo.json"

# Funciones generales de carga y guardado de datos
def guardar_datos():
    try:
        with open(ruta_json, "w", encoding="utf-8") as file:
            json.dump(informacion, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos():
    try:
        with open(ruta_json, "r", encoding="utf-8") as archivo:
            informacion.update(json.load(archivo))
    except FileNotFoundError:
        print("Archivo no encontrado. Se utilizará la estructura por defecto.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

# Funciones auxiliares para entradas y validaciones
def obtener_opcion_numerica(mensaje, rango):
    try:
        opcion = int(input(mensaje))
        if 1 <= opcion <= rango:
            return opcion
        else:
            print("❌ Opción fuera de rango. Intenta nuevamente.")
    except ValueError:
        print("❌ Entrada inválida. Por favor, ingresa un número.")
    return None

def mostrar_lista(items, titulo):
    print("\n" + "=" * 40)
    print(titulo)
    print("=" * 40)
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    print("=" * 40)

# Funciones principales
def mostrar_rutas_entrenamiento():
    cargar_datos()
    rutas = list(informacion["Rutas"].keys())
    mostrar_lista(rutas, "Las actuales rutas de entrenamiento son:")
    return rutas

def seleccionar_ruta_entrenamiento():
    rutas = mostrar_rutas_entrenamiento()
    opcion = obtener_opcion_numerica("Selecciona la ruta: ", len(rutas))
    if opcion:
        ruta = rutas[opcion - 1]
        print(f"✅ Ruta seleccionada: {ruta}")
        return ruta
    return None

def nueva_ruta_entrenamiento():
    cargar_datos()
    nueva_ruta = input("Ingresa el nombre de la nueva ruta: ").strip()
    if nueva_ruta not in informacion["Rutas"]:
        informacion["Rutas"][nueva_ruta] = {}
        print(f"✔ La ruta '{nueva_ruta}' ha sido creada exitosamente.")
        guardar_datos()
    else:
        print("❌ La ruta ya existe.")

def crear_grupo_ruta():
    cargar_datos()
    ruta = seleccionar_ruta_entrenamiento()
    if ruta:
        grupo = input("Ingresa el nombre del grupo: ").strip()
        if grupo not in informacion["Rutas"][ruta]:
            informacion["Rutas"][ruta][grupo] = {"Módulos": {}}
            print(f"✔ Grupo '{grupo}' creado en la ruta '{ruta}'.")
            guardar_datos()
        else:
            print("❌ El grupo ya existe en esta ruta.")

def mostrar_grupos_ruta():
    ruta = seleccionar_ruta_entrenamiento()
    if ruta:
        grupos = list(informacion["Rutas"][ruta].keys())
        mostrar_lista(grupos, f"Grupos en la ruta '{ruta}':")
        return grupos, ruta
    return None, None

def agregar_modulos_ruta():
    cargar_datos()
    grupos, ruta = mostrar_grupos_ruta()
    if grupos:
        opcion_grupo = obtener_opcion_numerica("Selecciona el grupo: ", len(grupos))
        if opcion_grupo:
            grupo = grupos[opcion_grupo - 1]
            while True:
                mostrar_lista(list(modulos_skills.keys()), "Seleccionar Módulo:")
                opcion_modulo = obtener_opcion_numerica("Selecciona el módulo: ", len(modulos_skills))
                if opcion_modulo:
                    modulo = list(modulos_skills.keys())[opcion_modulo - 1]

                    if modulo == "Bases de datos":
                        tecnologias = modulos_skills[modulo]
                        mostrar_lista(tecnologias, "Selecciona las tecnologías de base de datos:")
                        seleccion_principal = obtener_opcion_numerica("Selecciona la tecnología principal: ", len(tecnologias))
                        if seleccion_principal:
                            tecnologia_principal = tecnologias[seleccion_principal - 1]
                            print(f"✔ Tecnología principal seleccionada: {tecnologia_principal}")

                            tecnologias_restantes = [t for t in tecnologias if t != tecnologia_principal]
                            mostrar_lista(tecnologias_restantes, "Selecciona la tecnología secundaria:")
                            seleccion_secundaria = obtener_opcion_numerica("Selecciona la tecnología secundaria: ", len(tecnologias_restantes))
                            if seleccion_secundaria:
                                tecnologia_secundaria = tecnologias_restantes[seleccion_secundaria - 1]
                                print(f"✔ Tecnología secundaria seleccionada: {tecnologia_secundaria}")

                                informacion["Rutas"][ruta][grupo]["Módulos"].setdefault(modulo, [])
                                informacion["Rutas"][ruta][grupo]["Módulos"][modulo].extend(["Principal: " + tecnologia_principal, "Secundaria: " + tecnologia_secundaria])
                                guardar_datos()
                            else:
                                print("❌ Selección de tecnología secundaria inválida.")
                        else:
                            print("❌ Selección de tecnología principal inválida.")

                    else:
                        tecnologias = modulos_skills[modulo]
                        mostrar_lista(tecnologias, "Selecciona las tecnologías:")
                        seleccionadas = []
                        while True:
                            seleccion = obtener_opcion_numerica("Selecciona una tecnología (0 para finalizar): ", len(tecnologias))
                            if seleccion == 0:
                                break
                            elif seleccion:
                                tecnologia = tecnologias[seleccion - 1]
                                if tecnologia not in seleccionadas:
                                    seleccionadas.append(tecnologia)
                                    print(f"✔ Tecnología '{tecnologia}' agregada.")
                                else:
                                    print(f"⚠️ La tecnología '{tecnologia}' ya fue seleccionada.")

                        if seleccionadas:
                            informacion["Rutas"][ruta][grupo]["Módulos"].setdefault(modulo, []).extend(seleccionadas)
                            guardar_datos()

                continuar = input("¿Deseas agregar otro módulo? (s/n): ").lower()
                if continuar != "s":
                    break
    else:
        print("❌ No se encontraron grupos para agregar módulos.")
