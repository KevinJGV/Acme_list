import getpass
import re
import threading
import os
from colorama import init, Fore, Back, Style
from termcolor import colored

# Inicializar colorama
init(autoreset=True)

# Recibe únicamente números, repite cuando no se cumple


def solo_numeros(mensaje):
    while True:
        try:
            valido = int(campo_no_vacio(mensaje))

            if valido > 0:
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


# Recibe únicamente números en texto, repite cuando no se cumple
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


# No acepta que se dejen espacios, repite cuando no se cumple
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


# Valida que en los campos tenga información, sino repite cuando no se cumple
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


# Solo acepta texto y sin caracteres especiales
def solo_texto(mensaje):
    while True:

        patron = re.compile(r"[a-zA-ZáéíóúñÑ ]+$")

        valido = campo_no_vacio(mensaje)

        if patron.match(valido):
            return valido
        else:
            print("No se acepta números o caracteres especiales")

            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔══════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           No se acepta números o caracteres especiales          "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚══════════════════════════════════════╝"))
            #print("No se acepta números o caracteres especiales")
        

# Validación de correo electrónico
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


# Validación de contraseña mínima 8 caracteres
def contraseñavalida(mensaje):
    while True:

        contraseña = getpass.getpass(
            "\n(mínimo 8 caracteres, incluyendo mayúsculas, minúsculas y números)\n" + mensaje)

        if len(contraseña) < 8 or not re.search("[a-z]", contraseña) or not re.search("[A-Z]", contraseña) or not re.search("[0-9]", contraseña):
            print(
                "La contraseña debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas y números.")
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╔════════════════════════════════════════════════════════════════════════════════╗"))
            print("{:^160}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + " ║"+ Fore.WHITE +"           La contraseña debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas y números.          "+ Fore.CYAN +"║"))
            print("{:^150}".format(Back.BLACK + Fore.CYAN + Style.BRIGHT + "╚════════════════════════════════════════════════════════════════════════════════╝"))
            #print("La contraseña debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas y números.")
        else:
            return contraseña

# El nombre debe ser único


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


# Valida campos
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

# Generar un nuevo id


def generador_id(datos):

    lock = threading.Lock()

    with lock:
        if not datos:
            id = 1

            return id

        else:
            anterior_id = datos[-1]
            clave_id = next((clave for clave in anterior_id.keys()
                            if clave.startswith("id")), None)
            if clave_id:
                id_nuevo = anterior_id[clave_id] + 1
            else:
                raise KeyError("Ha existido un error")
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

# Imprime en pantalla las tareas que esten contenidas en la estructura json  diseñada para el programa, se puede usar facilmente con, por ejemplo, cruds.datos_registro


def imprimir_tabla_diccionario_lista(json_a_visualizar):
    # Obtener encabezados (claves únicas) de la lista de diccionarios
    json_tamaño = len(json_a_visualizar)
    encabezados = set()
    for diccionario in json_a_visualizar:
        encabezados.update(diccionario.keys())
        if "subtareas" in diccionario:
            for subtarea in diccionario["subtareas"]:
                encabezados.update(subtarea.keys())

    # Filtrar encabezados en el orden deseado
    desired_column_order = ["id_tarea", "titulo", "descripcion",
                            "estado", "prioridad", "fecha_limite", "subtareas"]
    encabezados_filtrados = [
        h for h in desired_column_order if h in encabezados]

    # Diccionario para reemplazar nombres de columnas
    header_replacements = {
        "id_tarea": "ID",
        "titulo": "TITULO",
        "descripcion": "DESCRIPCIÓN",
        "estado": "ESTADO",
        "prioridad": "PRIORIDAD",
        "fecha_limite": "FECHA LIMITE",
        "subtareas": "SUBTAREAS"
    }

    # Obtener ancho máximo para cada encabezado considerando clave y valor
    anchos_maximos = {}
    for encabezado in encabezados_filtrados:
        ancho_maximo_clave = 0
        ancho_maximo_valor = 0

        for diccionario in json_a_visualizar:
            if encabezado in diccionario and encabezado != "subtareas":
                valor = str(diccionario[encabezado])
                ancho_maximo_clave = max(ancho_maximo_clave, len(encabezado))
                ancho_maximo_valor = max(ancho_maximo_valor, len(valor))

            elif encabezado == "subtareas":
                # No se procesa la clave "subtareas" si no existe en las subtareas
                if "subtareas" in diccionario:
                    ancho_maximo_clave = max(
                        ancho_maximo_clave, len(encabezado))

                    for subtarea in diccionario["subtareas"]:
                        ancho_maximo_subtarea = 0
                        for atributo in subtarea:
                            valor_subtarea = str(subtarea[atributo])
                            ancho_maximo_subtarea = max(
                                ancho_maximo_subtarea, len(valor_subtarea))

                        ancho_maximo_valor = max(
                            ancho_maximo_valor, ancho_maximo_subtarea)

        anchos_maximos[encabezado] = max(
            ancho_maximo_clave, ancho_maximo_valor)

    # Asignar ancho máximo del encabezado a la columna "subtareas"
    anchos_maximos["subtareas"] = 9

    # Generar estructura de la tabla
    tabla_formateada = ""

    # Línea superior con encabezados centrados
    linea_encabezados = ""
    for encabezado, ancho_maximo in anchos_maximos.items():
        if json_tamaño != 0:
            linea_encabezados += f"| {header_replacements.get(encabezado, encabezado):^{ancho_maximo}} |"
        else:
            linea_encabezados += f"| ID | TITULO | DESCRIPCIÓN | ESTADO | PRIORIDAD | FECHA LIMITE | SUBTAREAS |"
    longitud_tabla = len(linea_encabezados)
    linea_encabezados = f"{'-' * (int(longitud_tabla))}\n" + linea_encabezados
    tabla_formateada += linea_encabezados + "\n"

    # Línea divisoria
    linea_divisoria = f"|{'=' * (int(longitud_tabla)-2)}|"
    tabla_formateada += linea_divisoria + "\n"

    # Líneas para cada fila del diccionario
    if json_tamaño != 0:
        for diccionario in json_a_visualizar:
            linea_fila = ""
            subtareas = ""
            for encabezado in encabezados_filtrados:
                valor = ""
                if encabezado in diccionario:
                    if encabezado == "estado":
                        valor = str(diccionario[encabezado]).capitalize()
                    elif encabezado == "prioridad":
                        valor = str(diccionario[encabezado]).upper()
                    elif encabezado != "subtareas":
                        valor = str(diccionario[encabezado])
                    else:
                        # Utilizar la función procesar_subtareas sin recursividad
                        valor = str(len(diccionario[encabezado]))
                        if len(diccionario["subtareas"]) > 0:
                            # Formatear texto de la línea divisoria
                            linea_taras_vacias = f"| {
                                'SUBTAREAS':^{longitud_tabla - 4}} |"

                            # Agregar línea divisoria a la tabla formateada
                            subtareas += linea_taras_vacias + "\n"

                            subtareas += procesar_subtareas(
                                diccionario["subtareas"], anchos_maximos)

                linea_fila += f"| {valor:<{anchos_maximos[encabezado]}} |"

            tabla_formateada += linea_fila + "\n"

            if subtareas != "":
                tabla_formateada += subtareas
                linea_divisoria = f"|{'-' * (int(longitud_tabla)-2)}|"
                tabla_formateada += linea_divisoria + "\n"
    else:
        linea_taras_vacias = f"| {'SIN TAREAS REGISTRADAS ACTUALMENTE ;)':^{longitud_tabla - 4}} |"
        tabla_formateada += linea_taras_vacias + "\n"
    linea_pie = f"{'-' * (int(longitud_tabla))}\n"
    tabla_formateada += linea_pie

    # Imprimir la tabla
    print(tabla_formateada)


