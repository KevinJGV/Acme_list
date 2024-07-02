import funciones
import json

# cargar los datos de un archivo json
# en el parametro de ruta se pone la ruta relativa del archivo json que se quiere leer
def cargar_datos_json(ruta):
    datos = {}
    file = open(ruta,"r",encoding="utf-8")
    datos = json.load(file)
    return datos

# guardar los datos en un archivo json
# en el parametro de ruta se pone la ruta relativa del archivo json que se quiere leer
# en el parametro datos se pone los datos que se van a agregar
# al agregar los datos utilizar el mismo contenido del archivo antes de modificar + los cambios que se le alla hecho por medio de na variable
def guardar_datos_json(datos, ruta):
    datos = list(datos)
    diccionario = json.dumps(datos,ensure_ascii=True, indent=4)
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
datos_cancelado = cargar_datos_json(tarea_cancelado)


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


#Búsqueda de la tarea
def traer_tarea(id_tarea):

    indice_registro = funciones.valida_campos("id_tarea", id_tarea, datos_registro, True)
    indice_en_curso = funciones.valida_campos("id_tarea", id_tarea, datos_en_curso, True)
    indice_terminado = funciones.valida_campos("id_tarea", id_tarea, datos_terminado, True)
    indice_cancelado = funciones.valida_campos("id_tarea", id_tarea, datos_cancelado, True)

    if indice_registro is False and indice_en_curso is False and indice_terminado is False and indice_cancelado is False:
        return "Tarea no encontrada."
        

    if indice_registro is not False:

        return indice_registro

        
    if indice_en_curso is not False:

        return indice_en_curso


    if indice_terminado is not False:

        return indice_terminado


    if indice_cancelado is not False:
            
        return indice_cancelado


#Modifica una tarea
def modifica_tarea(id_tarea, tarea:dict):
    
    try:

        indice = traer_tarea(id_tarea)

        if indice is False:
            return "Tarea no existe"
        
        if indice["estado"] == "por hacer":
        
            datos_registro[indice] = tarea

            guardar_datos_json(datos_registro, tarea_registro)

        if indice["estado"] == "en curso":

            datos_en_curso[indice] = tarea

            guardar_datos_json(datos_en_curso, tarea_en_curso)

        if indice["estado"] == "terminado":

            datos_terminado[indice] = tarea

            guardar_datos_json(datos_terminado, tarea_terminado)

        if indice["estado"] == "cancelado":

            datos_cancelado[indice] = tarea

            guardar_datos_json(datos_cancelado, tarea_cancelado)
            

        return "Tarea modificada con éxito."

    except Exception as e:
        print(f"Error al modificar la tarea: {e}")
        return "Error al modificar la tarea."


#Lista de Tareas por hacer
def lista_tareas_registro():
    return datos_registro


#Lista de Tareas en curso
def lista_tareas_en_curso():
    return datos_en_curso


#Lista de Tareas terminadas
def lista_tareas_terminado():
    return datos_terminado


#Lista de Tareas canceladas
def lista_tareas_cancelado():
    return datos_cancelado


#Lista de Tareas
def lista_tareas():
    lista_combinada = []
    lista_combinada.extend(lista_tareas_registro())
    lista_combinada.extend(lista_tareas_en_curso())
    lista_combinada.extend(lista_tareas_terminado())
    lista_combinada.extend(lista_tareas_cancelado())
    return lista_combinada


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


#Trae la subtarea de la tarea
def trae_subtarea(id_tarea, id_subarea):
    
    tarea = traer_tarea(id_tarea)

    if tarea is False:
        return "No existe la tarea"
    
    subtarea = funciones.valida_campos("id_subtarea", id_subarea, tarea["subtarea"], True)

    if subtarea is False:
        return "No existe la subtarea"
    
    return subtarea


#Trae todas las subtareas de la Tarea
def lista_subtareas(id_tarea):

    tarea = traer_tarea(id_tarea)

    if tarea is False:
        return "No existe la tarea"
    
    if tarea["subtarea"]:
        for subtarea in tarea["subtarea"]:
            print(subtarea)
    else:
        print("La tarea no tiene subtareas")
    

