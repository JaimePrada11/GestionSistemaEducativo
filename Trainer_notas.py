import Cargar_Guardar_datos as Datos

notas =[]

def Trabajos_Clase():
    global notas 
    try:
        Cant_Notas = int(input("Ingresa cantidad de notas"))
    except Exception:
        print("ok")

    Nota_final=0
    Nota_parcial = 0

    if Cant_Notas > 1:
        for i in range(Cant_Notas):
            Nota=int(input("Ingresa el valor de la nota"))
            porcentaje = int(input("Ingresa el porcentaje de la nota"))
            
            notas.append(Nota)
            nota_porcentual = Nota * (porcentaje/100)
            Nota_parcial += nota_porcentual
        Nota_final = Nota_parcial * 0.1
    else:
        Nota=int(input("Ingresa el valor de la nota"))
        Nota_final = Nota * 0.1
    return Nota_final


def Ingresar_Nota():
    global notas
    print("*****")
    nota_teoria = int(input("Ingresa nota teorica"))
    nota_practica = int(input("Ingresa nota practica"))
    nota_trabajos = Trabajos_Clase()

    final = nota_teoria*.3 + nota_practica*0.6 + nota_trabajos

    print(final)

def calificar_modulo():
    Datos.cargar_datos()

    print("Las rutas de entrenamiento disponibles son:")
    for i, ruta in enumerate(Datos.Informacion["Rutas"], 1):
        print(f"{i}. {ruta}")

    try:
        opc_ruta = int(input("Selecciona la ruta para calificar los módulos: "))
        if 1 <= opc_ruta <= len(Datos.Informacion["Rutas"]):
            ruta_seleccionada = list(Datos.Informacion["Rutas"])[opc_ruta - 1]
        else:
            print("Opción inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    print(f"Los grupos en la ruta '{ruta_seleccionada}' son:")
    for i, grupo in enumerate(Datos.Informacion["Rutas"][ruta_seleccionada], 1):
        print(f"{i}. {grupo}")

    try:
        opc_grupo = int(input("Selecciona el grupo para calificar los módulos: "))
        if 1 <= opc_grupo <= len(Datos.Informacion["Rutas"][ruta_seleccionada]):
            grupo_seleccionado = list(Datos.Informacion["Rutas"][ruta_seleccionada])[opc_grupo - 1]
        else:
            print("Opción inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    if "Módulos" not in Datos.Informacion["Rutas"][ruta_seleccionada][grupo_seleccionado]:
        print("El grupo seleccionado no tiene módulos para calificar.")
        return

    while True:  
        modulos_grupo = Datos.Informacion["Rutas"][ruta_seleccionada][grupo_seleccionado]["Módulos"]
        for modulo, tecnologias in modulos_grupo.items():
            print(f"Calificando módulo '{modulo}':")
            for tecnologia in tecnologias:
                print(f"Calificación para '{tecnologia}':")
                calificacion = Ingresar_Nota()

        respuesta = input("¿Desea seguir calificando otra nota? (s/n): ")
        if respuesta.lower() != 's':
            break

    print("Calificación completada.")
