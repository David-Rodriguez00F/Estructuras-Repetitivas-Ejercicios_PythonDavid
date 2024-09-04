#Ejercicio 2

#Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
#numeros.

suma_positivos = 0

for _ in range(10):
    numero = int(input("Ingrese un numero negativo:"))
    if numero < 0:
        numero = abs(numero)
    suma_positivos += numero

print(f"La suma de los numeros convertidos a positivos es:{suma_positivos}")        