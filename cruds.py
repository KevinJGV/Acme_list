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

