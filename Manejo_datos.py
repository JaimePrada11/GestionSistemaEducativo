import json

from Datos import *


Ruta_JSON = "Base_Datos.json"


def guardar_datos():
    try:
        contenido = json.dumps(Informacion, indent=4,  ensure_ascii=False)
        with open(Ruta_JSON, "w", encoding='utf-8') as file:
            file.write(contenido)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos():
    try:
        with open(Ruta_JSON, mode="r", encoding='utf-8') as archivo:
            Informacion.update(json.load(archivo))
    except Exception as e:
        print(f"Error al cargar Datos {e}")