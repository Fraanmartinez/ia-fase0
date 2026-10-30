nombre = input("¿Cómo te llamas? ")
edad = int(input("Cuántos años tenés? "))

print(f"Hola, {nombre}.")

if edad < 12:
	print(f"Categoría: Niño/a")

elif edad >= 12 and edad <=17:
	print(f"Categoría: Adolescente")

elif edad >=18 and edad <=64:
	print(f"Categoría: Adulto/a")

else:
	print(f"Categoría: Adulto/a mayor")
