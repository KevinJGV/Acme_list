import json
import threading
import os
from colorama import init, Fore, Back, Style
from termcolor import colored

# Inicializar colorama
init(autoreset=True)

#Cargar los datos del archivo JSON a un Dict
def cargar_datos(archivo):
    try:
        datos = {}
        with open(archivo,"r") as file:
            datos=json.load(file)
        return datos
    except Exception:
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
        print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           Error durante la ejecución. Revisar el log de errores.          "+ Fore.CYAN +"║"))
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
        #print("Error durante la ejecución. Revisar el log de errores.")
        
        
#Guardar los nuevos datos del al archivo JSON
def guardar_datos(datos:dict, archivo):
    try:
        diccionario=json.dumps(datos, indent=4)
        file=open(archivo,"w")
        file.write(diccionario)
        file.close()
    except Exception:
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
        print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           Error durante la ejecución. Revisar el log de errores.          "+ Fore.CYAN +"║"))
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
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