# Acme List: gestor de tareas

## Contenido del proyecto

- [Acme List: gestor de tareas](#acme-list-gestor-de-tareas)
  - [Contenido del proyecto](#contenido-del-proyecto)
  - [Descripción](#descripción)
  - [Estructura de datos](#estructura-de-datos)
  - [Tecnologías implementadas](#tecnologías-implementadas)
  - [Uso](#uso)
  - [Errores conocidos hasta la fecha](#errores-conocidos-hasta-la-fecha)
  - [Autoría](#autoría)

## Descripción

Este proyecto tiene como objetivo presentar de manera satisfactoria un pequeño software que solucione la necesidad de gestionar tareas del dia, teniendo la posibilidad de almacenar, crear o actualizar tareas y subtareas aledañas a estas dandole una prioridad, fecha de vencimiento de la tarea con su propia descripción de la tarea / subtarea.

## Estructura de datos

Este programa funciona extrictamente con archvios de datos `json` con la siguiente estructura:

```json
[
    {
        "id_tarea": 4,
        "id_usuario": 1,
        "titulo": "Gestionar archivos (otro)",
        "descripcion": "otro programa para gestionar archivos",
        "fecha_limite": "09/11/2024",
        "estado": "cancelada",
        "prioridad": "alta",
        "subtareas": [
            {
                "id_subtarea": 1,
                "id_usuario": 1,
                "titulo": "Menú Principal",
                "descripcion": "hacer el menu principal",
                "fecha_limite": "01/11/2024",
                "estado": "cancelada",
                "prioridad": "media"
            },
            {
                "id_subtarea": 2,
                "id_usuario": 1,
                "titulo": "Menú crud a archivos",
                "descripcion": "el menu de gestion de archivos",
                "fecha_limite": "05/11/2024",
                "estado": "cancelada",
                "prioridad": "alta"
            }
        ]
    }
]
```

## Tecnologías implementadas

ACME List esta desarrollada en Python 3

## Uso

Descargar `.zip` del repositorio y ejecutar desde el archivo `main.py`

## Errores conocidos hasta la fecha

**Problema:** Fallas al instalar Colorama

**Solución:**

**Paso 1: Verificar la instalación del módulo**

1. Ejecuta el siguiente comando en tu terminal:

```sh
pip install colorama
```

* Si ya tienes Colorama instalado, verás un mensaje que indica que el requisito ya está satisfecho.
* Si no, el comando instalará el módulo.

**Paso 2: Verificar el entorno de Python**

1. Comprueba en qué entorno de Python estás ejecutando tu script.

* **Unix (Linux, macOS):**

```sh
which python
```

* **Windows:**

```sh
where python
```

2. Asegúrate de que la ruta del intérprete coincida con donde instalaste Colorama.

**Si el problema persiste:**

* Consulta la documentación oficial de Colorama: [https://super-devops.readthedocs.io/en/latest/misc.html](https://super-devops.readthedocs.io/en/latest/misc.html)
* Envía un problema en el repositorio de GitHub del proyecto: [https://github.com/tartley/colorama](https://github.com/tartley/colorama)

**Nota:**

* Si utilizas entornos virtuales (venv, virtualenv), asegúrate de instalar Colorama dentro del entorno activo.

**¡Esperamos que esto te ayude!**


## Autoría

* [Kevin González - KevinJGV](https://github.com/KevinJGV)
* [Alvaro Andres Martinez Alcina - alvaroMartinez13](https://github.com/alvaroMartinez13)
* [Javier Eduardo Acevedo Noguera - JavierEAcevedoN](https://github.com/JavierEAcevedoN)
* [Mario Felipe Parra Delgado - MarioFelipe19](https://github.com/MarioFelipe19)
