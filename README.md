# Work Project | Acme List: gestor de tareas

Este proyecto tiene como objetivo presentar de manera satisfactoria un pequeño software que solucione la necesidad de gestionar tareas del dia, teniendo la posibilidad de almacenar, crear o actualizar tareas y subtareas aledañas a estas dandole una prioridad, fecha de vencimiento de la tarea con su propia descripción de la tarea / subtarea.

## Contenido del proyecto

- [Work Project | Acme List: gestor de tareas](#work-project--acme-list-gestor-de-tareas)
  - [Contenido del proyecto](#contenido-del-proyecto)
  - [Comenzando 🚀](#comenzando-)
  - [Pre-requisitos 📖](#pre-requisitos-)
    - [Python](#python)
    - [Bibliotecas Estándar](#bibliotecas-estándar)
    - [Bibliotecas Externas](#bibliotecas-externas)
    - [Instalación de Dependencias](#instalación-de-dependencias)
  - [Errores conocidos hasta la fecha ⚠](#errores-conocidos-hasta-la-fecha-)
    - [**Problema:** Fallas al instalar Colorama](#problema-fallas-al-instalar-colorama)
  - [Construido con 🛠️](#construido-con-️)
  - [Autores ✒️](#autores-️)

## Comenzando 🚀

Puedes descargar el repositorio e iniciarlo mediante `main.py`

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
            }
        ]
    }
]
```

## Pre-requisitos 📖

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

### Python

Este proyecto requiere Python 3 o superior. Puedes descargar Python desde [python.org](https://www.python.org/downloads/).

Para instalar Python en Linux, sigue los pasos detallados en la [documentación oficial de Python sobre la instalación en plataformas Unix](https://docs.python.org/3/using/unix.html).

### Bibliotecas Estándar

El proyecto utiliza las siguientes bibliotecas estándar de Python, que no necesitan instalación adicional ya que vienen incluidas con Python:

- `getpass`: Para manejar entradas de contraseña de manera segura.
- `datetime`: Para manejar fechas y horas.
- `re`: Para trabajar con expresiones regulares.
- `threading`: Para manejar hilos de ejecución.

### Bibliotecas Externas

El proyecto también utiliza una biblioteca externa que necesita ser instalada:

- `colorama`: Para el formateo de texto en la consola (colores).

### Instalación de Dependencias

Para instalar todas las dependencias necesarias, ejecuta el siguiente comando:

```sh
pip install -r requirements.txt
```

## Errores conocidos hasta la fecha ⚠

### **Problema:** Fallas al instalar Colorama

**Solución:** *Verificar el entorno de Python*

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

## Construido con 🛠️

Unicamente Python 

## Autores ✒️

* [Kevin González - KevinJGV](https://github.com/KevinJGV)
* [Alvaro Andres Martinez Alcina - alvaroMartinez13](https://github.com/alvaroMartinez13)
* [Javier Eduardo Acevedo Noguera - JavierEAcevedoN](https://github.com/JavierEAcevedoN)
* [Mario Felipe Parra Delgado - MarioFelipe19](https://github.com/MarioFelipe19)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/KevinJGV/Work-Project_SCRUM_GonzalezKevinVelandia/graphs/contributors) quíenes han participado en este proyecto.