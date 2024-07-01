# Seccion para importar rutas
import signin
import cruds
import filters
import os
from colorama import init, Fore, Back, Style
from termcolor import colored

# Inicializar colorama
init(autoreset=True)


def menu_principal():
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
    print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║            "+ Fore.WHITE +"ACME-list                 "+ Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╠══════════════════════════════════════╣"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 1. " + Fore.WHITE + "Iniciar Sesion                    " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 2. " + Fore.WHITE + "Registrarse                       " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 3. " + Fore.WHITE + "Salir                             " + Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
    
def menu_Inicio_Sesion():
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
    print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║            "+ Fore.WHITE +"Inicio de Sesion          "+ Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╠══════════════════════════════════════╣"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 1. " + Fore.WHITE + "Correo                            " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 2. " + Fore.WHITE + "Contraseña                        " + Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))

def menu_Registro():
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
    print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║            "+ Fore.WHITE +"Registro          "+ Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╠══════════════════════════════════════╣"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 1. " + Fore.WHITE + "Correo                            " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 2. " + Fore.WHITE + "Contraseña                        " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 3. " + Fore.WHITE + "Nombre                            " + Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))

def pedir_opcion():
    try:
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
        print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
        op = int(input("                                                                  "))
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
    
        
        return op
    except Exception:
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
        print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           OPCION NO VALIDA!          "+ Fore.CYAN +"║"))
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))




while True:
    menu_principal()
    op = pedir_opcion()
    
    if op == 3:
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
        print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║"+ Fore.WHITE +"                  ADIOS!              "+ Fore.CYAN +"║"))
        print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
        break
    if op == 1:
        while True:
            menu_Inicio_Sesion()
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            op = int(input("                                                    Correo:"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            op = int(input("                                                    Contraseña:"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
    if op == 2:
        while True:
            menu_Registro()
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            op = int(input("                                                    Correo:"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            op = int(input("                                                    Contraseña:"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            op = int(input("                                                    Nombre:"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
                