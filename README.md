# Gestion Administrativa

El proyecto está diseñado para facilitar la gestión y administración de usuarios y entrenamientos a través de un sistema organizado y eficiente. Este sistema se basa en una estructura clara de roles y responsabilidades, permitiendo una administración efectiva y un seguimiento detallado del progreso de los usuarios.


## Tabla de contenidos

| Indice | Titulo |
|--|--|
| 1 | [Requisitos](#requisitos)|
| 2 | [Instalación](#instalacion)|
| 3 | [Uso](#uso)|
| 4 | [Tecnologías y Herramientas](#tecnologías-y-herramientas-utilizadas) |
| 5 | [Funcionalidades](#funcionalidades)|
| 6 | [Estructura del Proyecto](#estructura-del-proyecto) |
| 7 | [Manejo de Datos y Estructura JSON](#manejo-de-datos-y-estructura-json)|
| 8 | [Contribuir](#contribuir) |
| 9 | [Autor](#autor)|
| 10 | [Licencia](#licencia)|


## Requisitos

### Requisitos de Software

- **Visual Studio Code:** Se recomienda utilizar Visual Studio Code para el desarrollo. Puedes descargarlo desde [aquí](https://code.visualstudio.com/).
  
### Requisitos de Instalación

- **Git:** Para clonar el repositorio, necesitas tener Git instalado. Puedes descargarlo desde [aquí](https://git-scm.com/).


## Instalacion
Para instalar y ejecutar la página web localmente:

   1. Clona el repositorio:
   ```bash
   $ git clone https://github.com/JaimePrada11/Python.git
   ```
   2. Navega al directorio del proyecto:
   
   ```bash
   cd Python
   ```

## Uso
Para visualizar y trabajar con esta página web, sigue estos pasos:
1. **Abrir el Proyecto:**
   - Navega a la carpeta del proyecto donde has clonado o descomprimido el repositorio.
     
2. **Abrir el Archivo Principal:**
   - ejecuta el comando `python main.py` y sigue las instrucciones en la consola



## Tecnologías y Herramientas Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-%230078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

- **Python**: Utilizado para el desarrollo de la lógica y funcionalidad del proyecto.
- **Visual Studio Code**: Editor de código.


## Funcionalidades

- **Registro**: Permite ingresar y modificar la información de los usuarios
- **Asignacion de Rutas de Entrenamiento**: Administra diferentes rutas de entrenamiento.
- **Evaluacion**: Permite la evaluacion de los campers.
- **Reportes**: Genera reportes detallados.
- **Base de datos**: Guarda la informacion en un JSON.
  


## Estructura del Proyecto

El proyecto se organiza en torno a tres roles principales, cada uno con responsabilidades específicas que contribuyen a la funcionalidad general del sistema:

- **Coordinador**: 
  - **Responsabilidades**: Gestiona la administración general del proyecto, supervisa el funcionamiento de los otros roles.
  - **Funcionalidades**: Ver reportes de actividades y progreso, Asignar rutas a Trainers y Campers, Asignar salones para las actividades entre otras

- **Trainer**:
  - **Responsabilidades**: Se encarga de calificar el rendimiento de los usuarios en las rutas de entrenamiento.
  - **Funcionalidades**: Evaluación y calificación del progreso de los usuarios, asegurando que las evaluaciones sean precisas y justas.

- **Camper**:
  - **Responsabilidades**: Representa a los usuarios del sistema, gestiona su información personal 
  - **Funcionalidades**: Registro de datos personales, seguimiento del progreso en las rutas de entrenamiento.



## Manejo de Datos y Estructura JSON

La gestión de datos en el proyecto se realiza utilizando un archivo JSON que almacena la información de los usuarios y sus evaluaciones. A continuación, se describe la estructura del archivo JSON y las funciones asociadas para manejar estos datos.

### Esctructura JSON
```python
   {
    "Candidato": {},
    "Camper": {
        "123456": {
            "Nombre": "ANDRES",
            "Apellidos": "PRADA",
            "Direccion": "GIRON",
            "Email": "JANDRESPRADATO.11@GMAIL.COM",
            "Acudiente": "SONIA",
            "Telefono": {
                "Fijo": "6011639",
                "Movil": "3011778698"
            },
            "Estado": "Cursando",
            "Ruta": "Diseño de interiores",
            "Riesgo": true,
            "Grupo": "P1",
            "Notas": {
                "Fundamentos de programacion": {
                    "Introducción a la algoritmia": {
                        "Nota Teorica": 25,
                        "Nota Practica": 75,
                        "Nota Trabajos": 26.0,
                        "Nota Final": 55.1
                    },
                    "PSeInt": {
                        "Nota Teorica": 36,
                        "Nota Practica": 75,
                        "Nota Trabajos": 0,
                        "Nota Final": 55.8
                    }
                }
            },
            "Reprobadas": 2
        },
```
### Funciones de manejo de datos 
```python

import json

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
```

## Contribuir

¡Gracias por tu interés en contribuir a este proyecto! Aquí tienes algunos pasos para comenzar:

1. **Fork del Repositorio**
   - Realiza un fork del repositorio en GitHub para tener tu propia copia del proyecto. Puedes hacer esto haciendo clic en el botón "Fork" en la parte superior derecha de la página del repositorio.

2. **Clona el Repositorio**
   - Clona el repositorio forked a tu máquina local para que puedas trabajar en él. Usa el siguiente comando:
     ```bash
     git clone https://github.com/TU_USUARIO/NOMBRE_DEL_REPOSITORIO.git
     ```
   - Asegúrate de reemplazar `TU_USUARIO` y `NOMBRE_DEL_REPOSITORIO` con tu nombre de usuario y el nombre del repositorio correspondiente.

3. **Crea una Rama**
   - Crea una nueva rama para tus cambios. Es una buena práctica nombrar la rama de manera descriptiva:
     ```bash
     git checkout -b nombre-de-tu-rama
     ```

4. **Realiza Cambios**
   - Haz los cambios necesarios en el código, la documentación o en los archivos del proyecto. Asegúrate de probar tus cambios localmente antes de proceder.

5. **Commit y Push de tus Cambios**
   - Una vez que hayas realizado y probado tus cambios, realiza un commit y luego haz push a tu repositorio forked:
     ```bash
     git add .
     git commit -m "Descripción de los cambios"
     git push origin nombre-de-tu-rama
     ```

6. **Envía un Pull Request**
   - Ve a la página de tu repositorio en GitHub y verás una opción para enviar un pull request para tu rama. Haz clic en "New Pull Request", selecciona la rama en la que has trabajado y crea el pull request.
   - Asegúrate de proporcionar una descripción clara de los cambios que has realizado y cualquier detalle adicional que pueda ser útil para la revisión.


## Autor
Este proyecto fue desarrollado por Jaime Andres Prada Torres

- **Email**: [jandrespradato.11@gmail.com](mailto:jandrespradato.11@gmail.com)
Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través del enlace anterior.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.
