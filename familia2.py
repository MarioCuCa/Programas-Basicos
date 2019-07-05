print("Vamos a practicar Funciones")

familia = []

def agregarFam():
	nombre = input("Nombre:")
	familia.append(nombre)
	
def listarFam():
	print("Miembros:")
	for nombre in familia:
		print(nombre)

valor = 1
while valor == 1:
	respuesta = input("Desea ingresar a alguien mas? ")
	if respuesta == 's' or respuesta == 'S':
		agregarFam()
		valor = 1
	elif respuesta == 'n' or respuesta == 'N':
		valor = 0

listarFam()


			


