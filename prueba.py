from datetime import datetime
import cruds
import textwrap

def imprimir_tabla_diccionario_lista(lista_diccionarios):
    # Obtener encabezados (claves únicas) de la lista de diccionarios
    encabezados = set()
    for diccionario in lista_diccionarios:
        encabezados.update(diccionario.keys())
        if "subtareas" in diccionario:
            for subtarea in diccionario["subtareas"]:
                encabezados.update(subtarea.keys())

    # Filtrar encabezados en el orden deseado
    desired_column_order = ["id_tarea", "titulo", "descripcion", "estado", "prioridad", "fecha_limite", "subtareas"]
    encabezados_filtrados = [h for h in desired_column_order if h in encabezados]

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
        for diccionario in lista_diccionarios:
            if encabezado in diccionario and encabezado != "subtareas":
                valor = str(diccionario[encabezado])
                ancho_maximo_clave = max(ancho_maximo_clave, len(encabezado))
                ancho_maximo_valor = max(ancho_maximo_valor, len(valor))

            else:
                ancho_maximo_clave = len(encabezado)
                ancho_maximo_valor = len(diccionario['subtareas'])

        anchos_maximos[encabezado] = max(ancho_maximo_clave, ancho_maximo_valor)

    # Generar estructura de la tabla
    tabla_formateada = ""

    # Línea superior con encabezados centrados
    linea_encabezados = ""
    for encabezado, ancho_maximo in anchos_maximos.items():
        linea_encabezados += f"| {header_replacements.get(encabezado, encabezado):^{ancho_maximo}} |"
    longitud_tabla = len(linea_encabezados)
    tabla_formateada += linea_encabezados + "\n"

    # Línea divisoria
    linea_divisoria = f"|{'=' * (int(longitud_tabla)-2)}|"
    tabla_formateada += linea_divisoria + "\n"

    # Líneas para cada fila del diccionario
    subtareas = ""
    for diccionario in lista_diccionarios:
        linea_fila = ""
        for encabezado in encabezados_filtrados:
            valor = ""
            if encabezado in diccionario:
                if encabezado != "subtareas":
                    valor = str(diccionario[encabezado])
                else:
                    valor = str(len(diccionario[encabezado]))
                    # Verificar longitud de subtareas
                    if len(diccionario["subtareas"]) > 0:
                        # Formatear texto de la línea divisoria
                        linea_divisoria_subtareas = f"| {'SUBTAREAS':^{longitud_tabla - 4}} |"

                        # Agregar línea divisoria a la tabla formateada
                        subtareas += linea_divisoria_subtareas + "\n"

                        # Recorrer y mostrar subtareas
                        for subtarea in diccionario["subtareas"]:
                            # Formatear información de la subtarea
                            info_subtarea = f"{subtarea.get('id_subtarea', '')}"

                            # Ajustar el ancho del texto
                            info_subtarea_ajustada = textwrap.fill(info_subtarea, width=anchos_maximos[encabezado] - 2)

                            # Crear la línea de la subtarea
                            linea_subtarea = f"| {info_subtarea_ajustada:<{anchos_maximos[encabezado]}} |"

                            # Agregar línea de la subtarea a la tabla formateada
                            subtareas += linea_subtarea + "\n"

            linea_fila += f"| {valor:<{anchos_maximos[encabezado]}} |"
        tabla_formateada += linea_fila + "\n"
        if subtareas != "":
            tabla_formateada += subtareas + "\n"
            subtareas = ""


    # Imprimir la tabla
    print(tabla_formateada)

# Ejemplo de uso
lista_diccionarios = [
    {
        "id_tarea": 1,
        "id_usuario": 1,
        "titulo": "Tarea Inglés muy larga",
        "descripcion": "hacer la tarea de ingles, una descripción muy extensa",
        "fecha_limite": "07/07/2024",
        "estado": "por hacer",
        "prioridad": "baja",
        "subtareas": []
    },
    {
        "id_tarea": 2,
        "id_usuario": 1,
        "titulo": "Gestionar archivos",
        "descripcion": "hacer un programa para gestionar archivos",
        "fecha_limite": "12/10/2024",
        "estado": "por hacer",
        "prioridad": "alta",
        "subtareas": [
            {
                "id_subtarea": 1,
                "id_usuario": 1,
                "tiulo": "Menú Principal",
                "descripcion": "hacer el menu principal",
                "fecha_limite": "12/10/2024",
                "estado": "por hacer",
                "prioridad": "media"
            },
            {
                "id_subtarea": 2,
                "id_usuario": 1,
                "tiulo": "Menú Gestionar archivos",
                "descripcion": "hacer el menu de gestion de archivos",
                "fecha_limite": "12/10/2024",
                "estado": "por hacer",
                "prioridad": "alta"
            }
        ]
    }
]

imprimir_tabla_diccionario_lista(lista_diccionarios)