# Funcion auxiliar de imprimir_tabla_diccionario_lista() que realiza el proceso de estructuracion para el print final
def procesar_subtareas(subtareas, anchos_maximos):
    encabezados = ['id_subtarea', 'titulo', 'descripcion',
                   'estado', 'prioridad', 'fecha_limite']
    subtareas_formateadas = ""
    for subtarea in subtareas:
        linea_subtarea = ""
        for encabezado in encabezados:
            if encabezado == "estado":
                valor_subtarea = str(subtarea[encabezado]).capitalize()
            elif encabezado == "prioridad":
                valor_subtarea = str(subtarea[encabezado]).upper()
            else:
                valor_subtarea = str(subtarea[encabezado])
            if encabezado == "id_subtarea":
                linea_subtarea += f"| {valor_subtarea:<{
                    anchos_maximos["id_tarea"]}} |"
            else:
                linea_subtarea += f"| {valor_subtarea:<{
                    anchos_maximos[encabezado]}} |"

        subtareas_formateadas += linea_subtarea + "\n"
    return subtareas_formateadas

datos = [
    {
        "id_tarea": 2,
        "id_usuario": 1,
        "titulo": "Gestionar archivos",
        "descripcion": "hacer un programa para gestionar archivos",
        "fecha_limite": "12/06/2024",
        "estado": "terminada",
        "prioridad": "alta",
        "subtareas": [
            {
                "id_subtarea": 1,
                "id_usuario": 1,
                "titulo": "Menú Principal",
                "descripcion": "hacer el menu principal",
                "fecha_limite": "05/06/2024",
                "estado": "terminada",
                "prioridad": "media"
            },
            {
                "id_subtarea": 2,
                "id_usuario": 1,
                "titulo": "Menú crud archivos",
                "descripcion": "el menu de gestion de archivos",
                "fecha_limite": "06/06/2024",
                "estado": "terminada",
                "prioridad": "alta"
            },
            {
                "id_subtarea": 3,
                "id_usuario": 1,
                "titulo": "Interfaz",
                "descripcion": "hacer la interfaz",
                "fecha_limite": "10/06/2024",
                "estado": "por hacer",
                "prioridad": "baja"
            }
        ]
    }
]

imprimir_tabla_diccionario_lista(datos)