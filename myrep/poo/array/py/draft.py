lista = [10, 20, 30, 40, 50]
x = 69

encontrado = False

for valor in lista:
    if valor == x:
        encontrado = True
        break

print(encontrado)   # True