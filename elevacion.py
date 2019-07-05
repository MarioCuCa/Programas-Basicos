print("Vamos a elevar un numero al numero de eligas")
numero = int(input("Numero a elevar: "))
elevador = int(input("Cantidad a elevar: "))

numero2 = numero

for cantidad in range(1,elevador):
	nuevo = numero2*numero
	numero2 = nuevo

print(nuevo)
