#Ejercicio 7

#La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad
#de Ibagué, cuantos entran con calcomanía de cada color.

n = int(input("Ingrese el numero de datos que entraron a la ciudad:"))
colores = {'Amarillo':0,'Rosa':0,'Rojo':0,'Verde':0,'Azul':0}

for _ in range(n):
    ultimo_digito = int(input("Ingrese el ultimo digito de la placa:"))
if ultimo_digito in [1,2]:
    colores['Amarillo'] += 1
elif ultimo_digito in [3,4]:
    colores['Rosa'] += 1
elif ultimo_digito in [5,6]:
    colores['Rojo'] += 1
elif ultimo_digito in [7,8]:
    colores['Verde'] += 1
elif ultimo_digito in [9,0]:
    colores['Azul'] += 1

for color, cantidad in colores.items():
    print(f"Color {color}:{cantidad}")