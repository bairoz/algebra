from decimal import Decimal, getcontext

getcontext().prec = 28

matrices = {}

def crear_matriz():
    identificador = input("Ingresa un identificador para la matriz: ")
    filas = int(input("Ingresa el número de filas de la matriz: "))
    columnas = int(input("Ingresa el número de columnas de la matriz: "))

    matriz = []

    print("Ingresa los valores de la matriz (fila por fila):")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingresa el valor para la posición ({i}, {j}): "))
            fila.append(valor)
            
        matriz.append(fila)

    matrices[identificador] = matriz
    print(f"Matriz '{identificador}' creada y almacenada.")
    return matriz

def seleccionar_matriz():
    if not matrices:
        print("No hay matrices disponibles.")
        return None
    print("Matrices disponibles:")
    for key in matrices:
        print(f"- {key}")
    
    seleccion = input("Ingresa el identificador de la matriz que deseas seleccionar: ")
    if seleccion in matrices:
        return matrices[seleccion]
    else:
        print("Identificador no válido.")
        return None
    
def borrar_matriz(identificador):
    if identificador in matrices:
        del matrices[identificador]
        print(f"Matriz '{identificador}' eliminada del diccionario.")
    else:
        print(f"No se encontró la matriz '{identificador}' en el diccionario.")

def rev_matri(matriz):
    if matriz is None:
        print("No hay matriz cargada.")
        return
    print("Matriz seleccionada:")
    for fila in matriz:
        fila_formateada = [f"{valor:.2f}" for valor in fila]
        print(fila_formateada)

def rref(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    matriz = [[Decimal(x) for x in fila] for fila in matriz]
    
    fila_actual = 0
    for col in range(columnas):
        if fila_actual >= filas:
            break
        
        # Encuentra el pivote en la columna actual
        max_fila = max(range(fila_actual, filas), key=lambda r: abs(matriz[r][col]))
        if matriz[max_fila][col] == 0:
            continue  # No hay pivote en esta columna, pasar a la siguiente columna
        
        # Intercambia la fila actual con la fila del pivote
        if max_fila != fila_actual:
            print("-------------------------------------------------------")
            print(f"Intercambiando F{fila_actual + 1} <-> F{max_fila + 1}")
            matriz[fila_actual], matriz[max_fila] = matriz[max_fila], matriz[fila_actual]
        
        pivote = matriz[fila_actual][col]
        if pivote != 0:
            print("--------------------------------------------------------")
            print(f"F{fila_actual + 1} -> F{fila_actual + 1} / {pivote:.2f}")
            for j in range(columnas):
                matriz[fila_actual][j] /= pivote
        
        for i in range(filas):
            if i != fila_actual:
                factor = matriz[i][col]
                print("------------------------------------------------------------------")
                print(f"F{i+1}->F{i + 1}-({factor:.2f}*F{fila_actual + 1})")
                for j in range(columnas):
                    matriz[i][j] -= factor * matriz[fila_actual][j]
        
        fila_actual += 1
    
    # Convertir de vuelta la matriz a flotantes para que sea legible
    matriz = [[float(x) for x in fila] for fila in matriz]
    
    return matriz

def es_inconsistente(matriz_rref):
    filas = len(matriz_rref)
    columnas = len(matriz_rref[0])
    
    for i in range(filas):
        if all(matriz_rref[i][j] == 0 for j in range(columnas - 1)) and matriz_rref[i][-1] != 0:
            return True
    return False

def imprimir_ecuaciones_y_soluciones(matriz_aumentada):
    filas = len(matriz_aumentada)
    columnas = len(matriz_aumentada[0])
    
    matriz_rref = rref(matriz_aumentada)
    
    if es_inconsistente(matriz_rref):
        print("--------------------------------------------------------")
        print("El sistema es inconsistente y no tiene solución.")
        return
    
    variables = ['X' + str(i + 1) for i in range(columnas - 1)]
    soluciones = {}
    variables_libres = []
    
    # Imprimir el sistema de ecuaciones
    print("\nSistema de ecuaciones:")
    for i in range(filas):
        ecuacion = ""
        for j in range(columnas - 1):  # Hasta la penúltima columna
            coeficiente = matriz_rref[i][j]
            if coeficiente != 0:
                if coeficiente > 0 and j > 0:
                    ecuacion += " + "
                ecuacion += f"{coeficiente:.2f}{variables[j]}"
        
        termino_constante = matriz_rref[i][-1]  # Última columna
        if termino_constante != 0:
            ecuacion += f" = {termino_constante:.2f}"
        else:
            ecuacion += " = 0"
        
        print(ecuacion)
    
    # Determinar las soluciones o variables libres
    print("\nSoluciones:")
    for j in range(columnas - 1):
        es_libre = True
        for i in range(filas):
            if matriz_rref[i][j] != 0:
                es_libre = False
                break
        if es_libre:
            variables_libres.append(variables[j])
    
    for i in range(filas):
        fila = matriz_rref[i]
        if all(val == 0 for val in fila[:-1]) and fila[-1] != 0:
            print("El sistema no tiene solución.")
            return
        elif all(val == 0 for val in fila[:-1]):
            continue
        else:
            for j in range(columnas - 1):
                if fila[j] != 0:
                    soluciones[variables[j]] = fila[-1]
                    break
    
    # Imprimir las soluciones o declarar variables libres
    for var in variables:
        if var in soluciones:
            print(f"{var} = {soluciones[var]:.2f}")
        else:
            print(f"{var} es libre")

def reducir_filas(matriz):
    # Aplicar reducción por filas usando RREF
    return rref(matriz)

def multiplicar_filas_columnas(matriz_a, matriz_b):
    filas_a, columnas_a = len(matriz_a), len(matriz_a[0])
    filas_b, columnas_b = len(matriz_b), len(matriz_b[0])

    # Verificar si se están multiplicando matrices
    if columnas_a == filas_b:
        # Multiplicación de matrices
        matriz_resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]

        for i in range(filas_a):
            for j in range(columnas_b):
                for k in range(columnas_a):
                    matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

        identificador = input("Ingresa un identificador para la nueva matriz resultante: ")
        matrices[identificador] = matriz_resultado

        print(f"Matriz '{identificador}' creada y guardada con éxito.")
        return matriz_resultado
    else:
        # Verificar si se están multiplicando vectores columna (producto punto)
        if columnas_a == 1 and columnas_b == 1 and filas_a == filas_b:
            producto_punto = sum(matriz_a[i][0] * matriz_b[i][0] for i in range(filas_a))
            
            print(f"El producto de los vectores es: {producto_punto:.2f}")
            return producto_punto
        else:
            print("Error: Las dimensiones de los vectores no son compatibles para el producto punto.")
            return None



