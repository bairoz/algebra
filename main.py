from os import system, name
from matrices import (crear_matriz, rev_matri,
                      borrar_matriz, reducir_filas,
                      seleccionar_matriz, imprimir_ecuaciones_y_soluciones,
                      multiplicar_filas_columnas)

def solicitar_opcion():
    while True:
        try:
            opcion = int(input("Digite un número:\n"
                               "1. Crear matriz\n"
                               "2. Revisar matrices\n"
                               "3. Borrar matriz\n"
                               "4. Método de reducción\n"
                               "5. Imprimir ecuaciones y soluciones\n"
                               "6. Multiplicar matrices\n"
                               "7. Salir\n"))
            if opcion in [1, 2, 3, 4, 5, 6, 7]:
                return opcion
            else:
                print("Opción no válida, por favor ingrese un número entre 1 y 7.")
        except ValueError:
            print("Entrada no válida, por favor ingrese un número entero.")

matrices = {}

def limpiar_pantalla():
    # Función para limpiar la pantalla dependiendo del sistema operativo
    system('cls' if name == 'nt' else 'clear')

while True:
    opcion = solicitar_opcion()

    if opcion == 1:
        crear_matriz()
        print("Matriz creada y guardada.")

    elif opcion == 2:
        matriz = seleccionar_matriz()
        if matriz is not None:
            rev_matri(matriz)
        else:
            print("No se ha seleccionado ninguna matriz.")

    elif opcion == 3:
        identificador = input("Ingresa el identificador de la matriz a borrar: ")
        if identificador in matrices:
            borrar_matriz(identificador)
            print(f"Matriz '{identificador}' borrada.")
        else:
            print("No se encontró una matriz con ese identificador.")

    elif opcion == 4:
        matriz = seleccionar_matriz()
        if matriz is not None:
            matriz_rref = reducir_filas(matriz)
            print("\nMatriz reducida por filas:")
            rev_matri(matriz_rref)
        else:
            print("No hay matriz seleccionada para reducir.")

    elif opcion == 5:
        matriz = seleccionar_matriz()
        if matriz is not None:
            imprimir_ecuaciones_y_soluciones(matriz)
        else:
            print("No hay matriz seleccionada para imprimir ecuaciones y soluciones.")
            
    elif opcion == 6:
        matriz_a = seleccionar_matriz()
        if matriz_a is not None:
            matriz_b = seleccionar_matriz()
            if matriz_b is not None:
                matriz_resultado = multiplicar_filas_columnas(matriz_a, matriz_b)
                if matriz_resultado is not None:
                    print("\nResultado de la multiplicación de matrices:")
                    rev_matri(matriz_resultado)
            else:
                print("No se ha seleccionado la segunda matriz para la multiplicación.")
        else:
            print("No se ha seleccionado la primera matriz para la multiplicación.")

    elif opcion == 7:
        print("Programa terminado.")
        break

    input("\nPresiona Enter para continuar...")
    system("clear")
