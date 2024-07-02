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
tarea_cancelado = "data_base/tarea_canceladas.json"

#Guarda los datos de las tareas JSON  
datos_registro = cargar_datos_json(tarea_registro)
datos_en_curso = cargar_datos_json(tarea_en_curso)
datos_terminado = cargar_datos_json(tarea_terminado)


#Crea una nueva tarea
def crea_tarea(id_usuario, tarea:dict):
    
    try:

        id_tarea = funciones.generador_id(tarea)

        task_data = {
            "id_tarea": id_tarea,
            "id_usuario": id_usuario,
            **tarea 
        }

        datos_registro.append(task_data)

        guardar_datos_json(datos_registro, tarea_registro)

        return f"Tarea creada con éxito."
    
    except Exception as e:
        print(f"Error al crear la tarea: {e}")
        return "Error al crear la tarea."


#Modifica una tarea
def modifica_tarea(id_tarea, tarea:dict):
    
    try:

        indice_registro = funciones.valida_campos("id_tarea", id_tarea, datos_registro, True)
        indice_en_curso = funciones.valida_campos("id_tarea", id_tarea, datos_en_curso, True)
        indice_terminado = funciones.valida_campos("id_tarea", id_tarea, datos_terminado, True)

        if indice_registro is False and indice_en_curso is False and indice_terminado is False:
            return "Tarea no encontrada."
        

        if indice_registro is not False:

            datos_registro[indice_registro] = tarea

            guardar_datos_json(datos_registro, tarea_registro)

        
        if indice_en_curso is not False:

            datos_en_curso[indice_en_curso] = tarea

            guardar_datos_json(datos_en_curso, tarea_en_curso)


        if indice_terminado is not False:

            datos_terminado[indice_terminado] = tarea

            guardar_datos_json(datos_terminado, tarea_terminado)

        return "Tarea modificada con éxito."

    except Exception as e:
        print(f"Error al modificar la tarea: {e}")
        return "Error al modificar la tarea."


#Crea una nueva subtarea
def crea_subtarea(id_tarea, subtarea:dict):
    
    try:

        tarea = funciones.valida_campos("id_tarea", id_tarea, datos_registro, True)

        if tarea is False:
            return "Tarea no encontrada"
        else:

            id_subtarea = funciones.generador_id(subtarea)

            subtask_data = {
                "id_subtarea": id_subtarea,
                **subtarea 
            }

            tarea["subtareas"].append(subtask_data)

            datos_registro[tarea] = tarea

            guardar_datos_json(datos_registro, tarea_registro)

            return f"subtarea creada con éxito."
    
    except Exception as e:
        print(f"Error al crear la subtarea: {e}")
        return "Error al crear la subtarea."


#Modifica una subtarea
def modifica_tarea(id_tarea, id_subtarea, subtarea:dict):
    try:
        
        indice_tarea_registro = funciones.valida_campos("id_tarea", id_tarea, datos_registro, True)
        indice_tarea_en_curso = funciones.valida_campos("id_tarea", id_tarea, datos_en_curso, True)
        indice_tarea_terminado = funciones.valida_campos("id_tarea", id_tarea, datos_terminado, True)

        if indice_tarea_registro is False and indice_tarea_en_curso is False and indice_tarea_terminado is False:
            return "Tarea no encontrada."

        if indice_tarea_registro is not False:
            indice_subtarea = funciones.valida_campos("id_subtarea", id_subtarea, datos_registro[indice_tarea_registro]["subtareas"], True)

            datos_registro[indice_tarea_registro]["subtareas"][indice_subtarea] = subtarea

            guardar_datos_json(datos_registro, tarea_registro)

        if indice_tarea_en_curso is not False:
            indice_subtarea = funciones.valida_campos("id_subtarea", id_subtarea, datos_registro[indice_tarea_en_curso]["subtareas"], True)

            datos_en_curso[indice_tarea_en_curso]["subtareas"][indice_subtarea] = subtarea

            guardar_datos_json(datos_en_curso, tarea_en_curso)


        if indice_tarea_terminado is False:
            indice_subtarea = funciones.valida_campos("id_subtarea", id_subtarea, datos_registro[indice_tarea_terminado]["subtareas"], True)

            datos_terminado[indice_tarea_terminado]["subtareas"][indice_subtarea] = subtarea

            guardar_datos_json(datos_terminado, tarea_terminado)
        
        return "Subtarea modificada con éxito."

    except Exception as e:
        print(f"Error al modificar la subtarea: {e}")
        return "Error al modificar la subtarea."


