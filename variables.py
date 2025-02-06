"""Variables y Entrada/Salida
Saludo personalizado: Pide al usuario su nombre y muestra un mensaje como "¡Hola, [nombre]!".

Convertidor de moneda: Convierte una cantidad en dólares a euros (usa un tipo de cambio fijo, ej: 1 dólar = 0.85 euros).

Calculadora simple: Pide dos números y muestra la suma, resta, multiplicación y división."""

import sys

# Ejercisio 1     
def saludo() -> str:
    name = input("Digite su nombre: ") 
    return print(f"Hola {name}")

# Ejercisio 2 
def cambio_moneda()->float:
    cant_dolar = int(input("Digite la cantidad de dolar que desea saber su conversion a euros: \n"))
    return cant_dolar * 0.85
    
# Ejercisio 3

def calculadora()->float:
    num_1 = int(input("Digite su primer numero: "))
    num_2 = int(input("Digite el segundo numero : "))
    
    return num_1 + num_2 , num_1 - num_2 , num_1 * num_2 , num_1 / num_2
        
    

# Funcion main 
def main():
   while True:
       print(" Seleccione 1 -> Saludo \n Seleccione 2 -> Camcio de dolar a euro \n Seleccione 3 -> Calculos Base 2 numeros\n Seleccione 4 -> Salir \n")
       selecction = int(input("->"))
       match selecction:
            case 1 :
               saludo()
            case 2:
                print(cambio_moneda())
            case 3 :
                calculos = calculadora()
                for x in calculos:
                    print(x)
            case 4:
                sys.exit()
                
if __name__ == "__main__":
    main()
