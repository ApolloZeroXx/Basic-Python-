# Funciones 
print("\n>>>>>>>>>>>> Funciones <<<<<<<<<<<<<\n")


#Ejemplo 1 
print(">>>>>>>>>>>> Ejemplo N1 <<<<<<<<<<<<<\n")

def saludo():
    print("Hola, ¿como has estado?\n")

saludo()


#Ejemplo 2
print(">>>>>>>>>>>> Ejemplo N2 <<<<<<<<<<<<<\n")

def multiplicacion(A,B):
    print("Multiplicacion de 5*5")
    return A*B

print (f"El resultado de la multiplicacion es: {multiplicacion(5, 5)}\n")


#Ejemplo 3 
print(">>>>>>>>>>>> Ejemplo N3 <<<<<<<<<<<<<\n")

nota= 8
def Aprobacion(nota):
    print("El estudiante tiene un 8\n")
    Valor="Aprobado"
    if 6>nota:
        valor="Reprobado"
    return Valor

print(Aprobacion(int(nota)))


# Default Parameters 
print("\n\n>>>>>>>>>>>> Default Parameters  <<<<<<<<<<<<<\n")


# Ejemplo 1
print(">>>>>>>>>>>> Ejemplo 1 <<<<<<<<<<<<<\n")
def suma(num1 = 0, num2 = 0):
    return num1 + num2


print(f'suma {suma(21, 13)}')
print(f'suma {suma(9)}')

#Ejemplo 2
print("\n>>>>>>>>>>>> Ejemplo 2 <<<<<<<<<<<<<\n")

def gastos(servicios = 500, renta = 2100, comida = 700):
    return renta + comida + servicios

print(f"los gastos totales son: {gastos(500)}\n")


#Ejemplo 3
print("\n>>>>>>>>>>>> Ejemplo 3 <<<<<<<<<<<<<\n")

def nombre(apellido, nombre = "Roberto"):
      print (f"{nombre} {apellido}")

nombre("Rosales")

# Keyword Arguments 
print("\n>>>>>>>>>>>> Keyword Arguments  <<<<<<<<<<<<<\n")

#Ejemplo 1 
print(">>>>>>>>>>>> Ejemplo N1 <<<<<<<<<<<<<\n")

def nombre (Nombre, Apellido):
    print(f"{Nombre} {Apellido}")

nombre(Nombre="Roberto", Apellido="Rosales")

#Ejemplo 2 
print("\n>>>>>>>>>>>> Ejemplo N2 <<<<<<<<<<<<<\n")

def division (dividendo, divisor):
    return dividendo/divisor 

print(f"El resultado de la division es: {division(dividendo=100,divisor=2)}")

#Ejemplo 3 
print("\n>>>>>>>>>>>> Ejemplo N3 <<<<<<<<<<<<<\n")

def area_cuadrado (lado):
    return lado**2

print(f"El area del cuadrado es: {area_cuadrado(33)} m2")
