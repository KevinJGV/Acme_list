from datetime import datetime
import cruds
import funciones

tarea_registro = "data_base/tareas_registradas.json"
tarea_en_curso = "data_base/tareas_en_curso.json"
tarea_terminado = "data_base/tareas_terminadas.json"
tarea_cancelado = "data_base/tareas_canceladas.json"

datos_registro = cruds.cargar_datos_json(tarea_registro)
datos_en_curso = cruds.cargar_datos_json(tarea_en_curso)
datos_terminado = cruds.cargar_datos_json(tarea_terminado)
datos_cancelado = cruds.cargar_datos_json(tarea_cancelado)

# muestra las tareas que no se han terminado
def tareaspendientes(tareas):
    for i in tareas:
        if i["estado"] == "por hacer":
            funciones.imprimir_tabla_diccionario_lista([i])

# muestra las tareas terminadas
def tareasterminadas(tareas):
    for i in tareas:
        if i["estado"] == "terminada":
            funciones.imprimir_tabla_diccionario_lista([i])

# muestra las tareas canceladas
def tareascanceladas(tareas):
    for i in tareas:
        if i["estado"] == "cancelada":
            funciones.imprimir_tabla_diccionario_lista([i])

# muestra las tareas en curso
def tareasencurso(tareas):
    for i in tareas:
        if i["estado"] == "en curso":
            funciones.imprimir_tabla_diccionario_lista([i])

# muestra las tareas por orden de prioridad (alta, media, baja)
def prioridadtareas(tareas):
    alta = []
    media = []
    baja = []

    for i in tareas:
        if i["prioridad"] == "alta":
            alta.append(i)
        elif i["prioridad"] == "media":
            media.append(i)
        elif i["prioridad"] == "baja":
            baja.append(i)

    for i in alta:
        funciones.imprimir_tabla_diccionario_lista([i])
    for i in media:
        funciones.imprimir_tabla_diccionario_lista([i])
    for i in baja:
        funciones.imprimir_tabla_diccionario_lista([i])

# muestra las tareas que se tienen fecha limite cercana dentro de 7 dias en adelante
def tareascercanas(tareas):
    for i in tareas:
        if i["fecha_limite"]:
            fecha_limite = datetime.strptime(i["fecha_limite"], "%d/%m/%Y")
            fecha_actual = datetime.now()
            diferencia = fecha_limite - fecha_actual
            if -1 <= diferencia.days <= 6:
                funciones.imprimir_tabla_diccionario_lista([i])

# esta es la funcion del menu de filtros
def menufiltros():
    while True:
        choice = -1
        try:

            # opciones
            choice = int(input("""
Menu general
ingresa la opcion: 
(1) Mostrar tareas pendientes.
(2) Mostrar tareas terminadas.
(3) Mostrar tareas canceladas.
(4) Mostrar tareas en curso.
(5) Mostrar tareas por orden de prioridad.
(6) Mostrar tareas cercanas.
(0) Terminar. """))
        
        except Exception as e:
            print("error en la seleccion: ",e)

        if choice == 1:
            tareaspendientes(datos_registro)
        elif choice == 2:
            tareasterminadas(datos_registro)
        elif choice == 3:
            tareascanceladas(datos_registro)
        elif choice == 4:
            tareasencurso(datos_registro)
        elif choice == 5:
            prioridadtareas(datos_registro)
        elif choice == 6:
            tareascercanas(datos_registro)
        elif choice == 0:
            print("terminando proceso")
            break