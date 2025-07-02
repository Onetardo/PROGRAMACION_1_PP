#-------------------- Funciones de validación --------------------------#

def validar_nombre(nombre:str) -> bool:
    '''
    Valida que un nombre no contenga caracteres incorrectos o que esté vacío.
    Args:
        nombre(str)
        
    returns:
        Bool: en caso de haber error retornará True, de lo contrario, retorna False
    '''
    hay_error = False
    for i in nombre:
        if ord(i) >= 48 and ord(i) <= 57 or i == " ":
            hay_error = True

    return hay_error

def validar_genero(genero:str) -> bool:
    '''
    Valida que se cargue un genero de la manera solicitada.
    Args:
        genero(str)
        
    return:
        Bool: en caso de haber error retornará True, de lo contrario, retorna False
    '''
    hay_error = False
    if genero != "M" and genero != "F" and genero != "X" and genero != "m" and genero != "f" and genero != "x":
        hay_error = True
    return hay_error

def validar_legajo(legajo:str, legajos_existentes: list) -> bool:
    '''
    Valida que un legajo sea cargado correctamente (debe ser de 5 digitos, no empieza con 0 y no se repite con otro legajo ya existente)
    
    Args:
        legajo(str): es el legajo a ingresar
        legaos_existentes(list): es la lista en la que se cargaran los legajos para ser comparados con los posteriores
    return:
        Bool: en caso de haber error retornará True, de lo contrario, retorna False
    '''
    hay_error = False
    for i in legajo:
        if ord(i) < 48 and ord(i) > 57:
            hay_error = True
    legajo_valido = int(legajo)
    if legajo_valido < 10000 or legajo_valido > 99999:
            hay_error = True
    for existente in legajos_existentes:
        if existente == legajo:
            hay_error = True
    return hay_error

def validar_numero(numero:str) -> bool:
    '''
    Valida que lo que se esté ingresando sea un numero y que este no sea menor a 1
    Args:
        numero(str)
    returns:
        Bool: en caso de haber error retornará True, de lo contrario, retorna False
    '''
    hay_error = False
    for i in numero:
        if ord(i) > 47 and ord(i) < 58:
            if int(numero) < 1:
                hay_error = True
        else:
            hay_error = True
    return hay_error

def validar_nota(nota:str) -> bool:
    '''
    Valida que la nota ingresada se encuentre entre el 1 y el 10
    Args:
        nota(str)
    return:
        Bool: en caso de haber error retornará True, de lo contrario, retorna False
    '''
    hay_error = False
    for i in nota:
        if ord(i) < 48 and ord(i) > 57:
            hay_error = True
    numero_valido = int(nota)
    if numero_valido < 1 or numero_valido > 10:
        hay_error = True
    return hay_error

#--------------- busqueda ---------------#
def buscar_por_legajo(lista_legajos:list):
    '''
    Busca a un alumno por su legajo
    Args:
        lista_legajos(list): la lista de legajos en la que se buscará el legajo solicitado
    Return:
        el legajo solicitado
    '''
    legajo = input("Ingrese legajo del alumno: ")
    legajo_encontrado = None
    while validar_legajo(legajo, lista_legajos):
        legajo = input("Ingrese legajo valido: ")
    legajo_validado = int(legajo)
    for i in range(len(lista_legajos)):
        if legajo_validado == lista_legajos[i]:
            legajo_encontrado = i
            break
    return legajo_encontrado
#--------------- inicializar ---------------#
def menu(opciones: str) -> int:
    '''
    Abre un menú de opciones.
    Args:
        opciones: son las opciones que el usuario podrá elegir
    return:
    int: la opcion elegida convertida en numero entero
    '''
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(opciones)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("")
    opcion_elegida = input("elija una opcion:\n\n----> ")
    validar_numero(opcion_elegida)
    while validar_numero(opcion_elegida) == True:
        opcion_elegida = input("Error. elija una opcion correcta:\n\n----> ")
    opcion_valida = int(opcion_elegida)
    return opcion_valida

def iniciar_matriz(cant_filas:int, cant_columnas:int, valor_inicial: any) -> list:
    '''
    Crea una matriz.
    Args:
        cant_filas(int): cantidad de filas que tendrá la matriz
        cant_columnas(int): cantidad de columnas que tendrá la matriz
        valor_inicial(any): valor con el que se rellenará la matriz
    return:
        list: la matriz
    '''
    matriz= []
    for i in range(cant_filas):
        i = [valor_inicial] * cant_columnas
        matriz += [i]
    return matriz

