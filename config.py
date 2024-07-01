import json
import threading

#Cargar los datos del archivo JSON a un Dict
def cargar_datos(archivo):
    try:
        datos = {}
        with open(archivo,"r") as file:
            datos=json.load(file)
        return datos
    except Exception:
        print("Error durante la ejecución. Revisar el log de errores.")
        
        
#Guardar los nuevos datos del al archivo JSON
def guardar_datos(datos:dict, archivo):
    try:
        diccionario=json.dumps(datos, indent=4)
        file=open(archivo,"w")
        file.write(diccionario)
        file.close()
    except Exception:
        print("Error durante la ejecución. Revisar el log de errores.")


#Generar un nuevo id
def generador_id(datos):

  lock = threading.Lock()

  with lock:
    if not datos:
      id = 1

      return id

    else:
      anterior_id = datos[-1]
      nuevoid = anterior_id["id"] + 1

    return nuevoid