import cruds
import threading
import funciones

# Aquí va la direccion del archivo
archivo = "data_base/informacion_usuarios.json"

#Guarda los datos de usuarios del JSON para implementar 
datos = cruds.cargar_datos_json(archivo)


#Crear usuario
def crear_usuario(user:dict):

    try:

        id_usuario = funciones.generador_id(datos)

        username = generar_username(user["nombre"], id_usuario)

        user_data = {
            "id": id_usuario,
            "usuario": username,
            **user  
        }

        datos.append(user_data)

        cruds.guardar_datos_json(datos, archivo)

        return f"Usuario creado con éxito. Su username es: {username}"
    
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return "Error al crear usuario."


#Generar username a partir las iniciales 
def generar_username(nombre, id):
  
  nombre_minúsculas = nombre.lower()

  palabras = nombre_minúsculas.split(" ")

  iniciales = []

  for palabra in palabras:

    if palabra:
      iniciales.append(palabra[:2])

  iniciales_unidas = "".join(iniciales)

  username = iniciales_unidas + str(id)

  return username
