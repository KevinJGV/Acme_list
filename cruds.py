import funciones_json
import funciones

# Aquí va la direccion de los archivos que se realizan CRUD
tarea_registro = "data_base/eventos_registrados.json"
tarea_en_curso = "data_base/eventos_en_curso.json"
tarea_terminado = "data_base/eventos_terminados.json"
usuario = "data_base/informacion_usuarios.json"

#Guarda los datos de las tareas JSON  
datos_regitro = funciones_json.cargar_datos_json(tarea_registro)
datos_en_curso = funciones_json.cargar_datos_json(tarea_en_curso)
datos_terminado = funciones_json.cargar_datos_json(tarea_terminado)
datos_usuario = funciones_json.cargar_datos_json(usuario)


#Crea una nueva tarea
def crea_tarea(id_usuario, tarea:dict):
    
    try:

        id_tarea = funciones.generador_id(tarea)

        task_data = {
            "id_tarea": id_tarea,
            "id_usuario": id_usuario,
            **tarea 
        }

        tarea.append(task_data)

        funciones_json.guardar_datos_json(tarea, datos_regitro)

        return f"Tarea creada con éxito."
    
    except Exception as e:
        print(f"Error al crear la tarea: {e}")
        return "Error al crear la tarea."


#Modifica una tarea
def modifica_tarea(id_tarea, tarea:dict):
    print()


#Crea una nueva subtarea
def crea_tarea(id_tarea, subtarea:dict):
    
    try:

        tarea = funciones.valida_campos("")

        id_subtarea = funciones.generador_id(subtarea)

        task_data = {
            "id_subtarea": id_subtarea,
            "id_tarea": id_tarea,
            **subtarea 
        }

        subtarea.append(task_data)

        funciones_json.guardar_datos_json(subtarea, datos_regitro)

        return f"subtarea creada con éxito."
    
    except Exception as e:
        print(f"Error al crear la subtarea: {e}")
        return "Error al crear la subtarea."


#Modifica una subtarea
def modifica_tarea(id_subtarea, subtarea:dict):
    print()


#Cambia el estado de la tarea / subtarea
def estado(id, dato:dict, tarea=False):
    print()


import signin
import main
import filters

# aqui estan las funciones para extraer y agregar la informacion de los archivos json
import json

# cargar los datos de un archivo json
# en el parametro de ruta se pone la ruta relativa del archivo json que se quiere leer
def cargar_datos_json(ruta):
    datos = {}
    file = open(ruta,"r")
    datos = json.load(file)
    return datos

# guardar los datos en un archivo json
# en el parametro de ruta se pone la ruta relativa del archivo json que se quiere leer
# en el parametro datos se pone los datos que se van a agregar
# al agregar los datos utilizar el mismo contenido del archivo antes de modificar + los cambios que se le alla hecho por medio de na variable
def guardar_datos_json(datos, ruta):
    datos = list(datos)
    diccionario = json.dumps(datos, indent=4)
    file = open(ruta,"w")
    file.write(diccionario)
    file.close()

# esta funcion sirve para indicar si una tarea tiene subtareas o no
# y si tiene subtareas verificar si estan todas terminadas y poner la tarea en terminada
def subtareasfinalizadas(tarea):
    if any(tarea["subtareas"]):
        for i in tarea["subtareas"]:
            if i["estado"] == "terminada":
                print("listo")
            else:
                print("hay subtareas que no se han termiando")
                return tarea
        tarea["estado"] = "terminada"
        return tarea

    else:
        return tarea

# sirve para terminar las tareas
def terminartareas(tareas):
    try:
        id = int(input("ingresa la id de la tarea: "))
    except Exception:
        print("ingresa un numero")
        return tareas

    for i in range(len(tareas)):
        if tareas[i]["id_tarea"] == id:
            if any(tareas[i]["subtareas"]):
                tareas[i] = subtareasfinalizadas(tareas[i])
            else:
                tareas[i]["estado"] = "terminada"
    return tareas
    
    

tareas_registradas = cargar_datos_json("data_base/tereas_registradas.json")

tareas_registradas = terminartareas(tareas_registradas)

guardar_datos_json(tareas_registradas,"data_base/tereas_registradas.json")