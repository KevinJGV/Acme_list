import funciones
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

# Aquí va la direccion de los archivos que se realizan CRUD
tarea_registro = "data_base/tareas_registradas.json"
tarea_en_curso = "data_base/tareas_en_curso.json"
tarea_terminado = "data_base/tareas_terminadas.json"
usuario = "data_base/informacion_usuarios.json"

#Guarda los datos de las tareas JSON  
datos_regitro = cargar_datos_json(tarea_registro)
datos_en_curso = cargar_datos_json(tarea_en_curso)
datos_terminado = cargar_datos_json(tarea_terminado)
datos_usuario = cargar_datos_json(usuario)


#Crea una nueva tarea
def crea_tarea(id_usuario, tarea:dict):
    
    try:

        id_tarea = funciones.generador_id(tarea)

        task_data = {
            "id_tarea": id_tarea,
            "id_usuario": id_usuario,
            **tarea 
        }

        datos_regitro.append(task_data)

        guardar_datos_json(datos_regitro, tarea_registro)

        return f"Tarea creada con éxito."
    
    except Exception as e:
        print(f"Error al crear la tarea: {e}")
        return "Error al crear la tarea."


#Modifica una tarea
def modifica_tarea(id_tarea, tarea:dict):
    
    try:

        indice_registro = funciones.valida_campos("id_tarea", id_tarea, datos_regitro, True)
        indice_en_curso = funciones.valida_campos("id_tarea", id_tarea, datos_en_curso, True)
        indice_terminado = funciones.valida_campos("id_tarea", id_tarea, datos_terminado, True)

        if indice_registro is False and indice_en_curso is False and indice_terminado is False:
            return "Tarea no encontrada."
        

        if indice_registro is not False:

            datos_regitro[indice_registro] = tarea

        
        if indice_en_curso is not False:

            datos_en_curso[indice_en_curso] = tarea


        if indice_terminado is not False:

            datos_terminado[indice_terminado] = tarea

        return "Tarea modificada con éxito."

    except Exception as e:
        print(f"Error al modificar la tarea: {e}")
        return "Error al modificar la tarea."


#Crea una nueva subtarea
def crea_subtarea(id_tarea, subtarea:dict):
    
    try:

        tarea = funciones.valida_campos("id_tarea", id_tarea, datos_regitro, True)

        if tarea is False:
            return "Tarea no encontrada"
        else:

            id_subtarea = funciones.generador_id(subtarea)

            subtask_data = {
                "id_subtarea": id_subtarea,
                **subtarea 
            }

            subtarea["subtareas"].append(subtask_data)

            return f"subtarea creada con éxito."
    
    except Exception as e:
        print(f"Error al crear la subtarea: {e}")
        return "Error al crear la subtarea."


#Modifica una subtarea
def modifica_tarea(id_tarea, id_subtarea, subtarea:dict):
    print()


#Cambia el estado de la tarea / subtarea
def estado(id, dato:dict, tarea=False):
    print()


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