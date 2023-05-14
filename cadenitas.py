#Calculadora de Fernando Alania Atoche u22311364.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b


print("¡Bienvenido a la calculadora en Python!")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")


opcion = int(input("Selecciona una opción (1(Suma)/2(Resta)/3(Multiplicación)/4(División)): "))


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

#Posibles operaciones dependiendo de lo que elija el usuario
if opcion == 1:
    resultado = suma(num1, num2)
elif opcion == 2:
    resultado = resta(num1, num2)
elif opcion == 3:
    resultado = multiplicacion(num1, num2)
elif opcion == 4:
    resultado = division(num1, num2)
#Si pone un dato inválido
else:
    print("Opción inválida")


print("El resultado es:", resultado)
  

