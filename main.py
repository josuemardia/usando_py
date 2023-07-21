#This is a main script or that i want xd

#Encontrar el numero faltante
def FindFaltante():
    vector = [1,2,3,5,6,7]
    item = 0
    for i in vector:
        item += 1
        if i is not item:
            return print(f'El número faltante de la lista de números es: {i}')
    return print(f'No se ha encontrado un numero faltante')

#Rotar una matriz 90 grados con sentido horario
def RotarMatriz():
    matriz = [[0, 1, 0],
              [0, 1, 0],
              [0, 1, 0]]
    newMatriz =[[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    i = 0; j = 2
    k = 0; m = 0
    for i in range(3):
        k = 0; j = 2
        for  k in range(3):
            newMatriz[k, m] = matriz[i, j]
            j -= 1
            k += 1
        i += 1
        m += 1

    return print(f'La matriz invertida es:')     
            

