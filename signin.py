import config
import funciones

# Aquí va la direccion del archivo
archivo = "usuario.json"

#Guarda los datos de usuarios del JSON para implementar 
datos = config.cargar_datos(archivo)


#Iniciar sesion
def iniciar_sesion(user:dict):
    
    inicia_sesion = funciones.valida_campos("usuario", user["usuario"], datos, True)
    
    if inicia_sesion is False:
        return inicia_sesion
    else:
        return valida_sesion(inicia_sesion, user["contrasena"])
    

#Validación de la sesion antes de iniciar sesión y que cumpla los requisitos
def valida_sesion(user:dict, contrasena):
    return funciones.valida_campos("contrasena", contrasena, user)