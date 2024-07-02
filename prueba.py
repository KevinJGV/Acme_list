# Imprime en pantalla las tareas que esten contenidas en la estructura json  diseñada para el programa, se puede usar facilmente con, por ejemplo, cruds.datos_registro
def imprimir_tabla_diccionario_lista(json_a_visualizar):
    # Obtener encabezados (claves únicas) de la lista de diccionarios
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
                    ancho_maximo_clave = max(ancho_maximo_clave, len(encabezado))

                    for subtarea in diccionario["subtareas"]:
                        ancho_maximo_subtarea = 0
                        for atributo in subtarea:
                            valor_subtarea = str(subtarea[atributo])
                            ancho_maximo_subtarea = max(ancho_maximo_subtarea, len(valor_subtarea))

                        ancho_maximo_valor = max(ancho_maximo_valor, ancho_maximo_subtarea)

        anchos_maximos[encabezado] = max(ancho_maximo_clave, ancho_maximo_valor)

    # Asignar ancho máximo del encabezado a la columna "subtareas"
    anchos_maximos["subtareas"] = 9

    # Generar estructura de la tabla
    tabla_formateada = ""

    # Línea superior con encabezados centrados
    linea_encabezados = ""
    for encabezado, ancho_maximo in anchos_maximos.items():
        linea_encabezados += f"| {header_replacements.get(
            encabezado, encabezado):^{ancho_maximo}} |"
    longitud_tabla = len(linea_encabezados)
    linea_encabezados = f"{'-' * (int(longitud_tabla))}\n" + linea_encabezados
    tabla_formateada += linea_encabezados + "\n"

    # Línea divisoria
    linea_divisoria = f"|{'=' * (int(longitud_tabla)-2)}|"
    tabla_formateada += linea_divisoria + "\n"

    # Líneas para cada fila del diccionario
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
                        linea_divisoria_subtareas = f"| {'SUBTAREAS':^{longitud_tabla - 4}} |"

                        # Agregar línea divisoria a la tabla formateada
                        subtareas += linea_divisoria_subtareas + "\n"

                        subtareas += procesar_subtareas(
                            diccionario["subtareas"], anchos_maximos)

            linea_fila += f"| {valor:<{anchos_maximos[encabezado]}} |"

        tabla_formateada += linea_fila + "\n"

        if subtareas != "":
            tabla_formateada += subtareas
            linea_divisoria = f"|{'-' * (int(longitud_tabla)-2)}|"
            tabla_formateada += linea_divisoria + "\n"

    linea_pie = f"{'-' * (int(longitud_tabla))}\n"        
    tabla_formateada += linea_pie
        
    # Imprimir la tabla
    print(tabla_formateada)


# Funcion auxiliar de imprimir_tabla_diccionario_lista() que realiza el proceso de estructuracion para el print final
def procesar_subtareas(subtareas, anchos_maximos):
    encabezados = ['id_subtarea', 'titulo', 'descripcion', 'estado', 'prioridad', 'fecha_limite']
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
                linea_subtarea += f"| {valor_subtarea:<{anchos_maximos["id_tarea"]}} |"
            else:
                linea_subtarea += f"| {valor_subtarea:<{anchos_maximos[encabezado]}} |"

        subtareas_formateadas += linea_subtarea + "\n"
    return subtareas_formateadas

