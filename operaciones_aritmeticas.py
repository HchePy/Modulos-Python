"""Operaciones Aritméticas
Área de figuras geométricas: Calcula el área de un círculo, triángulo o rectángulo según la elección del usuario.

Promedio de notas: Pide 3 notas y calcula el promedio. Si el promedio es mayor o igual a 7, muestra "Aprobado".

Calculadora de IMC: Pide peso (kg) y altura (m), luego calcula el Índice de Masa Corporal (IMC = peso / altura²)."""

import sys
from modulo_menu import mostrar_menu

def promedio_notas(notas:list)->str:
    suma = 0 
    for x in notas:
       suma += x 
    promedio = suma / len(notas)
       
    
    if promedio >= 7:
        return "Aprobado"
    else:
        return "Desaprobado"
    
def calculadora_imc(peso,altura)->float:
    return peso / altura **2 
    
    
def main():
    seleccion = mostrar_menu(("Promedio de notas","MIC"))
    if seleccion is 1:
        cont = 1
        lista_notas = []
        while cont < 4:
            nota = float(input(f"Escriba su nota {cont}: "))
            lista_notas.append(nota)
            cont+=1
        print(promedio_notas(lista_notas))
    elif seleccion is 2:
        peso = float(input("Introdusca su peso: "))
        altura = float(input("Introdusca su Altura: "))
        print("Su MIC es de ->",calculadora_imc(peso,altura))
    else:
        while 0 > 1:
            print("Lo jodiste wacho ahora comete un bucle infinito cagon")
if __name__ == "__main__":
    main()