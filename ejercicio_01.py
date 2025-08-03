estudiantes={}

def menu():
    print("\n--MENÚ--")
    print("1.Agregar estudiante")
    print("2.Agregar curso con nota")
    print("3.Consultar estudiante")
    print("4.Calcular promedio de estudiante")
    print("5.Verificar si aprueba")
    print("6.Mostramos todos los estudiantes")
    print("7.Salir")

def agregar_estudiante():
    while True:
        print("\n--AGREGAR ESTUDIANTE--")
        id_unico = input("Ingrese el ID del estudiante: ")
        if id_unico in estudiantes:
            print("El ID ya existe, registre uno nuevo")
        else:
            nombre=input("Ingrese el nombre del estudiante: ")
            carrera=input("Ingrese la carrera del estudiante: ")
            estudiantes[id_unico]={
                "nombre":nombre,
                "carrera":carrera,
                "cursos":{}
            }
            print("Estudiante agregado correctamente")
            break

def agregar_curso():
    while True:
        id_est=input("\nIngrese el ID del estudiante: ")
        if id_est not in estudiantes:
            print("Estudiante no encontrado, inténtelo de nuevo")
        else:
            curso= input("Ingrese el nombre del curso: ")
            try:
                while True:
                    nota=int(input(f"Ingrese la nota final del curso '{curso.strip()}':"))
                    if 0<= nota <=100:
                        estudiantes[id_est]["cursos"][curso]=nota
                        print("Curso y nota agregado correctamente")
                        break
                    else:
                        print("La nota debe estar entre 0 y 100, inténtelo de nuevo.")
            except ValueError:
                print("Entrada invalida, inténtelo de nuevo")
            break



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
            agregar_estudiante()
        case 2:
            agregar_curso()