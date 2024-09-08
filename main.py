#if you are in windows change the system ('clear')
from os import system
from matrices import (crear_matriz, rev_matri,
                      borrar_matriz, reducir_filas,
                      seleccionar_matriz, imprimir_ecuaciones_y_soluciones)

def solicitar_opcion():
    while True:
        try:
            opcion = int(input("Digite un número:\n"
                               "1. Crear matriz\n"
                               "2. Revisar matrices\n"
                               "3. Borrar matriz\n"
                               "4. Método de reducción\n"
                               "5. Imprimir ecuaciones y soluciones\n"
                               "6. Salir\n"))
            if opcion in [1, 2, 3, 4, 5, 6]:
                return opcion
            else:
                print("Opción no válida, por favor ingrese un número entre 1 y 6.")
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
        matriz = seleccionar_matriz()
        if matriz is not None:
            identificador = input("Ingresa el identificador de la matriz a borrar: ")
            if identificador in matrices:
                archivo = f'{identificador}.json'  
                borrar_matriz(identificador, archivo)
                print(f"Matriz '{identificador}' borrada.")
            else:
                print("No se encontró una matriz con ese identificador.")
        else:
            print("No hay matrices disponibles para borrar.")

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
        print("Programa terminado.")
        break
    
    input("\nPresiona Enter para continuar...")
    system('clear')

