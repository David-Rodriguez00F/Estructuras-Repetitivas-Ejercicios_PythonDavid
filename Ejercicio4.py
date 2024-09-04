#Ejercicio 4

#Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se
#digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.

numero = int(input("Ingrese un numero para la tabla de multiplicar:"))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")