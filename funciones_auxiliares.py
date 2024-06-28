import csv
import json
from dateutil.relativedelta import relativedelta
import datetime
import dateutil
import modulo_consulta
import modulo_venta

def validar_int(msg, op_menu=False):
    while True:
        try:
            if op_menu:
                msgs(op_menu)
            prompt = int(input(msg))
            return prompt
        except:
            msgs("int")


def validar_alnum(msg):
    while True:
        prompt = input(msg)
        try:
            int(prompt)
            msgs("alnum")
        except:
            return prompt


def opener_catalogo():
    file = open("catalogo.csv")
    DictReader = csv.DictReader(file)
    return [file,DictReader]


def opener_db():
    try:
        with open("registro.json", encoding="utf-8") as file:
            registro = json.load(file)
            print("Registro de ventas cargado...")
            return registro
    except:
        estructura = {
                    "usuarios":[],
                    "pedidos":{
                        "creado": [],
                        "preparacion": []
                    }
}
        export_registro(estructura, is_origin_json=True)
        print("Registro para pedidos de hoy creado...")
        return estructura


def export_registro(db, is_origin_json=False):
    if is_origin_json:
        with open("db.json", "w", encoding="utf-8") as file:
            to_export = json.dumps(db,ensure_ascii=False,indent=4)
            file.write(to_export)
    else:
        with open("db.json", "w", encoding="utf-8") as file:
            to_export = json.dumps(db,ensure_ascii=False,indent=4)
            file.write(to_export)

def msgs(op):
    if op == 1:
        print("=" * 5 + " RESTAURANTE MOLIPOLLITO " + "=" * 5 + "\n1 - Realizar pedido\n2 - Consultar pedidos\n0 - Salir")
    elif op == "cancelar":
        print("> Cancelando compra")
    elif op == "cantidad":
        print("Cantidad de este producto (0 - Cancelar)")
    elif op == "carrito":
        print("Seleccione opcion para agregar al carrito\n[-1 - Finalizar seleccion]    [CANCELAR - Cancelar pedido]")
    elif op == "int":
        input("Ingreso incorrecto, se espera un valor númerico\n[ENTER - Reintentar]")
    elif op == "alnum":
        input("Ingreso incorrecto, se espera un valor alfanumerico\n[ENTER - Reintentar]")
    elif op == "id":
        print("Ingrese su ID")
    elif op == "bad_range":
        input("Opcion invalida, seleccione una opcion dada\n[ENTER - Reintentar]")
    elif op == "pagar":
        print("¿Desea pagar en este momento este pedido?\n[1 - Pagar]   [2- Despuesito]")

def opcion_continuar(msg):
    while True:
        print(f"¿Desea continuar en [{msg}]?\n[Cualquier ingreso - SI]    [0 - NO]")
        op = validar_int("> ")
        if op == 0:
            return op
        else:
            break

def encontrar_usuario(db):
    id = validar_int("> ", "id")
    usuarios = db.get("usuarios")
    for pos,user in enumerate(usuarios):
        id_in_dict = user.get("id usuario")
        if id == id_in_dict:
            print("Usuario Encontrado...")
            return [pos, user]
    return id

def menu_principal(catalogo,registro):
    body = 0
    while True:
        op = validar_int("> ", 1)
        if op == 0:
            print("> Bai")
            break
        elif op == 1:
            if body != 0:
                modulo_venta.inicio_modulo_compras(catalogo, registro, body=body)
            else:
                body = modulo_venta.inicio_modulo_compras(catalogo, registro)
        elif op == 2:
            modulo_consulta.inicio_modulo_consultas(registro)
        else:
            msgs("bad_range")


# PENDIENTE DE ESTRUCTURAR

def tiempo_para_servido():
    date = datetime.datetime.now()
    date_A = "2020-01-01 12:12:12"
    date_A = datetime.datetime.strptime(date_A, "%Y-%m-%d %H:%M:%S")
    diferencia_total = relativedelta(date,date_A).seconds
    print(diferencia_total)