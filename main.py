from os import system
from matrices import (crear_matriz, rev_matri, resta_vectorial,
                      borrar_matriz, reducir_filas, suma_vectorial,
                      seleccionar_matriz, imprimir_ecuaciones_y_soluciones,
                      multiplicar_filas_columnas)

def solicitar_opcion():
    while True:
        try:
            opcion = int(input("Digite un número:\n"
                               "1. Crear matriz\n"
                               "2. Revisar matrices\n"
                               "3. Borrar matriz\n"
                               "4. Método de reducción a su forma escalonada\n"
                               "5. Imprimir ecuaciones y soluciones\n"
                               "6. Multiplicar vectores/matrices\n"
                               "7. Suma o resta de vectores/matrices\n"
                               "8. Salir\n"))
            if opcion in [1, 2, 3, 4, 5, 6, 7, 8]:
                return opcion
            else:
                print("Opción no válida, por favor ingrese un número entre 1 y 8.")
        except ValueError:
            print("Entrada no válida, por favor ingrese un número entero.")

matrices = {}

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
                if isinstance(matriz_resultado, list):
                    print("\nResultado de la multiplicación de matrices:")
                    rev_matri(matriz_resultado)
                elif isinstance(matriz_resultado, float):
                    print(f"\nResultado del producto de vectores: {matriz_resultado:.2f}")
            else:
                print("No se ha seleccionado la segunda matriz para la multiplicación.")
        else:
            print("No se ha seleccionado la primera matriz para la multiplicación.")

            
    elif opcion == 7:
        n = int(input('Cantidad de vectores/matrices: '))
        if n < 2:
            print("Debe ingresar al menos dos vectores/matrices.")
            continue
        
        vectores = []
        escalares = []

        for i in range(n):
            vector = seleccionar_matriz()
            if vector is not None:
                vectores.append(vector)
            else:
                print(f"Error al seleccionar el vector/matriz {i+1}.")
                break

        if len(vectores) == n:
            for i in range(n):
                escalar = float(input(f'Ingrese el escalar para el vector/matriz {i+1}: '))
                escalares.append(escalar)

            operacion = int(input('¿Qué operación desea realizar?\n'
                                  '1. Suma\n'
                                  '2. Resta\n'))

            if operacion == 1:
                matriz_resultado = suma_vectorial(vectores, escalares)
                if matriz_resultado is not None:
                    print("----------------------------------------------------------------------------")
                    rev_matri(matriz_resultado)

            elif operacion == 2:
                matriz_resultado = resta_vectorial(vectores, escalares)
                if matriz_resultado is not None:
                    print("----------------------------------------------------------------------------")
                    rev_matri(matriz_resultado)

            else:
                print("Opción inválida. Por favor, elija 1 para suma o 2 para resta.")

    elif opcion == 8:
        print("Programa terminado.")
        break

    input("\nPresiona Enter para continuar...")
    system("clear")
