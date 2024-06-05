import json

Informacion = {"Candidato": {}, 
               "Camper": {}, 
               "Trainer": {},
               "Rutas": {
                   "Ruta NodeJS": {}, 
                   "Ruta Java": {},
                   "Ruta NetCore": {}
                   }
               }




modulos_skills = [
    {"Fundamentos de programacion":["Introducción a la algoritmia", "PSeInt",  "Python"]},
    {"Fundamentos web":["HTML", "CSS", "Bootstrap"]},
    {"Programación formal":["Java", "JavaScript", "C#"]},
    {"Bases de datos":["Mysql", "MongoDb" , "Postgresql"]},
    {"Backend":["NetCore", "Spring Boot", "NodeJS", "Express"]}
] 


Ruta_JSON = "Base_Datos.json"


def guardar_datos():
    try:
        contenido = json.dumps(Informacion, indent=4,  ensure_ascii=False)
        with open(Ruta_JSON, "w", encoding='utf-8') as file:
            file.write(contenido)
    except Exception:
        print("Error al guardar los datos:")

def cargar_datos():
    try:
        with open(Ruta_JSON, mode="r", encoding='utf-8') as archivo:
            Informacion.update(json.load(archivo))
    except Exception:
        print("Error al cargar Datos")