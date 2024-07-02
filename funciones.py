import getpass
import re
import threading
import os
from colorama import init, Fore, Back, Style
from termcolor import colored

# Inicializar colorama
init(autoreset=True)

#Recibe únicamente números, repite cuando no se cumple
def solo_numeros(mensaje):
    while True:
        try:
            valido = int(campo_no_vacio(mensaje))

            if valido >0:
                return valido
            else:
                print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
                print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           Debes digitar solo números positivos          "+ Fore.CYAN +"║"))
                print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
                #print("Debes digitar solo números positivos")

        except Exception as e:
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           Debes digitar un número entero          "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            #print("Debes digitar un número entero")


#Recibe únicamente números en texto, repite cuando no se cumple
def solo_numeros_texto(mensaje):
    while True:
        valido = campo_no_vacio(mensaje)

        if valido.isdigit():
            return valido
        else:
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           Digita unicamente números          "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            #print("Digita unicamente números")


#No acepta que se dejen espacios, repite cuando no se cumple
def sin_espacios(mensaje):
    while True:
        
        valido = campo_no_vacio(mensaje)

        if ' ' in valido:
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           Debes digitar información sin espacios          "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            #print("Debes digitar información sin espacios")
        else:
            return valido


#Valida que en los campos tenga información, sino repite cuando no se cumple
def campo_no_vacio(mensaje):

    while True:

        valido = input(mensaje)

        if valido.strip():
            return valido
        else:
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           No puedes omitir sin acceder información requerida          "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            #print("No puedes omitir sin acceder información requerida")


#Solo acepta texto y sin caracteres especiales
def solo_texto(mensaje):
    while True:

        patron = re.compile(r"[a-zA-ZáéíóúñÑ ]+$")

        valido = campo_no_vacio(mensaje)

        if patron.match(valido):
            return valido
        else:
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           No se acepta números o caracteres especiales          "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            #print("No se acepta números o caracteres especiales")
        

#Validación de correo electrónico
def solo_correo(mensaje):
    while True:

        correo = campo_no_vacio(mensaje)
        
        if not re.match(r"[^@]+@[^@]+\.[a-z]{2,}", correo):
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           Correo electrónico no válido.          "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            #print("Correo electrónico no válido.")
        else:
            return correo


#Validación de contraseña mínima 8 caracteres
def contraseñavalida(mensaje):
    while True:
        
        contraseña = getpass.getpass("\n(mínimo 8 caracteres, incluyendo mayúsculas, minúsculas y números)\n"+ mensaje)

        if len(contraseña) < 8 or not re.search("[a-z]", contraseña) or not re.search("[A-Z]", contraseña) or not re.search("[0-9]", contraseña):
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔════════════════════════════════════════════════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           La contraseña debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas y números.          "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚════════════════════════════════════════════════════════════════════════════════╝"))
            #print("La contraseña debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas y números.")
        else:
            return contraseña
        
#El nombre debe ser único
def unico_nombre(mensaje, datos):
    while True:
        nombre_unico = True

        nombre = solo_texto(mensaje)

        for usuario in datos:
            if usuario["nombre"] == nombre:
                print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
                print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           Nombre existente.          "+ Fore.CYAN +"║"))
                print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
                #print("Nombre existente")
                nombre_unico = False

        if nombre_unico:
            return nombre
        

#Valida campos
def valida_campos(key, valor, datos, opcion=False):
    
    if opcion is False:
        for campo in datos:
            if campo[key] == valor:
                return True
    else:
        for campo in datos:
            if campo[key] == valor:
                return campo
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
        print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           No existe campos.          "+ Fore.CYAN +"║"))
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
        #print("No existe campos")
    return False

#Generar un nuevo id
def generador_id(datos):

  lock = threading.Lock()

  with lock:
    if not datos:
      id = 1

      return id

    else:
      anterior_id = datos[-1]
      clave_id = next((clave for clave in anterior_id.keys() if clave.startswith("id")), None)
      if clave_id:
        id_nuevo = anterior_id[clave_id] + 1
      else:
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
        print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           Ha existido un error.          "+ Fore.CYAN +"║"))
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
        raise KeyError("Ha existido un error")

      return id_nuevo  
    