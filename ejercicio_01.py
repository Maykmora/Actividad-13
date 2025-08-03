estudiantes={}

def menu():
    print("\n--MENÚ--")
    print("1.Agregar estudiante")
    print("2.Agregar curso con nota")
    print("3.Consultar estudiante")                 #Creacion del menú principal
    print("4.Calcular promedio de estudiante")
    print("5.Verificar si aprueba")
    print("6.Mostramos todos los estudiantes")
    print("7.Salir")

def agregar_estudiante():
    while True:
        print("\n--AGREGAR ESTUDIANTE--")
        id_unico = input("Ingrese el ID del estudiante: ")      #solicitamos el ID
        if id_unico in estudiantes:                             #verificacion
            print("El ID ya existe, registre uno nuevo")
        else:
            nombre=input("Ingrese el nombre del estudiante: ")
            carrera=input("Ingrese la carrera del estudiante: ")
            estudiantes[id_unico]={                             #Agregamos los datos al diccionario
                "nombre":nombre,
                "carrera":carrera,
                "cursos":{}
            }
            print("Estudiante agregado correctamente")
            break

def agregar_curso():
    while True:
        print("\n--AGREGAR CURSO--")
        id_est=input("Ingrese el ID del estudiante: ")              #solicitamos el ID
        if id_est not in estudiantes:                               #verficacion
            print("Estudiante no encontrado, inténtelo de nuevo")
        else:
            curso= input("Ingrese el nombre del curso: ")              #solicitamos el nombre del curso
            try:                                                       #Evitamos errores
                while True:
                    nota=int(input(f"Ingrese la nota final del curso '{curso.strip()}':"))
                    if 0<= nota <=100:
                        estudiantes[id_est]["cursos"][curso]=nota       #agreamos al diccionario las notas
                        print("Curso y nota agregado correctamente")
                        break
                    else:
                        print("La nota debe estar entre 0 y 100, inténtelo de nuevo.")
            except ValueError:
                print("Entrada invalida, inténtelo de nuevo")
            break

def consultar_estudiante():
    while True:
        print("\n--CONSULTAR ESTUDIANTE--")
        id_est=input("Ingrese el ID del estudiante: ")                  #solicitamos el ID
        if id_est in estudiantes:                                       #verificacion
            print(f"Nombre: {estudiantes[id_est]["nombre"]}")           #imprimimos la información
            print(f"Carrera: {estudiantes[id_est]["carrera"]}")
            if estudiantes[id_est]["cursos"]:                           #validacion de que existan cursos
                print("Cursos asignados: ")
                print("Curso : Nota final")
                for curso, nota in estudiantes[id_est]["cursos"].items():
                    print(f"{curso}: {nota}")                           #Imprimimos información del estudiante
                break
            else:
                print("El estudiante no tiene cursos asignados")
                break

        else:
            print("El estudiante no fue encontrado, inténtelo de nuevo")

def promedio_estudiante():
    while True:
        print("\n--PROMEDIO DE ESTUDIANTE--")
        id_est = input("Ingrese el ID del estudiante: ")            #solicitamos el ID
        if id_est in estudiantes:                                   #verificacion de que exista el ID
            if estudiantes[id_est]["cursos"]:                       #si existen cursos imprime el promedio
                print(f"El promedio de {estudiantes[id_est]["nombre"]} es: {sum(estudiantes[id_est]["cursos"].values())/len(estudiantes[id_est]["cursos"]):.2f}")
                break
            else:
                print("El estudiante no tiene cursos registrados.")
        else:
            print("El estudiante no fue encontrado, inténtelo de nuevo")

def verificar_si_aprueba():
    while True:
        print("\n--VERIFICAR APROBACIÓN--")
        id_est=input("Ingrese el ID del estudiante:")           #solicitamos el ID
        if id_est in estudiantes:                               #verificacion si existe el ID
            if estudiantes[id_est]["cursos"]:                   #verifiacion si hay cursos
                aprueba=True
                for curso, nota in estudiantes[id_est]["cursos"].items():
                    if nota <61:
                        aprueba=False                           #convertimos el true en false para validar si aprobó o no
                        break                                   #detenemos para ya no seguir el for
                if aprueba:
                    print(f"El estudiante {estudiantes[id_est]["nombre"]}, aprobó todos sus cursos")
                    break
                else:
                    print(f"El estudiante {estudiantes[id_est]["nombre"]}, No aprobó los cursos:")
                    for curso, nota in estudiantes[id_est]["cursos"].items():
                        if nota < 61:
                            print(f"{curso}: {nota}")
                    break
            else:
                print("El estudiante no tiene cursos asignados")
        else:
            print("El estudiante no fue encontrado.")

def mostrar_info():
    while True:
        print("\n--INFORMACIÓN--")
        if not estudiantes:                                 #si no hay estudiantes se detiene
            print("No hay estudiantes para mostrar")
            break
        else:
            contador=1                                         #contador para imprimir el número de estudiante
            for id_est, datos in estudiantes.items():
                print(f"\nEstudiante #{contador}")
                print(f"ID: {id_est}")                         #imprimimos todos los datos
                print(f"Nombre: {datos["nombre"]}")
                print(f"Carrera: {datos["carrera"]}")
                if datos["cursos"]:                            #validacion si existen cursos
                    for curso, nota in datos["cursos"].items():
                        print(f"{curso}: {nota}")              #imprecion de cursos y notas
                else:
                    print("El estudiante no tiene cursos registrados")
                contador+=1
            break



while True:                 #Programa principal
    menu()
    while True:
        try:                                                            #try para evitar errores
            option=int(input("Seleccione una opción del menú (1-7): "))
            if 1<=option<=7:                                            #validación si está dentro del rango
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
        case 3:
            consultar_estudiante()

        case 4:
            promedio_estudiante()
        case 5:
            verificar_si_aprueba()
        case 6:
            mostrar_info()
        case 7:
            print("\nSaliendo del programa")
            break