#Cambia el estado de la tarea / subtarea
def estado(id, estado, tarea=True):
    try:
        if tarea:
        # Buscar la tarea 
            indice_tarea_registro = funciones.valida_campos("id_tarea", id, datos_registro, True)
            indice_tarea_en_curso = funciones.valida_campos("id_tarea", id, datos_en_curso, True)
            indice_tarea_terminado = funciones.valida_campos("id_tarea", id, datos_terminado, True)
            

            if indice_tarea_registro is False and indice_tarea_en_curso is False and indice_tarea_terminado is False:
                return "Tarea no encontrada."
            
            if indice_tarea_registro is not False:
                datos_registro[indice_tarea_registro]["estado"] = estado
                guardar_datos_json(datos_registro, tarea_registro)

            if indice_tarea_en_curso is not False:
                datos_en_curso[indice_tarea_en_curso]["estado"] = estado
                guardar_datos_json(datos_en_curso, tarea_en_curso)

            if indice_tarea_terminado is not False:
                datos_terminado[indice_tarea_terminado]["estado"] = estado
                guardar_datos_json(datos_terminado, tarea_terminado)
            
            return "Estado de la tarea modificado con éxito."


            indice_subtarea = funciones.valida_campos("id_subtarea", id, datos_registro[indice_tarea]["subtareas"], True)
            if indice_subtarea is False:
                return "Subtarea no encontrada."

            # Actualizar el estado de la subtarea
            datos_registro[indice_tarea]["subtareas"][indice_subtarea]["estado"] = estado
            return "Estado de la subtarea modificado con éxito."

        else:
            # Buscar la subtarea
            indice_tarea_registro = funciones.valida_campos("id_tarea", id, datos_registro, True)
            indice_tarea_en_curso = funciones.valida_campos("id_tarea", id, datos_en_curso, True)
            indice_tarea_terminado = funciones.valida_campos("id_tarea", id, datos_terminado, True)
            

            if indice_tarea_registro is False and indice_tarea_en_curso is False and indice_tarea_terminado is False:
                return "Tarea no encontrada."
            
            if indice_tarea_registro is not False:
                datos_registro[indice_tarea_registro]["estado"] = estado

                
                guardar_datos_json(datos_registro, tarea_registro)

            if indice_tarea_en_curso is not False:
                datos_en_curso[indice_tarea_en_curso]["estado"] = estado
                guardar_datos_json(datos_en_curso, tarea_en_curso)

            if indice_tarea_terminado is not False:
                datos_terminado[indice_tarea_terminado]["estado"] = estado
                guardar_datos_json(datos_terminado, tarea_terminado)
            
            return "Estado de la tarea modificado con éxito."

            # Actualizar el estado de la tarea
            datos_registro[indice_tarea]["estado"] = estado
            return "Estado de la tarea modificado con éxito."

    except Exception as e:
        print(f"Error al modificar el estado: {e}")
        return "Error al modificar el estado."


# esta funcion sirve para indicar si una tarea tiene subtareas o no
# y si tiene subtareas verificar si estan todas terminadas y poner la tarea en terminada
def subtareasfinalizadas(tarea):
    if any(tarea["subtareas"]):
        for i in tarea["subtareas"]:
            if i["estado"] == "terminado":
                print("listo")
            else:
                print("hay subtareas que no se han terminado")
                return tarea
        tarea["estado"] = "terminado"
        return tarea

    else:
        return tarea


# sirve para terminar las tareas
def terminartareas(id, tareas):
    for i in range(len(tareas)):
        if tareas[i]["id_tarea"] == id:
            if any(tareas[i]["subtareas"]):
                tareas[i] = subtareasfinalizadas(tareas[i])
            else:
                tareas[i]["estado"] = "terminado"
    return tareas