#Declaración de variables
igv = 1.18
subtotal = float()
total = float()
#Variable multilínea que guarda la carta de desayuno y almuerzo
carta = '''
|=============================|
| A |Café             |S/4.50 |
| B |Chocolate        |S/5.00 |
| C |Jugo de Fresas   |S/9.00 |
| D |Jugo de Papaya   |S/8.00 |
| E |Pan con Pollo    |S/7.00 |
| F |Pan con Jamón    |S/7.00 |
| G |Pan con Tortilla |S/7.00 |
| J |========= SALIR =========|
|=============================|
'''
#Variable multilínea que guarda la carta de la cena
cena = '''
|            Cena             |
|=============================|
| A |Pizza Exprés     |S/9.50 |
| B |Ensalada Campera |S/7.50 |
| C |Gazpacho         |S/6.00 |
| D |Caldo de Gallina |S/6.00 |
| E |Pollo al horno   |S/5.50 |
| F |Menestrón        |S/4.00 |
| G |========= SALIR =========|
|=============================|
'''
#Inicializando variables booleanas
respuesta1 = True
respuesta2 = True
#Primera estructura repetitiva que evalúa las opciones principales
while respuesta1 :
    print("|===========================|")
    print("|        RESTAURANTE        |")
    print("|===========================|")
    print("|A | Desayuno               |")
    print("|B |Almuerzo                |")
    print("|C |Cena                    |")
    print("|D |======== SALIR =========|")
    #variable que guarda la opción ingresada
    op1 = input("Elija una opción: ")
    
    #Condicional que evalúa si la opción elegida es D(salir)
    if (op1 == "D" or op1 =="d"):
        print("programa terminado...")
        break #termina el primer ciclo(while)
    
    #Segunda estructura repetitiva que evalúa las cartas(desayuno, almuerzo, cena)
    while respuesta2 :
        #Condicional que evalúa si ha elegido desayuno o almuerzo
        if op1 == "A" or op1 == "a" or op1 == "B" or op1 == "b": #DESAYUNO y ALMUERZO
            if (op1 == "A" or op1 == "a"):
                print('|            Desayuno         |')
            else:
                print('|          Almuerzo           |')
            
            #variable que guarda la opción ingresada
            op2 = input(carta) 
            
            if(op2 == "A" or op2 == "a"): #cafe
                subtotal+= 4.50
            if(op2 == "B" or op2 == "b"): #chocolate
                subtotal += 5.00
            if(op2 == "C" or op2 == "c"): #jugo de fresas
                subtotal+= 9.00
            if(op2 == "D" or op2 == "d"): #jugo de papaya
                subtotal+=8.00
            if(op2 == "E" or op2 == "e" or op2 =="F" or op2 == "f" or op2 == "G" or op2 == "g"): #Pan con Pollo, Pan con Jamón, Pan con tortilla
                subtotal+=7.00
            if(op2 == "J" or op2 == "j"): #salir
                break
            print(f'compra añadida, escogió la opción {op2}' )
            
            #variable que guarda la respuesta del usuario
            rpt = input("¿Desea seguir comprando? (S/N): ")
            
            #condicional que evalúa si su respuestas es Si o No
            if (rpt == "S" or rpt == "s"):
                respuesta2 = True #Cuando es SI
            else:
                respuesta2 = False #Cuando es NO
        
        #Condicional que evalúa si ha elegido Cena
        elif(op1 == "C" or op1 == "c"):
            op2 = input(cena)
            if(op2 == "A" or op2 == "a"):#pizza exprés 
                subtotal += 9.50 
            if(op2 == "B" or op2 == "b"): #ensalada campera
                subtotal += 7.50
            if(op2 == "C"  or op2 == "c" or op2 =="D" or op2 == "d"): # gazpacho, caldo de gallina
                subtotal+= 6.00
            if(op2 == "E" or op2 == "e"): #pollo al horno
                subtotal+=5.50
            if(op2 == "F" or op2 == "f"): #menestrón
                subtotal+=4.00
            if(op2 == "G" or op2 == "g"): #salida
                break #termina el segundo ciclo(while)
            
            print(f'compra añadida, escogió la opción {op2}' )
           
            #variable que guarda la respuesta del usuario
            rpt = input("¿Desea seguir comprando? (S/N): ")
            if (rpt == "S" or rpt == "s"):
                respuesta2 = True
            else:
                respuesta2 = False
    #condicional que evalúa si en el menú se ha elegido la opción salir
    if (op2 == "J" or op2 == "j" or op2 == "G" or op2 == "g"):
        print("programa terminado...")
        break #termina el primer ciclo(while)
    
    #Suma del subtotal con el igv
    total = subtotal + igv 
    
    #Muestra de la boleta de ventas
    print("|       BOLETA DE VENTAS      |")
    print("|=============================|")
    print("| Subtotal     : "+ str(subtotal))
    print("| Igv          : "+ str(igv) )
    print("| Total a pagar: "+ str(total))
    #variable que guarda la respuesta del usuario
    rpt = input("¿Desea hacer otra boleta de venta? (S/N): ")
    if (rpt == "S"):
        respuesta1 = True
    else:
        respuesta1 = False