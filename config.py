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
