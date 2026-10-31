edad = -1

while edad < 0 or edad > 120:
    edad = int(input("Ingresa tu edad (0 a 120): "))
    if edad < 0 or edad > 120:
        print("Edad inválida, probá de nuevo.")
        
print(f"Edad registrada: {edad}")