def iniciar_lista(cant_filas: int, valor_inicial: any) -> list:
    '''
    Crea una lista
    Args:
        cant_filas(int): cantidad de filas de la lista
        valor_inicial(int): es el valor con el que se rellenará la lista
    Return:
        list: la lista
    '''
    lista = [valor_inicial] * cant_filas
    return lista

#--------------- calculos ---------------# 
def calcular_promedio(lista_numeros:list) -> float:
    '''
    Calcula el promedio de los numeros dentro de una lista
    Args:
        lista_numeros: la lista de numeros a promediar
    Return:
        float: el promedio de los numeros
    '''
    acumulador = 0
    contador = 0
    for numero in lista_numeros:
        acumulador += numero
        contador += 1
    if contador == 0:
        resultado = 0
        
    resultado = acumulador / contador
    return resultado

def calcular_promedio_matriz(matriz_numeros:list) -> list:
    '''
    calcula el promedio de la columna de una matriz y almacena estos promedios en una lista
    Args:
        matriz_numeros(list): es la matriz que se utilizara para el calculo
    Return:
        list: lista de los promedios
    '''
    cant_columnas = 0
    for fila in matriz_numeros:
        if len(fila) > cant_columnas:
            cant_columnas = len(fila)

    acumulador_columnas = [0] * cant_columnas
    contador_columnas = [0] * cant_columnas

    for fila in matriz_numeros:
        for i in range(len(fila)):
            acumulador_columnas[i] += fila[i]
            contador_columnas[i] += 1
    
    promedios = [0] * cant_columnas
    for i in range(cant_columnas):
        promedios[i] = acumulador_columnas[i] / contador_columnas[i]
    return promedios

def cantidad_notas(matriz_notas: list) -> list:
    '''
    contabiliza la cantidad de notas que se repiten en una matriz de notas
    Args:
        matriz_notas(list): es la matriz donde se contabilizaran las notas repetidas
    Return:
        list: lista de cantidad de notas repetidas, donde cada columna representa la calificacion.
    '''
    contador = iniciar_matriz(5, 10, 0)
    for fila in matriz_notas:
        for j in range(5):
            nota = fila[j]
            contador[j][nota - 1] += 1

    return contador
#--------------- carga de datos ---------------#
def cargar_nombre() -> str:
    '''
    Ingresa un dato solicitado(nombre) y lo valida
    Args:

    Return:
        str: retorna el nombre validado
    '''
    nombre = input("Ingresar nombre: ")
    while validar_nombre(nombre):
        nombre = input("Error. Ingresar nombre válido: ")
    return nombre

def cargar_genero() -> str:
    '''
    Ingresa un dato solicitado(genero) y lo valida
    Args:
    
    Return:
        str: retorna el genero validado
    '''
    genero = input("Ingresar género[F | M | X]: ")
    while validar_genero(genero):
        genero = input("Error. Ingresar género válido[F | M | X]: ")
    return genero

def cargar_legajo(legajos_existentes:list) -> int:
    '''
    Ingresa un dato solicitado(legajo) y lo valida
    Args:
    legajos_existentes: utiliza la lis
    Return:
        int: retorna el legajo validado
    '''
    legajo = input("Ingresar legajo: ")
    while validar_legajo(legajo, legajos_existentes):
        legajo = input("Error. Ingresar legajo válido: ")
    legajo_valido = int(legajo)
    return legajo_valido

def cargar_notas(materias: list, cant_notas: int) -> list:
    '''
    Ingresa datos solicitados(notas), los valida y los mete a una lista
    Args:
    materias(list): es la lista de materias a la que se les asignan las notas
    cant_notas(int): la canidad de notas a ingresar
    Return:
        list: retorna el la lista de notas validadas
    '''
    notas = [0] * cant_notas
    for i in range(cant_notas):
        nota = input(f"Ingrese nota del alumno en {materias[i]}: ")
        while validar_nota(nota):
            nota = input(f"Error. Ingrese una nota valida: ")
        notas[i] = int(nota)
    return notas

def cargar_datos(nombres:list, generos:list, legajos:list, notas:list, cant:int, materias: list, cant_notas: int) -> None:
    '''
    carga todos los datos a sus respectivas listas
    Args:
    nombres(list): lista donde se cargan los nombres
    generos(list): lista donde se cargan los generos
    legajos(list): lista donde se cargan los legajos
    notas(list): lista donde se cargan las notas
    cant(int): la cantidad de personas a cargar
    materias(list): la lista de materias donde se asignaran las notas
    cant_notas(int): la cantidad de notas a cargar
    '''
    for i in range(cant):
        nombres[i] = cargar_nombre()
        generos[i] = cargar_genero()
        legajos[i] = cargar_legajo(legajos)
        notas[i] = cargar_notas(materias, cant_notas)

