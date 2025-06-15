import os

ARCHIVOS = {
    "huesped": "huespedes.txt",
    "automovil": "automoviles.txt",
    "turista": "turistas.txt"
}

def escribir_archivo(nombre_archivo, datos):
    with open(nombre_archivo, "a") as f:
        f.write(";".join(datos) + "\n")

def leer_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, "r") as f:
        return [line.strip().split(";") for line in f.readlines()]

def buscar_en_archivo(nombre_archivo, campo, valor):
    registros = leer_archivo(nombre_archivo)
    resultados = [r for r in registros if r[campo].lower() == valor.lower()]
    return resultados

def menu_huesped():
    while True:
        print("\n--- MENÚ HUÉSPED ---")
        print("1. Crear registro")
        print("2. Listar registros")
        print("3. Buscar por CI")
        print("4. Volver al menú principal")
        opc = input("Elija una opción: ")
        if opc == "1":
            ci = input("CI: ")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            procedencia = input("Procedencia: ")
            genero = input("Género: ")
            celular = input("Celular: ")
            escribir_archivo(ARCHIVOS["huesped"], [ci, nombre, edad, procedencia, genero, celular])
        elif opc == "2":
            for r in leer_archivo(ARCHIVOS["huesped"]):
                print(r)
        elif opc == "3":
            ci = input("CI a buscar: ")
            resultados = buscar_en_archivo(ARCHIVOS["huesped"], 0, ci)
            for r in resultados:
                print(r)
        elif opc == "4":
            break

def menu_automovil():
    while True:
        print("\n--- MENÚ AUTOMÓVIL ---")
        print("1. Crear registro")
        print("2. Listar registros")
        print("3. Buscar por Placa")
        print("4. Volver al menú principal")
        opc = input("Elija una opción: ")
        if opc == "1":
            placa = input("Placa: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")
            precio = input("Precio: ")
            escribir_archivo(ARCHIVOS["automovil"], [placa, marca, modelo, color, precio])
        elif opc == "2":
            for r in leer_archivo(ARCHIVOS["automovil"]):
                print(r)
        elif opc == "3":
            placa = input("Placa a buscar: ")
            resultados = buscar_en_archivo(ARCHIVOS["automovil"], 0, placa)
            for r in resultados:
                print(r)
        elif opc == "4":
            break

def menu_turista():
    while True:
        print("\n--- MENÚ TURISTA ---")
        print("1. Crear registro")
        print("2. Listar registros")
        print("3. Buscar por Identificador")
        print("4. Volver al menú principal")
        opc = input("Elija una opción: ")
        if opc == "1":
            idt = input("Identificador: ")
            nombre = input("Nombre: ")
            nacionalidad = input("Nacionalidad: ")
            genero = input("Género: ")
            lugar = input("Lugar de procedencia: ")
            escribir_archivo(ARCHIVOS["turista"], [idt, nombre, nacionalidad, genero, lugar])
        elif opc == "2":
            for r in leer_archivo(ARCHIVOS["turista"]):
                print(r)
        elif opc == "3":
            idt = input("Identificador a buscar: ")
            resultados = buscar_en_archivo(ARCHIVOS["turista"], 0, idt)
            for r in resultados:
                print(r)
        elif opc == "4":
            break

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestionar Huéspedes")
        print("2. Gestionar Automóviles")
        print("3. Gestionar Turistas")
        print("4. Salir")
        opc = input("Seleccione una opción: ")
        if opc == "1":
            menu_huesped()
        elif opc == "2":
            menu_automovil()
        elif opc == "3":
            menu_turista()
        elif opc == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu_principal()
