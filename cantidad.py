print("Vamos a listar y contar la cantidad de familiares")

familia = []

def agregar():
	nombre = input("Nombre: ")
	familia.append(nombre)

def listar():
	print("Miembros:")
	for nombre in familia:
		print(nombre)

cantidad = 0
valor = 1
while valor == 1:
	respuesta = input("Deseas agregar a alguien mas (s/n)? ")
	if respuesta == 's' or respuesta == 'S':
		cantidad = cantidad + 1
		valor = 1
		agregar()
	else:
		valor = 0
		listar()

print("Cantidad:",cantidad)
