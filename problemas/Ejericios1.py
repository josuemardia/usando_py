#Problema 1 | Evaluacion de inputs cadenas
def NumeroCaracteres (cadena):
    if (type(cadena) is str):
        return f'el numero de caracteres es {cadena.len()}'
    else:
        return f'el input: {cadena} no es una cadena de texto'

#Problema 2 | recortar una cadena
def RecortarCadena(cadena, numCaracter):
    cadenaRecortada = ""
    for i in range(numCaracter):
        cadenaRecortada += cadena[i]
    return cadenaRecortada

#Problema 3 | Separator symbol
def SeparadorCadena(cadena, separador):
    vector = cadena.split(separador)
    for element in vector:
        print(element)
        
#Problema 4 | Repetidor de cadena
def repetirCadena(cadena, veces):
    for i in range(veces):
        print(cadena)
        
                