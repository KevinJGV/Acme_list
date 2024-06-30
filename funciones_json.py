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

""" print(cargar_datos_json("./data_base/informacion_usuarios.json")) """