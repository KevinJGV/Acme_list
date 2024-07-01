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