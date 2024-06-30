import getpass
import re 

#Recibe únicamente números, repite cuando no se cumple
def solo_numeros(mensaje):
    while True:
        try:
            valido = int(campo_no_vacio(mensaje))

            if valido >0:
                return valido
            else:
                print("Debes digitar solo números positivos")

        except Exception as e:
            print("Debes digitar un número entero")


#Recibe únicamente números en texto, repite cuando no se cumple
def solo_numeros_texto(mensaje):
    while True:
        valido = campo_no_vacio(mensaje)

        if valido.isdigit():
            return valido
        else:
            print("Digita unicamente números")


#No acepta que se dejen espacios, repite cuando no se cumple
def sin_espacios(mensaje):
    while True:
        
        valido = campo_no_vacio(mensaje)

        if ' ' in valido:
            print("Debes digitar información sin espacios")
        else:
            return valido


#Valida que en los campos tenga información, sino repite cuando no se cumple
def campo_no_vacio(mensaje):

    while True:

        valido = input(mensaje)

        if valido.strip():
            return valido
        else:
            print("No puedes omitir sin acceder información requerida")


#Solo acepta texto y sin caracteres especiales
def solo_texto(mensaje):
    while True:

        patron = re.compile(r"[a-zA-ZáéíóúñÑ ]+$")

        valido = campo_no_vacio(mensaje)

        if patron.match(valido):
            return valido
        else:
            print("No se acepta números o caracteres especiales")
        

#Validación de correo electrónico
def solo_correo(mensaje):
    while True:

        correo = campo_no_vacio(mensaje)
        
        if not re.match(r"[^@]+@[^@]+\.[a-z]{2,}", correo):
            print("Correo electrónico no válido.")
        else:
            return correo


#Validación de contraseña mínima 8 caracteres
def contraseñavalida(mensaje):
    while True:
        
        contraseña = getpass.getpass("\n(mínimo 8 caracteres, incluyendo mayúsculas, minúsculas y números)\n"+ mensaje)

        if len(contraseña) < 8 or not re.search("[a-z]", contraseña) or not re.search("[A-Z]", contraseña) or not re.search("[0-9]", contraseña):
            print("La contraseña debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas y números.")
        else:
            return contraseña
        
#El nombre debe ser único
def unico_nombre(mensaje, datos):
    while True:
        nombre_unico = True

        nombre = solo_texto(mensaje)

        for usuario in datos:
            if usuario["nombre"] == nombre:
                print("Nombre existente")
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
        print("No existe campos")
    return False
                