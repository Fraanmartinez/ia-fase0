nombre = input("¿Cómo te llamás? ")
edad_texto = input("¿Cuántos años tenés? ")
edad = int(edad_texto)

print(f"Hola, {nombre}.")

if edad >= 18:
	print("Sos mayor de edad.")

else:
	print(f"Te faltan {18 - edad} años para ser mayor de edad.")