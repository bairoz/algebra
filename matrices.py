import decimal
from decimal import Decimal, getcontext
import os

# Establecer el nivel de precisión que deseas (por ejemplo, 28 dígitos)
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
    
def borrar_matriz(identificador, archivo):
    if os.path.exists(archivo):
        os.remove(archivo)
        print(f"Archivo {archivo} eliminado para la matriz '{identificador}'.")
    else:
        print(f"El archivo {archivo} no existe.")

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
    
    # Convertir la matriz a Decimal para mayor precisión
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
        
        # Normaliza la fila del pivote para que el valor pivote sea 1
        pivote = matriz[fila_actual][col]
        if pivote != 0:
            print("--------------------------------------------------------")
            print(f"F{fila_actual + 1} -> F{fila_actual + 1} / {pivote:.2f}")
            for j in range(columnas):
                matriz[fila_actual][j] /= pivote
        
        # Elimina los elementos en la columna actual de las otras filas
        for i in range(filas):
            if i != fila_actual:
                factor = matriz[i][col]
                print(f"{factor:.2f}*F{fila_actual + 1}-{i + 1}")
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
