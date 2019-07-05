print("Ahora vamos a comparar 3 numero")
numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))

if numero1 > numero2 and numero2 > numero3:
	print(numero1,">",numero2,">",numero3)
elif numero1 > numero3 and numero3 > numero2:
	print(numero1,">",numero3,">",numero2)
elif numero2 > numero1 and numero1 > numero3:
	print(numero2,">",numero1,">",numero3)
elif numero2 > numero3 and numero3 > numero1:
	print(numero2,">",numero3,">",numero1)
elif numero3 > numero1 and numero1 > numero2:
	print(numero3,">",numero1,">",numero2)
else:
	print(numero3,">",numero2,">",numero1)