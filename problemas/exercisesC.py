#-------------------- U9 ---------------------
#Ejercicio 1
print("Hola mundo")

#Ejercicio 2
PI = 3.14
print("el valor de PI es: "+ PI)

#Ejercicio 3
print("hola mi nombre es Juan")

#Ejercicio 4
num1 = 5
num2 = 8
suma = num1 + num2
print("La suma de "+num1+ " y "+num2+" es: "+suma)

#Ejercicio 5
num1 = 12
num2 = 6
division = num1/num2
print("La division de "+num1+ " y "+num2+" es: "+division)

#Ejercicio 6
edad = int(input("Ingresa tu edad: "))
print("Tu edad ingresada es: " + edad)

#Ejercicio 7
nombre = input("Ingrese su nombre, por favor: ")
edad = int(input("Ingrese su edad, por favor: "))
print("El nombre del trabajador es: "+nombre)
print("La edad del trabajador es: "+edad)

#Ejercicio 8
num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero: "))
suma = num1+num2
print("La suma de los números "+num1 +" y "+ num2+" es: "+suma)

#Ejercicio 9
apellidos = input("Ingrese sus apellidos, por favor: ")
edad = int(input("Ingrese su edad, por favor: "))
DNI = int(input("Ingrese su DNI, por favor: "))

print("Su apellido es: " + apellidos)
print("Su edad es: " + edad)
print("Su DNI es: " + DNI)

#Ejercicio 10
miNombre = "Caleb"
miEdad = 18

print("Mi "+miNombre+ " mi "+miEdad)

#-------------------- U10 ---------------------

#Ejercicio 1
edad = 12

if (edad >= 18):
    print("Es un adulto")
else:
    print("No es un adulto")
    
#Ejercicio 2
edad = int(input("Ingresa tu edad: "))

if (edad >= 18):
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
    
#Ejercicio 3
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if(num1 == num2):
    print(num1 +" y "+num2+ " son iguales")
else:
    print(num1 +" y "+num2+ " no son iguales")
    
#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if (edad >= 6 and edad <= 11):
    print("Niñez (6-11)")

if(edad >= 12 and edad <= 18):
    print("Adolescencia (12-18)")
    
if (edad >= 18 and edad <= 26):
    print("Juventud (18-26)")

if (edad >=27 and edad <= 59):
    print("Adultez (27-59)")
     
if (edad >=60):
    print("Vejez (60 a más)")
    
#Ejercicio 5
mes = int(input("Ingrese un numero(mes) del año(1-12): "))

if(mes < 1 or mes > 12):
    print("Valor inválido, solo se aceptan del 1-12")
else:
    if(mes == 1):
        print("El numero "+ mes + " es igual a Enero")
    if(mes == 2):
        print("El numero "+ mes + " es igual a Febrero")
    if(mes == 3):
        print("El numero "+ mes + " es igual a Marzo")
    if(mes == 4):
        print("El numero "+ mes + " es igual a Abril")
    if(mes == 5):
        print("El numero "+ mes + " es igual a Mayo")
    if(mes == 6):
        print("El numero "+ mes + " es igual a Junio")
    if(mes == 7):
        print("El numero "+ mes + " es igual a Julio")
    if(mes == 8):
        print("El numero "+ mes + " es igual a Agosto")
    if(mes == 9):
        print("El numero "+ mes + " es igual a Septiembre")
    if(mes == 10):
        print("El numero "+ mes + " es igual a Octubre")
    if(mes == 11):
        print("El numero "+ mes + " es igual a Noviembre")
    if(mes == 12):
        print("El numero "+ mes + " es igual a Diciembre")
        
#Ejercicio 6
usuario = "cmarcilla"
password = "12345"

user = input("Ingrese su nombre de usuario: ")
contrasenna = input("Ingrese su contraseña: ")

if(user == usuario and contrasenna == password):
    print("¡Bienvenido!")
else:
    print("Inténtelo de nuevo")
    
#Ejercicio 7
year = int(input("Ingrese el año: "))

