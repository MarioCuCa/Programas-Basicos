print("Vamos a sumar o multiplicar todos los numeros que usted escribe")
cantidad = int(input("Cantidad de numeros: "))

lista = []

def agregar():
	numero = int(input("Numero: "))
	lista.append(numero)

def sumar(cantidad):
	i = 0
	nuevo = 0
	for cantidad in range (0,cantidad+1):
		nuevo = lista[i] + nuevo
		i = i + 1
	print("La suma es:",nuevo)

def multiplicacion(cantidad):
	i = 0
	nuevo = 1
	for cantidad in range (0,cantidad+1):
		nuevo = lista[i] * nuevo
		i = i + 1
	print("La multiplicacion es",nuevo)

for cantidad in range (0,cantidad):
	agregar()
	
print("Selecciona la accion a realizar")
print("1. Suma de todos los numeros")
print("2. Multiplicacion de todos los numeros")

opcion = int(input("Respuesta: "))

if opcion == 1:
	sumar(cantidad)
elif opcion == 2:
	multiplicacion(cantidad)
else:
	print("Opcion incorrecta")