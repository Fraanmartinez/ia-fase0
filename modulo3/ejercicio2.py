edad = -1

while edad < 0 or edad > 120:
    edad = int(input("Ingresa tu edad (0 a 120) "))
    if edad < 0:
        print("Error. La edad debe ser 0 o mayor. ")
    elif edad > 120:
        print("Error. La edad debe ser 120 o menor. ")
        
if edad < 12:
    print("Clasificación: Niño/a")
        
elif edad < 18:
    print("Clasificación: Adolescente")
        
elif edad < 65:
    print("Clasificación: Adulto/a")
        
else:
    print("Clasificación: Adulto/a mayor")