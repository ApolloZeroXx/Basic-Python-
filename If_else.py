
#if else 
print(">>>>>>>>>>>> If Else <<<<<<<<<<<<<\n")

#ejemplo 1
print(">>>>>>>>>>>> Ejemplo N1 <<<<<<<<<<<<<\n")

calificacion = 9
if calificacion>=6:
    print(f"Aprobado, su caliciacion es un: {calificacion}\n")
else:
    print("Reprobado\n")

#ejemplo 2 
print(">>>>>>>>>>>> Ejemplo N2 <<<<<<<<<<<<<\n")

condicion = "certificado"
if condicion == "certificado":
    print("El alumno esta certificado\n")
else:
    print("El alumno no esta certificado\n")

#ejemplo 3
print(">>>>>>>>>>>> Ejemplo N3 <<<<<<<<<<<<<\n")

calificacion1 = 9
if calificacion1<6:
    print("No cumple con el resultado minimo")
elif calificacion1 == 6 or calificacion1<8:
    print("Cumple con el resultado minimo")
else: 
    print("Destaca en su resultado")

#operador ternario 
print(">>>>>>>>>>>> Operador Ternario <<<<<<<<<<<<<\n")

#ejemplo 1
print(">>>>>>>>>>>> Ejemplo N1 <<<<<<<<<<<<<\n")

condicion2 = "true"
print ("cumple con la condicion\n") if condicion2 == "true" else print ("No cumple con la condicion\n")


#ejemplo 2
print(">>>>>>>>>>>> Ejemplo N2 <<<<<<<<<<<<<\n")

Altura = 120
print("Puede entrar al juego mecanico\n") if Altura>130 else print("No puede entrar al juego mecanico\n")


#ejemplo 3
print(">>>>>>>>>>>> Ejemplo N3 <<<<<<<<<<<<<\n")

bateria = 20
print("Su bateria esta baja") if bateria<=15 else print("su bateria aun no esta baja")

#FOR LOOP WITH RANGE

#ejemplo 1
print(">>>>>>>>>>>> Ejemplo N1 <<<<<<<<<<<<<\n")


fecha=1999
años=0
for i in range(fecha, 2023,1):
    años= años+1

print(f"El usuario tiene {años} ")


#ejemplo 2
print(">>>>>>>>>>>> Ejemplo N2 <<<<<<<<<<<<<\n")

print("Tabla del 2")
for i in range (1,11):
    print(2*i)


#ejemplo 3
print(">>>>>>>>>>>> Ejemplo N3 <<<<<<<<<<<<<\n")
palabra = "ja"
for i in range(10):
    print(palabra)


#While
print("\n>>>>>>>>>>>> While <<<<<<<<<<<<<\n")

#ejemplo 1
print(">>>>>>>>>>>> Ejemplo N1 <<<<<<<<<<<<<\n")

j = 0
while fecha<2023:
    j=j+1
    fecha=fecha+1
print (f"El usuario tiene {j}")


#ejemplo 2
print(">>>>>>>>>>>> Ejemplo N2 <<<<<<<<<<<<<\n")

print("Tabla de multiplicar del 7")
k=1
while k<11:
    mult=k*7
    print(mult)
    k=k+1


#ejemplo 3
print(">>>>>>>>>>>> Ejemplo N3 <<<<<<<<<<<<<\n")

print("Calcular la cantidad de numeros naturales\n")
natural=0
n=int(input("Número (0 para terminar): "))
while n!=0:
    if n>0:
        natural+=1
    n=int(input("Número (0 para terminar): "))
print("Cantidad de positivos:", natural)

