#Ejercicio 3

#Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
#Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja
#de todo el grupo. 

calificaciones = []

for _ in range(20):
    calificacion = float(input("Ingrese la calificacion:"))
    calificaciones.append(calificacion)

promedio = sum(calificaciones)/len(calificaciones)
max_calificacion = max(calificaciones)
min_calificacion = min(calificaciones)

print(f"Promedio:{promedio}")
print(f"Calificacion mas alta:{max_calificacion}")
print(f"Calificacion mas baja:{min_calificacion}")