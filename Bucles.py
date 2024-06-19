###Bucles
#Ejercicio 1
a = input("dime una palabra:" )
for _ in range (10):
    print(a)
##Ejercicio 2
age = int(input("¿Cuántos años tenes? ")) 
for i in range(age): 
    print("Has cumplido " + str(i+1) + " años")

##Ejercicio 3
n = int(input("Introducí un número entero positivo: ")) 
for i in range(1, n+1, 2): 
    print(i, end=", ")

##Ejercicio 4
n = int(input("Introducí un número entero positivo: ")) 
for i in range(n, -1, -1): 
    print(i, end=", ") 

