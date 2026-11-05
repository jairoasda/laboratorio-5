
import os
import pickle

ARCHIVO = "contactos.txt"
BINARIO = "contactos.dat"


def registrar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")

    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(nombre + "," + telefono + "\n")

    print("Contacto guardado correctamente.")


def mostrar_contactos():
    if not os.path.exists(ARCHIVO):
        print("No hay contactos registrados.")
        return

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            print(linea.strip())


def buscar_contacto():
    nombre = input("Nombre a buscar: ").lower()
    encontrado = False

    if not os.path.exists(ARCHIVO):
        print("No hay contactos.")
        return

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if nombre in linea.split(",")[0].lower():
                print("Encontrado:", linea.strip())
                encontrado = True

    if not encontrado:
        print("Contacto no encontrado.")


def guardar_binario():
    contactos = []

    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",", 1)
                if len(datos) == 2:
                    contactos.append(datos)

    with open(BINARIO, "wb") as archivo:
        pickle.dump(contactos, archivo)

    print("Archivo binario guardado.")


def leer_binario():
    if not os.path.exists(BINARIO):
        print("No existe el archivo binario.")
        return

    with open(BINARIO, "rb") as archivo:
        contactos = pickle.load(archivo)

    for contacto in contactos:
        print("Nombre:", contacto[0],
              "| Telefono:", contacto[1])


while True:
    print("\n=== SISTEMA DE CONTACTOS ===")
    print("1. Registrar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Guardar archivo binario")
    print("5. Leer archivo binario")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        guardar_binario()
    elif opcion == "5":
        leer_binario()
    elif opcion == "6":
        print("Programa finalizado.")
        break
    else:
        print("Opcion incorrecta.")


