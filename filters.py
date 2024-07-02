from datetime import datetime

def imprimirtarea(i):
    print()
    for j in i:
        if j != "subtareas":
            print(j,":",i[j])
        elif any(i["subtareas"]):
            print("subtareas:")
            for k in i["subtareas"]:
                print()
                for l in k:
                    print("         ",l,":",k[l])

# muestra las tareas que no se han terminado
def tareaspendientes(tareas):
    for i in tareas:
        if i["estado"] == "por hacer":
            imprimirtarea(i)

# muestra las tareas terminadas
def tareasterminadas(tareas):
    for i in tareas:
        if i["estado"] == "terminada":
            imprimirtarea(i)

# muestra las tareas por orden de prioridad (alta, media, baja)
def prioridadtareas(tareas):
    alta = []
    media = []
    baja = []

    for i in tareas:
        if i["prioridad"] == "alta":
            alta.append(i)
        elif i["prioridad"] == "media":
            media.append(i)
        elif i["prioridad"] == "baja":
            baja.append(i)

    for i in alta:
        imprimirtarea(i)
    for i in media:
        imprimirtarea(i)
    for i in baja:
        imprimirtarea(i)

# muestra las tareas que se tienen fecha limite cercana dentro de 7 dias en adelante
def tareascercanas(tareas):
    print(datetime.now())
    for i in tareas:
        if i["fecha_limite"]:
            fecha_limite = datetime.strptime(i["fecha_limite"], "%d/%m/%Y")
            fecha_actual = datetime.now()
            diferencia = fecha_limite - fecha_actual
            if -1 <= diferencia.days <= 6:
                imprimirtarea(i)