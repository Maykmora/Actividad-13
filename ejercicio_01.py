def menu():
    print("1.Agregar estudiante")
    print("2.Agregar curso con nota")
    print("3.Consultar estudiante")
    print("4.Calcular promedio de estudiante")
    print("5.Verificar si aprueba")
    print("6.Mostramos todos los estudiantes")
    print("7.Salir")


while True:
    menu()
    while True:
        try:
            option=int(input("Seleccione una opción del menú (1-7): "))
            if option>0:
                break
            else:
                print("Error al seleccionar una opción")
        except ValueError:
            print("Error inténtelo de nuevo ")