if( year%2 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

#Ejercicio 8
dia = int(input("Ingrese un numero(dia): "))

if(dia < 1 or mes > 7):
    print("Valor inválido, solo se aceptan del 1-7")
else:
    if(dia == 1):
        print("El numero "+ dia + " es igual a Lunes")
    if(dia == 2):
        print("El numero "+ dia + " es igual a Martes")
    if(dia == 3):
        print("El numero "+ dia + " es igual a Miércoles")
    if(dia == 4):
        print("El numero "+ dia + " es igual a Jueves")
    if(dia == 5):
        print("El numero "+ dia + " es igual a Viernes")
    if(dia == 6):
        print("El numero "+ dia + " es igual a Sábado")
    if(dia == 7):
        print("El numero "+ dia + " es igual a Domingo")
        
#Ejercicio 9
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if(num1 > num2):
    print("El numero mayor es "+num1)
else:
    print("El numero mayor es "+num2)
    
#Ejercicio 10
num = int(input("Ingrese un numero: "))
if(num%2 == 0):
    print("El numero "+num+ " es par")
else:
    print("El numero "+num+ " no es par")
    
    
#----------------------------------------------
#-------------------- U11 ---------------------
#----------------------------------------------

#Ejercicio 1
for i in range(101):
    print(i+1)
    
#Ejercicio 2
i=2
while i<=50:
    print(i)
    i+=2
    
#Ejercicio 3
num=1
for i in range(20):
    print(num)
    num+=2
    
#Ejercicio 4
while True:
    num = input("Ingrese un numero entero: ")
    if num.isdigit():
        print(num + " es un numero entero: ")
        break
    else:
        print(num+" no es un numero entero")

#Ejercicio 5
num = 1
for i in range(12):
    print("==== TABLA DEL " + str(num) + " ====")
    for j in range(13):
        print(str(num)+ "*" + str(j) + "=" + str(num*j))
    print("=======================")
    num += 1

#Ejercicio 6
u = "caleb"
p = "12345"
i = 0
while True:
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    i += 1
    if (user == u and password == p):
        print("¡Bienvenido!")
        break
    else:
        print("Autenticación incorrecta")
    
    if(i == 3):
        print("Sobrepasó todos sus intentos")
        break

#Ejercicio 7
edades = []
while True:
    edad = int(input("Ingrese una edad: "))
    edades.append(edad)
    rpt = input("¿Desea seguir agregando? (S/N): ")
    if (rpt == "N" or rpt == "n"):
        break
    
print(edades)

#Ejercicio 8
contador = 0
for i in edades:
    if i >= 18 :
        contador += 1
print("Las personas mayores de edad son: " + contador)

#Ejercicio 9
nombre = input("Ingresa tu nombre: ")
print("Tu nombre " + nombre + " tiene: " + str(len(nombre)) + " letras")

#Ejercicio 10
vClientes = []
numCliente = int(input("Ingresa la cantidad de clientes: "))
for i in range(numCliente):
    vClientes.append(input("Ingresa el nombre del "+ str(i+1) +" cliente: "))
print("Los clientes son: \n"+ str(vClientes))

#----------------------------------------------
#-------------------- U12 ---------------------
#----------------------------------------------

#Ejercicio 1
def miFuncion():
    print("¡Hola Mundo!")
    
miFuncion()

#Ejercicio 2
def Sumar():
    num1 = int(input("Escriba el primer numero: "))
    num2 = int(input("Escriba el segundo numero: "))
    suma = num1 + num2
    print("la suma de "+str(num1)+ " y "+str(num2)+" es: "+ str(suma))
    
Sumar()

#Ejercicio 3
def obtenerMayor():
    numeros = []
    mayor = 0
    while True:
        num = int(input("Ingrese un numero: "))
        numeros.append(num)
        mayor = max(numeros)
        print("Números agregados hasta el momento: "+ str(numeros))
        rpt = input("¿Desea continuar? (S/N)")
        if (rpt == "N" or rpt == "n"):
            print("El número mayor es: " + str(mayor))
            break

obtenerMayor()

#Ejercicio 4
def verificarNumCelular():
    celular = input("Ingrese su número de teléfono: ")
    if (len(celular) == 9):
        print("la entrada tiene 9 dígitos")
    else:
        print("la entrada no tiene 9 dígitos")
        
verificarNumCelular()

#Ejercicio 5
def saludo(nombre, apellido):
    print("Hola me llamo "+nombre+" "+apellido+" y tengo la edad de 38")

saludo()

#Ejercicio 6
def hallarAreaTriangulo():
    base = float(input("Ingresa la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    area = (base*altura)/2
    print("El area del triangulo es: " + str(area))
    
hallarAreaTriangulo()

#Ejercicio 7
def hallarAreaCuadrado():
    lado = float(input("Ingrese la medición del lado del triangulo: "))
    area = lado*lado
    print("El area del cuadrado es: " + str(area))

hallarAreaCuadrado()

#Ejercicio 8
def restarYears(year1, year2):
    resultado = abs(int(year1) - int(year2))   
    print("La diferencia de "+str(year1)+ " y "+str(year2)+ " es: "+str(resultado))

a1 = input("Ingrese el primer año: ")
a2 = input("Ingrese el segundo año: ")
restarYears(a1,a2)

#Ejercicio 9
def parOImpar(num):
    if (num.isdigit()):
        if(num%2 == 0):
            print("El numero "+str(num)+ " es par")
        else:
            print("El numero "+str(num)+ " es impar")
    else:
        print("Solo se permite números enteros")

numero = input("Ingrese un numero: ")
parOImpar(numero)

#Ejercicio 10
def promedio():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    promedio = (num1 + num2) /2
    print("El promedio de "+str(num1)+" y "+str(num2)+ " es: "+str(promedio))

promedio()

#----------------------------------------------
#-------------------- U13 ---------------------
#----------------------------------------------

#Ejercicio 1
print("=============================")
print("Notas de matemática (4 notas)")
matematica = (
    float(input("Ingrese la nota 1: ")),
    float(input("Ingrese la nota 2: ")),
    float(input("Ingrese la nota 3: ")),
    float(input("Ingrese la nota 4: "))
)
print("=============================")
print("Notas de comunicación (4 notas)")
comunicacion = (
    float(input("Ingrese la nota 1: ")),
    float(input("Ingrese la nota 2: ")),
    float(input("Ingrese la nota 3: ")),
    float(input("Ingrese la nota 4: "))
)
print("=============================")
print("Notas de computación (4 notas)")
computacion = (
    float(input("Ingrese la nota 1: ")),
    float(input("Ingrese la nota 2: ")),
    float(input("Ingrese la nota 3: ")),
    float(input("Ingrese la nota 4: "))
) 

#Ejercicio 2
sum1 = float(); sum2 = float(); sum3 = float()
for i in matematica:
    sum1 += i
print("El promedio de matemática es: "+ str(sum1/len(matematica)))

for i in comunicacion:
    sum2 += i
print("El promedio de comunicación es: "+ str(sum2/len(comunicacion)))
for i in computacion:
    sum3 += i
print("El promedio de computación es: "+ str(sum3/len(computacion)))

#Ejercicio 3
def numMayor():
    numeros = [] #inicializando la lista
    mayor = int()
    menor = int()
    for i in range(10):
        numeros.append(input("Ingresa el "+ str(i+1)+ "numero: "))
    
    tuplaNum = tuple(numeros)
    mayor = max(tuplaNum)
    menor = min(tuplaNum)
    print("Tupla \n"+tuplaNum)
    print("El numero mayor es: "+mayor)
    print("El numero menor es: "+menor)

#Ejercicio 4
cliente = {
    "nombre"   : input("Ingrese su nombre: "),
    "apellido" : input("Ingrese su apellido: "),
    "edad"     : input("Ingrese su edad: "),
    "deporte"  : input("Ingrese su deporte favorito")
}

#Ejercicio 5
if (cliente["deporte"] == "basquetbol"):
    print("Eres un buen jugador de basquetbol")


#----------------------------------------------
#-------------------- U14---------------------
#----------------------------------------------

#Ejercicio 1
import random
print(random.randint(1, 100))

#Ejercicio 2
num = []
for i in range(10):
    num.append(random.randint(1, 100))
    
#Ejercicio 3
numPares = list(filter(lambda x: x % 2 == 0, num))
print("los numero pares son: \n" + str(numPares))

#Ejercicio 4
numImpares = list(filter(lambda x: x % 2 != 0, num))
print("los numero impares son: \n" + str(numImpares))

#Ejercicio 5
import math
print(math.sqrt(15))

#Ejercicio 6
print(math.pow(3,2))

#Ejercicio 7
print(math.pow(2,3))
    
#----------------------------------------------
#-------------------- U15---------------------
#----------------------------------------------

#Ejercicio 1
class Persona:
    def comer(self):
        print("Comiendo...")
    def dormir(self):
        print("durmiendo...")
    def jugando(self):
        print("jugando...")

#Ejercicio 2
class vehiculo:
    class frenar:
        def frena(self):
            print("frenando...")
    class acelerar:
        def acelera(self):
            print("acelerando...")
    class girar:
        def gira(self):
            print("girando...")
            
#Ejercicio 3
class calculadora:
    def sumar(self):
        print("sumando...")
    def restar(self):
        print("restando...")
    def multiplicar(self):
        print("multiplicando...")
    def dividir(self):
        print("dividiendo...")
        
#Ejercicio 4
class computadora:
    def verSeries():
        print("viendo series...")
    def jugar(self):
        print("jugando...")  
    def estudiar(self):
        print("estudiando...")   
    def apagar(self):
        print("apagando...")   
    def prender(self):
        print("prendiendo...")   
    
#----------------------------------------------
#-------------------- U16----------------------
#---------------------------------------------- 

#Ejercicio 1
class vehiculo:
    def avanzar(self):
        print("Avanzando sobre 4 ruedas")
#Ejercicio 2
class camion (vehiculo):
    print("Heredando de superclase")
    
#Ejercicio 3
class camion (vehiculo):
    def avanzar(self):
        print("Avanzando sobre 6 ruedas")
    