def suma_vectorial(vectores, escalares):
    if len(vectores) != len(escalares):
        print("Error: El número de vectores debe coincidir con el número "
              "de escalares.")
        return None

    filas, columnas = len(vectores[0]), len(vectores[0][0])

    for vector in vectores:
        if len(vector) != filas or len(vector[0]) != columnas:
            print("Error: Todos los vectores deben tener el mismo tamaño.")
            return None

    matriz_resultado = [[0 for _ in range(columnas)] for _ in range(filas)]

    for idx, vector in enumerate(vectores):
        escalar = escalares[idx]
        for i in range(filas):
            for j in range(columnas):
                matriz_resultado[i][j] += escalar * vector[i][j]

    identificador = input("Ingrese un identificador para el vector resultante: ")
    matrices[identificador] = matriz_resultado
    print(f"Vector '{identificador}' creado y guardado con éxito.")
    
    return matriz_resultado

def resta_vectorial(vectores, escalares):
    if len(vectores) != len(escalares):
        print("Error: El número de vectores debe coincidir con el número "
              "de escalares.")
        return None

    filas, columnas = len(vectores[0]), len(vectores[0][0])

    for vector in vectores:
        if len(vector) != filas or len(vector[0]) != columnas:
            print("Error: Todos los vectores deben tener el mismo tamaño.")
            return None

    matriz_resultado = [[escalares[0] * vectores[0][i][j] 
                         for j in range(columnas)] 
                        for i in range(filas)]

    for idx, vector in enumerate(vectores[1:], start=1):
        escalar = escalares[idx]
        for i in range(filas):
            for j in range(columnas):
                matriz_resultado[i][j] -= escalar * vector[i][j]

    identificador = input("Ingrese un identificador para el vector resultante: ")
    matrices[identificador] = matriz_resultado
    print(f"Vector '{identificador}' creado y guardado con éxito.")
    
    return matriz_resultado

def calcular_distributiva(matriz_a, vector_u, vector_v):
    
    columnas_a = len(matriz_a[0])
    filas_u, columnas_u = len(vector_u), len(vector_u[0])
    filas_v, columnas_v = len(vector_v), len(vector_v[0])
    
    if columnas_a != filas_u or columnas_a != filas_v or filas_u != filas_v or columnas_u != 1 or columnas_v != 1:
        print("Error: Las dimensiones de la matriz y los vectores no son compatibles.")
        return None
    
    # Sumar u + v
    vector_suma = [[vector_u[i][j] + vector_v[i][j] for j in range(columnas_u)] for i in range(filas_u)]
    
    resultado_au_v = multiplicar_matriz_vector(matriz_a, vector_suma)
    
    resultado_au = multiplicar_matriz_vector(matriz_a, vector_u)
    
    resultado_av = multiplicar_matriz_vector(matriz_a, vector_v)
    
    resultado_au_mas_av = [[resultado_au[i][j] + resultado_av[i][j] for j in range(len(resultado_au[0]))] for i in range(len(resultado_au))]
    
    print("\nResultado de A(u + v):")
    rev_matri(resultado_au_v)
    
    print("\nResultado de Au + Av:")
    rev_matri(resultado_au_mas_av)
    
    return resultado_au_v, resultado_au_mas_av


def multiplicar_matriz_vector(matriz_a, vector):
    filas_a, columnas_a = len(matriz_a), len(matriz_a[0])
    filas_v, columnas_v = len(vector), len(vector[0])
    
    # Verificar si es un vector columna
    if columnas_v != 1:
        print("Error: El segundo argumento no es un vector columna.")
        return None

    # Verificar si las dimensiones son compatibles
    if columnas_a != filas_v:
        print("Error: Las dimensiones de la matriz y el vector no son compatibles para la multiplicación.")
        return None

    # Inicializar el vector resultado
    vector_resultado = [[0] for _ in range(filas_a)]
    
    # Realizar la multiplicación de la matriz por el vector columna
    for i in range(filas_a):
        for j in range(columnas_a):
            vector_resultado[i][0] += matriz_a[i][j] * vector[j][0]
    
    return vector_resultado



    
    
    