def cargar_promedio(lista_notas: list):
    '''
    Carga los promedios calculados a una lista.
    Args:
        lista_notas(list): es la lista de notas a las que se les sacará promedio
    Return:
        lista_prom: la lista con los respectivos promedios
    '''
    lista_prom = []
    for i in lista_notas:
        lista_prom += [calcular_promedio(i)]
    return lista_prom

#--------------- ordenamiento de datos ---------------#
def ordenar_ascendente(lista_primer_criterio:list, lista_segundo_criterio:list, lista_c:list, lista_d = None, lista_e = None) -> None:
    '''
    ordena listas de manera ascendente teniendo en cuenta dos criterios.
    Args:
        lista_primer_criterio(list): es la lista con la que se tomará el primer criterio de ordenanza
        lista_segundo_criterio(list): lista con la que, en caso de que la primera lista esté ordenada de por si, ordenará bajo otro criterio
        lista_c(list): lista que se ordenará en base a los dos criterios anteriores
        lista_d(None): lista opcional, en caso de no haber lista, simplemente no ordenará nada
        lista_e(None): lista opcional, en caso de no haber lista, simplemente no ordenará nada
    '''
    for i in range(0, len(lista_primer_criterio)-1, 1):
        for j in range(i + 1, len(lista_primer_criterio), 1):
            if lista_primer_criterio[i] > lista_primer_criterio[j]:
                primer_auxiliar = lista_primer_criterio[i]
                lista_primer_criterio[i] = lista_primer_criterio[j]
                lista_primer_criterio[j] = primer_auxiliar
                
                auxiliar_b = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = auxiliar_b
                
                segundo_auxiliar = lista_segundo_criterio[i]
                lista_segundo_criterio[i] = lista_segundo_criterio[j]
                lista_segundo_criterio[j] = segundo_auxiliar
                
                if lista_d != None:
                    auxiliar_d = lista_d[i]
                    lista_d[i] = lista_d[j]
                    lista_d[j] = auxiliar_d
                if lista_e != None:
                    auxiliar_e = lista_e[i]
                    lista_e[i] = lista_e[j]
                    lista_e[j] = auxiliar_e
            elif lista_primer_criterio[i] == lista_primer_criterio[j]:
                if lista_segundo_criterio[i] > lista_segundo_criterio[j]:
                    auxiliar_b = lista_c[i]
                    lista_c[i] = lista_c[j]
                    lista_c[j] = auxiliar_b
                
                    primer_auxiliar = lista_primer_criterio[i]
                    lista_primer_criterio[i] = lista_primer_criterio[j]
                    lista_primer_criterio[j] = primer_auxiliar
                    
                    if lista_d != None:
                        auxiliar_d = lista_d[i]
                        lista_d[i] = lista_d[j]
                        lista_d[j] = auxiliar_d
                    if lista_e != None:
                        auxiliar_e = lista_e[i]
                        lista_e[i] = lista_e[j]
                        lista_e[j] = auxiliar_e

def ordenar_descendente(lista_primer_criterio:list, lista_segundo_criterio:list, lista_c:list, lista_d = None, lista_e = None) -> None:
    '''
    ordena listas de manera descendente teniendo en cuenta dos criterios.
    Args:
        lista_primer_criterio(list): es la lista con la que se tomará el primer criterio de ordenanza
        lista_segundo_criterio(list): lista con la que, en caso de que la primera lista esté ordenada de por si, ordenará bajo otro criterio
        lista_c(list): lista que se ordenará en base a los dos criterios anteriores
        lista_d(None): lista opcional, en caso de no haber lista, simplemente no ordenará nada
        lista_e(None): lista opcional, en caso de no haber lista, simplemente no ordenará nada
    '''
    for i in range(0, len(lista_primer_criterio)-1, 1):
        for j in range(i + 1, len(lista_primer_criterio), 1):
            if lista_primer_criterio[i] < lista_primer_criterio[j]:
                primer_auxiliar = lista_primer_criterio[i]
                lista_primer_criterio[i] = lista_primer_criterio[j]
                lista_primer_criterio[j] = primer_auxiliar
                
                auxiliar_b = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = auxiliar_b
                
                segundo_auxiliar = lista_segundo_criterio[i]
                lista_segundo_criterio[i] = lista_segundo_criterio[j]
                lista_segundo_criterio[j] = segundo_auxiliar
                
                if lista_d != None:
                    auxiliar_d = lista_d[i]
                    lista_d[i] = lista_d[j]
                    lista_d[j] = auxiliar_d
                if lista_e != None:
                    auxiliar_e = lista_e[i]
                    lista_e[i] = lista_e[j]
                    lista_e[j] = auxiliar_e
            elif lista_primer_criterio[i] == lista_primer_criterio[j]:
                if lista_segundo_criterio[i] < lista_segundo_criterio[j]:
                    auxiliar_b = lista_c[i]
                    lista_c[i] = lista_c[j]
                    lista_c[j] = auxiliar_b
                
                    primer_auxiliar = lista_primer_criterio[i]
                    lista_primer_criterio[i] = lista_primer_criterio[j]
                    lista_primer_criterio[j] = primer_auxiliar
                    
                    if lista_d != None:
                        auxiliar_d = lista_d[i]
                        lista_d[i] = lista_d[j]
                        lista_d[j] = auxiliar_d
                    if lista_e != None:
                        auxiliar_e = lista_e[i]
                        lista_e[i] = lista_e[j]
                        lista_e[j] = auxiliar_e
