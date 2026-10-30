nombre = input("¿Cómo te llamas? ")
edad = int(input("Cuántos años tenés? "))

print(f"Hola, {nombre}.")

if edad < 12:
	print("Categoría: Niño/a")
elif edad <=17:
	print("Categoría: Adolescente")
elif edad <=64:
    print("Categoría: Adulto/a")
else:
	print("Categoría: Adulto/a mayor")