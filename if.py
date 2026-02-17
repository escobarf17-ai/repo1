
num1 = 2
num2 = 7

if num1 < num2:
    print("el primer numero es menor que el segundo numero")
else:
    print("el segundo numero es mayor que el primer numero")

#mayor igual >=
#Menor igual <=
# == igual
#!= diferente de
# and or not


print("Eres mayor de edad? ")

edad = int(input("Ingresa tu edad "))

if edad > 18 and edad < 50:
    print("eres mayor de edad ")
elif edad < 18:
    print("eres menor de edad ")
elif edad > 50:
    print("Abuelo ")    
        