#--------------- impresión de datos ---------------#
def imprimir_repeticiones_notas(matriz_notas:list, lista_materias: list):
    '''
    imprime la cantidad de veces que se repite una nota por materia
    Args:
        matriz_notas(list): la matriz de notas que se analizará
        lista_materias(list): las materias a las que se les contarán las repeticiones
    '''
    resultado = cantidad_notas(matriz_notas)
    for i in range(len(lista_materias)):
        print(f"recuento de notas para {lista_materias[i]}")
        for nota in range(10):
                print(f"nota {nota+1}: {resultado[i][nota]} repeticiones")
        print("")

def imprimir_promedios_materias(promedio_materias:list, lista_materias:list):
    '''
    imprime los promedios de las materias ordenados de forma descendente.
    Args:
        promedios_materias(list): es la lista que contiene los promedios de cada materia
        lista_materias(list): lista de las materias a las que le pertenece cada promedio
    '''
    indices = lista_materias
    for i in range(len(indices)):
        for j in range ( i + 1,5):
            if promedio_materias[i] < promedio_materias[j]:

                aux= promedio_materias[i]
                promedio_materias[i]= promedio_materias[j]
                promedio_materias[j] = aux

                aux = indices[i]
                indices[i] = indices[j]
                indices[j] = aux 
    for i in range(len(lista_materias)):
        print (f"Materia: {lista_materias[i]} | Promedio : {promedio_materias[i]}")

def imprimir_dato(nombre:list, genero:list, legajo:list, nota: list, indice = None, promedio = None) -> None:
    if indice == None:
        print("error para imprimir")
    elif promedio == None:
        print(f"{nombre[indice]}\t {genero[indice]}\t {legajo[indice]}\t", end="")
        for n in nota[indice]:
            print(f"\t{n}\t", end = "")
        print("")
    else:
        print(f"{nombre[indice]}\t {genero[indice]}\t {legajo[indice]}\t", end = " ")
        for n in nota[indice]:
            print(f"\t{n}\t", end = " ")
        print(f"\t{promedio[indice]}\t")

def imprimir_datos(nombres:list, generos:list, legajos:list, notas: list, tamano:int, promedios = None) -> None:
    if nombres == None:
        print("primero cargue almenos un alumno.")
    for i in range(tamano):
        imprimir_dato(nombres, generos, legajos, notas, i, promedios)

def imprimir_matriz(matriz: list):
    '''
    muestra la matriz de manera mas ordenada y estética
    Args:
        matriz: matriz a imprimir
    '''
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print("")

def imprimir_lista(lista:list):
    '''
    muestra la lista de manera mas ordenada y estética
    Args:
        lista: lista a imprimir
    '''
    for i in lista:
        print(f"{i}\t", end= " ")
    print(" ")

def imprimir_promedio_mayor(promedios_materias: list, lista_materias: list):
    '''
    imprime la materia con mayor promedio.
    Args:
        promedio_materias(list): son los promedios de las materias que se utilizaran para ver cual es el mas alto
        lista_materias(list): la lista de las materias
    '''
    mayor = promedios_materias[0]
    posicion= 0

    for i in range(len(lista_materias)):
        if promedios_materias[i] > mayor:
            mayor = promedios_materias[i]
            posicion = i
    nombre_materia= lista_materias[posicion]
    print(f"Materia con mayor promedio general: {nombre_materia} | Promedio: {mayor}")

def imprimir_materias(materias:list):
    '''
    muestra la lista de naterias de manera mas ordenada y estética
    Args:
        lista: lista a imprimir
    '''
    for i in materias:
        print(f"{i}\t|\t", end= " ")
