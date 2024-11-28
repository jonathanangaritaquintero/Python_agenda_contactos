
def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto: ")
    telefono = input("Por favor introduzca el numero de telefono: ")
    email = input("Por favor introduzca el email: ")
    agenda[nombre] = { "telefono": telefono, "email": email}
    print(f"Se ha agregado el contacto {nombre} exitosamente!")


def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    opcion = input("Esta seguro que desea eliminarlo? ")
    if opcion == "si":
        if nombre in agenda:
            del agenda[nombre]
            print(f"El contacto {nombre} ha sido eliminado correctamente")
        else:
            print(f"No se ha encontrado un contacto con el nombre {nombre}")
    else:
        print("Por favor elija una opcion: ")       

def buscar_contacto(agenda):
    nombre = input("Por favor ingresa el contacto que quiera buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]["telefono"]} ")
        print(f"Email: {agenda[nombre]["email"]} ")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")
        

def listar_contactos(agenda):
    if agenda:
        print("\nList de contactos: ")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20)

    else:
        print("La agenda esta vacia")

            
def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opcion: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Salliendo de la agenda de contactos!")
            break
        else:
            print("Por favor seleccione una opcion valida")

agenda_contactos()



