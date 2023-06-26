#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa que calcula la función cuadrática y lineal y las grafica.

@Autor: Cristian Cala
"""

import matplotlib.pyplot as plt

def mostrar_titulo():
    print("\033[32m=== Programa de Funciones Matemáticas ===\n \033[0m")

def mostrar_menu():
    print("\033[31m1- Salir. \033[0m")
    print("\033[36m2- Calcular función.\033[0m")
    print("\033[36m3- Calcular función cuadrática.\n\033[0m")

def formatear_numero(numero):
    if numero.is_integer():
        return int(numero)
    else:
        return numero

def funcion_lineal():
    print("\033[34m=== Función Lineal ===\033[0m")
    coeficiente = float(input("Ingrese el coeficiente del término dependiente: "))
    termino_independiente = float(input("Ingrese el término independiente: "))

    x = list(range(0, 11))
    y = [coeficiente * xi + termino_independiente for xi in x]

    print("Conjunto de Coordenadas: \n")
    for i in range(len(x)):
        print(f"({x[i]}, {y[i]})", end="\n")

    coeficiente = formatear_numero(coeficiente)
    termino_independiente = formatear_numero(termino_independiente)

    ecuacion = f"y = {coeficiente}x + {termino_independiente}"

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la Función Lineal \n' + ecuacion,
        fontsize=16,
        color='#5A6AC1',
        fontweight='bold'
    )
    plt.show()

def funcion_cuadratica():
    print("\033[34m=== Función Cuadrática ===\033[0m")
    coeficiente_cuadrado = float(input("Ingrese el coeficiente del término dependiente de grado dos: "))
    coeficiente_lineal = float(input("Ingrese el coeficiente del término dependiente de grado uno: "))
    termino_independiente = float(input("Ingrese el término independiente: "))

    x = list(range(0, 11))
    y = [coeficiente_cuadrado * xi ** 2 + coeficiente_lineal * xi + termino_independiente for xi in x]

    print("Conjunto de Coordenadas:\n")
    for i in range(len(x)):
        print(f"({x[i]}, {y[i]})", end="\n")

    coeficiente_cuadrado = formatear_numero(coeficiente_cuadrado)
    coeficiente_lineal = formatear_numero(coeficiente_lineal)
    termino_independiente = formatear_numero(termino_independiente)

    ecuacion = f"y = {coeficiente_cuadrado}x^2 + {coeficiente_lineal}x + {termino_independiente}"

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la Función Cuadrática \n' + ecuacion,
        fontsize=16,
        color='#5A6AC1',
        fontweight='bold'
    )
    plt.show()

def main():
    mostrar_titulo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción:\n")

        if opcion == "1":
            break
        elif opcion == "2":
            funcion_lineal()
        elif opcion == "3":
            funcion_cuadratica()
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
