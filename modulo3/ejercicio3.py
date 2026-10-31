total = 0

for numero in range(1,21):
    if numero % 2 == 0:
        total += numero
        
print(f"Total de sumar solo los números pares en un rango de 1 a 20: {total}")