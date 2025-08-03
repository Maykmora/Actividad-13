estudiantes={}

def menu():
    print("1.Agregar estudiante")
    print("2.Agregar curso con nota")
    print("3.Consultar estudiante")
    print("4.Calcular promedio de estudiante")
    print("5.Verificar si aprueba")
    print("6.Mostramos todos los estudiantes")
    print("7.Salir")
def agregar_estudiante():
    id_unico=input("Ingrese el ID del estudiante: ")
    if id_unico in estudiantes:
        print("El ID ya existe, registre uno nuevo")
while True:
    menu()
    while True:
        try:
            option=int(input("Seleccione una opción del menú (1-7): "))
            if 1<=option<=7:
                break
            else:
                print("Error inténtelo de nuevo ")
        except ValueError:
            print("Error inténtelo de nuevo ")

    match option:
        case 1:
            print()