#Ejercicio 6

#Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un
#total de n personas.

n = int(input("Ingrese el numero total de personas en el salon:"))
hombres = 0
mujeres = 0

for _ in range(n):
    sexo = input("Ingrese el sexo(H/M):").upper()
    if sexo == 'H':
        hombres += 1
    elif sexo == 'M':
        mujeres += 1

print(f"Hombres:{hombres}")
print(f"Mujeres:{mujeres}")