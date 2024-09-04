#Ejercicio 5
 
#Una persona debe realizar un muestreo con 50 personas para determinar el
#promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona. 

niños = 0
jovenes = 0
adultos = 0
ancianos = 0
total_niños = total_jovenes = total_adultos = total_ancianos = 0

for _ in range(50):
    edad = int(input("Ingrese la edad:"))
    peso = float(input("ingrese el peso:"))

    if 0 <= edad <= 12:
        niños += 1
        total_niños += peso 
    elif 13 <= edad <= 29:
        jovenes += 1
        total_jovenes += peso
    elif 30 <= edad <= 59:
        adultos += 1
        total_adultos += peso
    else:    
        ancianos += 1
        total_ancianos += peso

if niños > 0:
    print(f"Promedio de peso de niños:{total_niños/niños}")
if jovenes > 0:
    print(f"Promedio de peso de jovenes:{total_jovenes/jovenes}")
if adultos > 0:
    print(f"Promedio de peso de adultos:{total_adultos/adultos}")
if ancianos > 0:
    print(f"Promedio de peso de ancianos:{total_ancianos/ancianos}")                    