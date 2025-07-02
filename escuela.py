from biblioteca import *

cant_alumnos = 30
legajos = [10345, 10012, 10278, 10456, 10123, 10089, 10567, 10234, 10045, 10412, 
            10321, 10111, 10543, 10034, 10198, 10211, 10500, 10078, 10156, 10290,
            10400, 10167, 10001, 10512, 10056, 10200, 10367, 10489, 10100, 10525
            ]
nombres = ["Juan Perez", "Maria Gomez", "Lucia Martinez", "Pedro Ramirez", "Camila Torres",
            "Nicolas Sosa", "Julieta Rios", "Facundo Diaz", "Sofia Blanco", "Bruno Ibarra",
            "Valentina Vera", "Agustin Leiva", "Martina Gom", "Ramiro Ortiz", "Dana Lujan",
            "Gonzalo Ayala", "Tamara Rojas", "Leonel Castro", "Isabel Moreno", "Franco Medina",
            "Carla Acosta", "Tomas Molina", "Emilia Nuñez", "Axel Gimenez", "Cecilia Vidal",
            "Emiliano Rojas", "Florencia Paz", "Mateo Peña", "Paula Sosa", "Alex Gomez"
            ]
generos = ['M', 'F', 'F', 'M', 'F',
            'M', 'F', 'M', 'F', 'M',
            'F', 'M', 'F', 'M', 'X',
            'M', 'F', 'M', 'F', 'M',
            'F', 'M', 'F', 'M', 'F',
            'M', 'F', 'M', 'F', 'X'
            ]
notas = [
    [7, 8, 9, 7, 7],
    [9, 6, 7, 8, 3],
    [5, 7, 8, 9, 7],
    [8, 9, 6, 8, 9],
    [6, 1, 9, 7, 6],
    [7, 6, 10, 9, 7],
    [8, 7, 7, 6, 8],
    [9, 8, 6, 10, 7],
    [6, 9, 8, 7, 10],
    [7, 6, 7, 8, 6],

    [5, 8, 9, 7, 9],
    [10, 7, 8, 6, 7],
    [8, 9, 6, 9, 6],
    [7, 10, 7, 7, 9],
    [6, 9, 8, 10, 8],
    [9, 1, 9, 10, 7],
    [7, 6, 10, 9, 10],
    [8, 8, 7, 8, 6],
    [9, 7, 6, 7, 9],
    [6, 9, 7, 10, 8],

    [7, 8, 9, 6, 7],
    [9, 1, 7, 8, 5],
    [5, 7, 8, 9, 7],
    [8, 9, 6, 8, 9],
    [6, 1, 9, 7, 6],
    [7, 6, 10, 9, 7],
    [8, 7, 7, 6, 8],
    [9, 8, 6, 10, 7],
    [6, 1, 8, 7, 5],
    [7, 6, 7, 8, 6]
]

opciones = "1. Cargar alumnos\n2. Mostrar alumnos\n3. Promedios de alumnos\n4. Mayores Promedios\n5. Materias con mayor promedio\n6. Buscar alumno por legajo\n7. repeticiones de notas por materia\n8. Salir"
opciones2 = "1. salir\npresione cualquier otro numero para volver"
materias = ["Matematica", "Programacion", "Arq. y Sistemas Op.", "Ingles", "Metodologia de Estudio"]

while True:
    match menu(opciones):
        case 1:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("1. Cargar alumnos")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            cant_alumnos = int(input("ingrese cantidad de alumnos a cargar:"))
            nombres = iniciar_lista(cant_alumnos, " ")
            generos = iniciar_lista(cant_alumnos, " ")
            legajos = iniciar_lista(cant_alumnos, 0)
            notas = iniciar_matriz(cant_alumnos, 5, 0)
            
            cargar_datos(nombres, generos, legajos, notas, cant_alumnos, 5)
            match menu(opciones2):
                case 1:
                    break
                case 2:
                    continue
        case 2:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("2. Mostrar alumnos")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            if cant_alumnos == 0:
                print("no hay alumnos cargados.")
            else:
                print("")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("nombre   /  genero  /   legajo | \t\t\t Materias ")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                imprimir_datos(nombres, generos, legajos, notas, cant_alumnos)
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            match menu(opciones2):
                case 1:
                    break
                case 2:
                    print("")
                    continue
        case 3:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("3. Promedios de alumnos ")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            promedios = cargar_promedio(notas)
            imprimir_datos(nombres, generos, legajos, notas, cant_alumnos, promedios)
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("nombre   /  genero  /   legajo  |\t\t\t\t Materias \t\t\t\t\t| Promedio")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            imprimir_datos(nombres, generos, legajos, notas, cant_alumnos, promedios)
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            match menu(opciones2):
                case 1:
                    break
                case _:
                    continue
        case 4:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("4. Mayores Promedios")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("nombre   /  genero  /   legajo |\t\t\t\t Materias \t\t\t\t\t| Promedio")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            ordenar_descendente(promedios, notas, generos, legajos, nombres)
            imprimir_datos(nombres, generos, legajos, notas, cant_alumnos, promedios)
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            match menu(opciones2):
                case 1:
                    break
                case 2:
                    continue
        case 5:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("5. Materias con mayor promedio")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            promedio_materias = calcular_promedio_matriz(notas)
            imprimir_promedios_materias(promedio_materias)
            print("")
            imprimir_promedio_mayor(promedio_materias)
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            match menu(opciones2):
                case 1:
                    break
                case _:
                    continue
        case 6:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("6. Buscar alumno por legajo")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            legajo = buscar_por_legajo(legajos)
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("nombre   /  genero  /   legajo |\t\t\t\t Materias \t\t\t\t\t| Promedio")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            imprimir_dato(nombres, generos, legajos, notas, legajo, promedios)
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            print("")
            print("")
            match menu(opciones2):
                case 1:
                    break
                case _:
                    continue
            break
        case 7:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("7. repeticiones de notas por materia")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("")
            imprimir_repeticiones_notas(notas)
            match menu(opciones2):
                case 1:
                    break
                case 2:
                    continue
        case 8:
            print("")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("8. Salir")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━")
            break