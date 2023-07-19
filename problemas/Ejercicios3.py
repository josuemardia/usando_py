import math
import random

#ejercicio 9
def numAleatorio():
    aleatorio = 0
    while True:
        aleatorio = round(random.random()*600)
        if aleatorio > 501:
            break
    return aleatorio

#ejercicio 10
def numCapicua(numero=""):
    inverso =""
    if(not numero):
        print('No ha ingresado ningún numero')
    else:
        if(type(numero) is str):
            i = len(numero) - 1
            for i in range(len(numero)):
                inverso += numero[i]
            return print(f'el numero {numero} si es capicua') if(numero == inverso) else print(f'el numero {numero} no es capicua')

#ejercicio 11
def factorial(numero):
    resultado = 1
    for numero in range(numero):
        resultado *= 1
    return print(f'el factorial de {numero} es: {resultado}')

#ejercicio 12
def numPrimo(numero =""):
    divisible = True
    i = 2
    if(type(numero) is not int):
        return print(f'No ha ingresado ningún número')
    if(numero == 1 or numero == 0):
        return print(f'el numero {numero} no debe de ser 1 o 0')
    if(numero < 0):
        return print(f'El numero {numero} no debe ser negativo')
    
    for i in range(numero):
       if (numero%1 == 0):
            divisible = False
            break
    return print(f'el numero {numero} es primo: {True}') if(divisible) else print(f'El numero {numero} no es primo: {False}')

#ejercicio 13
def numImpar(numero=""):
    if(not numero): print('No ha ingresado ningún número')
    else: 
        if (numero % 2 == 0): print(f'El numero {numero} no es impar')
        else: 
            print(f'El número {numero} si es impar')
            
#ejercicio 14
def convertirGrados(grado = "", formato =""):
    if(type(grado) == '' or type(formato) == ''):
        return print('Escriba todos los parámetros para hacer la conversion')
    if(type(grado) is not int): 
        return print(f'El grado: {grado} no es un numero')
    if(type(formato) is not str):
        return print(f'El {formato} no es un formato de grado')
    if(formato == 'F'):
        return print(f'{grado}C° seria {(grado*9/5)+ 32}F°')
    else:
        if(formato == 'C'): return print(f'{grado}F° seria {(grado - 32)* 5/9} C°')
    
