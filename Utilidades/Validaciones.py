import re
import Utilidades.Datos as Datos

def validar_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validar_cedula(cedula):
    for Categoria in Datos.Informacion.values():
        if cedula in Categoria:
            return True
        return False