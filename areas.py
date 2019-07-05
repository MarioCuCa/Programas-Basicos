print("Proyecto final, calcularemos las areas de figuras geometricas:")
print("ELiga la figura geometrica que desea hallar su area")
print("1. Cuadrado")
print("2. Triangulo")
print("3. Circulo")
print("4. Rectagulo")
print("5. Trapecio")

eleccion = int(input("Que numero selecciona?: "))

if eleccion==1:
	altura = int(input("Altura: "))
	base = int(input("Base: "))
	area = altura * base
	print("Area del Cuadrado es",area)
if eleccion==2:
	altura = int(input("Altura: "))
	base = int(input("Base: "))
	area = (altura*base)/2
	print("Area del Triangulo es",area)
if eleccion==3:
	radio = int(input("Radio: "))
	area = 3.14*radio
	print("Area del Circulo es",area)
if eleccion==4:
	altura = int(input("Altura: "))
	base = int(input("Base: "))
	area = altura * base
	print("Area del Rectagulo es",area)
if eleccion==5:
	altura = int(input("Altura: "))
	baseinf = int(input("Base Inferior: "))
	basesup = int(input("Base Superior: "))
	area = ((basesup+baseinf)/2)*altura
	print("Area del Trapecio ess",area)
