import signin
import signup
import cruds
import filters
import funciones
import os
from colorama import init, Fore, Back, Style
from termcolor import colored

usuario = "data_base/informacion_usuarios.json"
tareas_por_hacer = "data_base/tareas_registrar.json"

datos = cruds.cargar_datos_json(usuario)
datos_hacer = cruds.cargar_datos_json(tareas_por_hacer)
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
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 1. " + Fore.WHITE + "Nombre                            " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 2. " + Fore.WHITE + "Correo                        " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 3. " + Fore.WHITE + "Contraseña                            " + Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))




def menu_central():
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
    print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║            "+ Fore.WHITE +"Bienvenida                 "+ Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╠══════════════════════════════════════╣"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 1. " + Fore.WHITE + "Completar Tarea                       " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 2. " + Fore.WHITE + "Crear tarea nueva                             " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 3. " + Fore.WHITE + "Editar tarea                             " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 4. " + Fore.WHITE + "Filtrar tareas                             " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 5. " + Fore.WHITE + "Cerrar sesion                             " + Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))

def crear_tarea():
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
    print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║            "+ Fore.WHITE +"Tarea Nueva                 "+ Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╠══════════════════════════════════════╣"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 1. " + Fore.WHITE + "Titulo                    " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 2. " + Fore.WHITE + "Descripcion                       " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 3. " + Fore.WHITE + "Fecha_limite                           " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 4. " + Fore.WHITE + "Estado                            " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 5. " + Fore.WHITE + "Prioridad                             " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 6. " + Fore.WHITE + "Sub Tareas                             " + Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))

def menu_EditarTarea():
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
    print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║            "+ Fore.WHITE +"Editar Tarea                 "+ Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╠══════════════════════════════════════╣"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 1. " + Fore.WHITE + "Nueva Descripcion                    " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 2. " + Fore.WHITE + "Nueva Fecha objetivo / vencido                       " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 3. " + Fore.WHITE + "Nueva Recordatorio  opcional                           " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 4. " + Fore.WHITE + "Nueva Nivel de prioridad (alta, normal, baja)                            " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + " 5. " + Fore.WHITE + "Nueva Subtareas opcional                             " + Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))

def menu_Filtros():
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
    print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║            "+ Fore.WHITE +"Filtros          "+ Fore.CYAN + "║"))
    print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╠══════════════════════════════════════╣"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 1. " + Fore.WHITE + "Eventos pendientes                            " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 2. " + Fore.WHITE + "Eventos realizados                        " + Fore.CYAN + "║"))
    print("{:^165}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║" + Fore.YELLOW + " 3. " + Fore.WHITE + "Por prioridad                            " + Fore.CYAN + "║"))
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
            correo=funciones.solo_correo("                                                    Correo:")
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            contraseña=funciones.contraseñavalida("                                                    Contraseña:")
            user={
                "correo":correo, 
                "contraseña":contraseña
            }
            inicio = signin.iniciar_sesion(user)
            if inicio: 
                print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Bienvenido:          "+ Fore.CYAN +"║"))
                menu_central()
            else:
                print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           La contraseña es incorrecta.          "+ Fore.CYAN +"║"))
                menu_principal()
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
    if op == 2:
        while True:
            menu_Registro()
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            nombre=funciones.unico_nombre("                                                    Nombre:", datos)
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            correo=funciones.solo_correo("                                                    Correo:")
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            contraseña=funciones.contraseñavalida("                                                    Contraseña:")
            user={
                "correo":correo, 
                "contraseña":contraseña,
                "nombre":nombre
            }
            signup.crear_usuario(user)
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Bienvenido:          "+ Fore.CYAN +"║"))
            print(menu_central())
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))

def op_menu_central():
    while True:
        menu_central()
        op = pedir_opcion()
        if op == 5:
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "║"+ Fore.WHITE +"                  ADIOS!              "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            break
        if op == 1:
            print("hola")
        if op == 2:
            titulo=funciones.unico_nombre("                                                    Titulo:", datos)
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            descripcion=funciones.unico_nombre("                                                    Descripcion:", datos)
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            fechalimite=funciones.unico_nombre("                                                    Fecha_limite:", datos)
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion:          "+ Fore.CYAN +"║"))
            prioridad=funciones.unico_nombre("                                                    Prioridad:", datos)
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"          Ingrese su opcion 1. Alto 2. Medio 3. Bajo:          "+ Fore.CYAN +"║"))
            