#Modifica una subtarea
def modifica_tarea(id_tarea, id_subtarea, subtarea:dict):

    try:

        indice_tarea = traer_tarea(id_tarea)

        if indice_tarea is False:
            return "No existe Tarea" 

        indice_subtarea = trae_subtarea(id_tarea, id_subtarea)

        if indice_subtarea is False:
            return "No existe la subtarea"


        if indice_tarea["estado"] == "por hacer":

            datos_registro[indice_tarea]["subtareas"][indice_subtarea] = subtarea

            guardar_datos_json(datos_registro, tarea_registro)


        if indice_tarea["estado"] == "en curso":

            datos_en_curso[indice_tarea]["subtareas"][indice_subtarea] = subtarea

            guardar_datos_json(datos_en_curso, tarea_en_curso)

        if indice_tarea["estado"] == "terminado":

            datos_terminado[indice_tarea]["subtareas"][indice_subtarea] = subtarea

            guardar_datos_json(datos_terminado, tarea_terminado)

        if indice_tarea["estado"] == "cancelado":

            datos_cancelado[indice_tarea]["subtareas"][indice_subtarea] = subtarea

            guardar_datos_json(datos_cancelado, tarea_cancelado)

        return "Subtarea modificada con éxito."

    except Exception as e:
        print(f"Error al modificar la subtarea: {e}")
        return "Error al modificar la subtarea."


#Cambia el estado de la tarea | subtarea
def estado(id_tarea, estado, tarea = True, id_subtarea = 0):
    try:

        indice_tarea = traer_tarea(id_tarea)

        if indice_tarea is False:
            return "No existe tarea"
        
        if tarea:

            if tarea["estado"] == estado:
                return "No existe cambios"
            
            if  estado == "por hacer":

                id_nuevo = funciones.generador_id(datos_registro)
                        
                indice_tarea["id_tarea"] = id_nuevo
                indice_tarea["estado"] = estado

                del datos_registro[indice_tarea]

                datos_registro.append(indice_tarea)
                guardar_datos_json(datos_registro, tarea_registro)

            if  estado == "en curso":

                id_nuevo = funciones.generador_id(datos_en_curso)
                        
                indice_tarea["id_tarea"] = id_nuevo
                indice_tarea["estado"] = estado

                del datos_en_curso[indice_tarea]

                datos_en_curso.append(indice_tarea)
                guardar_datos_json(datos_en_curso, tarea_en_curso)

            if  estado == "terminado":

                id_nuevo = funciones.generador_id(datos_terminado)
                        
                indice_tarea["id_tarea"] = id_nuevo
                indice_tarea["estado"] = estado

                del datos_terminado[indice_tarea]

                datos_terminado.append(indice_tarea)
                guardar_datos_json(datos_terminado, tarea_terminado)

            if  estado == "cancelado":

                id_nuevo = funciones.generador_id(datos_cancelado)
                        
                indice_tarea["id_tarea"] = id_nuevo
                indice_tarea["estado"] = estado

                del datos_cancelado[indice_tarea]

                datos_cancelado.append(indice_tarea)
                guardar_datos_json(datos_cancelado, tarea_cancelado)

            return "Estado de Tarea exitoso"

        elif tarea is False and id_subtarea > 0:

            indice_subtarea = trae_subtarea(id_tarea, id_subtarea)

            if indice_subtarea is False:
                return "No existe la subtarea"
            
            if indice_subtarea["estado"] == estado:
                return "No existen cambios"
            else:

                if indice_tarea["estado"] == "por hacer":

                    datos_registro[indice_tarea]["subtareas"][indice_subtarea]["estado"] = estado

                    guardar_datos_json(datos_registro, tarea_registro)

                if indice_tarea["estado"] == "en curso":

                    datos_en_curso[indice_tarea]["subtareas"][indice_subtarea]["estado"] = estado

                    guardar_datos_json(datos_en_curso, tarea_en_curso)
                
                if indice_tarea["estado"] == "terminado":

                    datos_terminado[indice_tarea]["subtareas"][indice_subtarea]["estado"] = estado

                    guardar_datos_json(datos_terminado, tarea_terminado)

                if indice_tarea["estado"] == "cancelado":

                    datos_cancelado[indice_tarea]["subtareas"][indice_subtarea]["estado"] = estado

                    guardar_datos_json(datos_cancelado, tarea_cancelado)

                return "Estado de Subtarea exitoso"
        
        else:
            return "Se ha generado un Error"
           
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