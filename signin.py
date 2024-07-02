
import cruds
import funciones

# Aquí va la direccion del archivo
archivo = "data_base/informacion_usuarios.json"

#Guarda los datos de usuarios del JSON para implementar 
datos = cruds.cargar_datos_json(archivo)


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