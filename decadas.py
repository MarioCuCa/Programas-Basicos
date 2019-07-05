print("Vamos a calcular a separar por milenio, siglos, decadas, lustros")
cantidad = int(input("Digita la cantidad de años a calcular: "))

if cantidad < 5:
	print("Contiene",cantidad,"años")
elif cantidad >= 5 and cantidad < 10:
	annos = cantidad - 5
	print("Contiene 1 lustro y",annos,"años")
elif cantidad >= 10 and cantidad < 100:
	decadas = cantidad//10
	lustros = (cantidad%10)//5
	annos = (cantidad%10)%5
	print("Contiene",decadas,"decadas",lustros,"lustros y",annos,"años")
elif cantidad >= 100 and cantidad < 1000:
	siglos = cantidad//100
	decadas = (cantidad%100)//10
	lustros = ((cantidad%100)%10)//5
	annos = ((cantidad%100)%10)%5
	print("Contiene",siglos,"siglos",decadas,"decadas",lustros,"lustros",annos,"años")
else:
	milenio = cantidad//1000
	siglos = (cantidad%1000)//100
	decadas = ((cantidad%1000)%100)//10
	lustros = (((cantidad%1000)%100)%10)//5
	annos = (((cantidad%1000)%1000)%10)%5
	print("Contiene",milenio,"milenios",siglos,"siglos",decadas,"decadas",lustros,"lustros y",annos,"años")