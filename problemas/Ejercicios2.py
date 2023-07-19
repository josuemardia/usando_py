import re

#Problema 5
def invertirCadena(cadena):
    return f'la cadena invertida de {cadena} sería: {cadena.split("").reverse().join()}'

#problema 6
def findRepeticion(cadena, repetido):
    vecesRepetidads = re.finditer(cadena, repetido)
    return f'Las veces repetidas fueron {vecesRepetidads}'

#problema 7
def palindromoCadena(cadena):
    inverso = ''
    for i in range(len(cadena)):
        inverso+= cadena[i]
    
    if (inverso.upper() == cadena.upper()):
        return print('Si es un palindromo :D')
    else:
        return print('No es un palindromo D:')
    
#problema 8
def removePatron(cadena, regexP):
    regex = regexP
    a = re.finditer(cadena, regex)
    return a