import json
import os
from Gestion_Datos.Datos import Informacion

Ruta_JSON = "SistemaEducativo.json"

def guardar_datos():
    try:
        if not os.path.exists(Ruta_JSON):
            with open(Ruta_JSON, "w", encoding='utf-8') as nuevo_archivo:
                json.dump(Informacion, nuevo_archivo, indent=4, ensure_ascii=False)
            print("✅ Archivo creado y datos guardados.")
        else:
            with open(Ruta_JSON, "w", encoding='utf-8') as file:
                json.dump(Informacion, file, indent=4, ensure_ascii=False)
            print("💾 Datos actualizados correctamente.")
    except Exception as e:
        print(f"❌ Error al guardar los datos: {e}")

def cargar_datos():
    try:
        if os.path.exists(Ruta_JSON):
            with open(Ruta_JSON, "r", encoding='utf-8') as archivo:
                Informacion.update(json.load(archivo))
            print("📥 Datos cargados correctamente.")
    except Exception as e:
        print(f"❌ Error al cargar Datos: {e}")
