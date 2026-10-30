nombre = "Ana"
edad = 28
altura = 1.65
es_estudiante = True

print(nombre, type(nombre))
print(edad, type(edad))
print(altura, type(altura))
print(es_estudiante, type(es_estudiante))

print(f"{nombre} tiene {edad} años y mide {altura} m")

if edad >= 18:
	print("Es mayor de edad")
else:
	print("Es menor de edad")

if es_estudiante and edad <30:
	print("Entra en el descuento joven")