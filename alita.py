# Alita Broaster
import os
import time

ala = [5]
pierna = [3]
encuentro = [5]
pecho = [5]
arroz = [4]
ensalada = [4]
papas = [5]
mayonesa = [3]
mostaza = [2]
ketchup = [4]
tartara = [4]
ganancia = [3]

def menu_principal():
	os.system ("cls")
	print("Bienvenidos a la tiendita del Sabor")
	print("====================================")
	print("1. Almacen")
	print("2. Venta")
	print("3. Salir")
	respuestaPrincipal = int(input("Que opcion elige: "))
	if respuestaPrincipal == 1:
		almacen()
	elif respuestaPrincipal == 2:
		menu_venta()
	elif respuestaPrincipal == 3:
		exit()
	else:
		print("Opcion Incorrecta, vuelva a ingresar")
		menu_principal()

def almacen():
	os.system ("cls")
	print("Bienvenidos al almacen:")
	print("======================")
	print("1. Agregar insumos")
	print("2. Listar insumos")
	print("3. Regresar al menu principal")
	respuestaAlmacen = int(input("Que opcion elige: "))
	if respuestaAlmacen == 1:
		menu_agregar()
	elif respuestaAlmacen == 2:
		listarInsumos()
	elif respuestaAlmacen == 3:
		menu_principal()
	else:
		print("Opcion Incorrecta, vuelva a ingresar")
		almacen()

def menu_agregar():
	os.system ("cls")
	print("Seleccione el insumo que va agregar:")
	print("====================================")
	print("1. Ala")
	print("2. Pierna")
	print("3. Encuentro")
	print("4. Pecho")
	print("5. Arroz")
	print("6. Ensalada")
	print("7. Papas")
	print("8. Mayonesa")
	print("9. Mostaza")
	print("10. Ketchup")
	print("11. Tartara")
	print("12. Regresar al menu del Almacen")
	respuestaAgregar = int(input("Que opcion elige: "))
	if respuestaAgregar == 1:
		cantidadAla = int(input("Cantidad: "))
		ala[0] = ala[0] + cantidadAla
		menu_agregar()
	elif respuestaAgregar == 2:
		cantidadPierna = int(input("Cantidad: "))
		pierna[0] = pierna[0] + cantidadPierna
		menu_agregar()
	elif respuestaAgregar == 3:
		cantidadEncuentro = int(input("Cantidad: "))
		encuentro[0] = encuentro[0] + cantidadEncuentro
		menu_agregar()
	elif respuestaAgregar == 4:
		cantidadPecho = int(input("Cantidad: "))
		pecho[0] = pecho[0] + cantidadPecho
		menu_agregar()
	elif respuestaAgregar == 5:
		cantidadArroz = int(input("Cantidad: "))
		arroz[0] = arroz[0] + cantidadArroz
		menu_agregar()
	elif respuestaAgregar == 6:
		cantidadEnsalada = int(input("Cantidad: "))
		ensalada[0] = ensalada[0] + cantidadEnsalada
		menu_agregar()
	elif respuestaAgregar == 7:
		cantidadPapas = int(input("Cantidad: "))
		papas[0] = papas[0] + cantidadPapas
		menu_agregar()
	elif respuestaAgregar == 8:
		cantidadMayonesa = int(input("Cantidad: "))
		mayonesa[0] = mayonesa[0] + cantidadMayonesa
		menu_agregar()
	elif respuestaAgregar == 9:
		cantidadMostaza = int(input("Cantidad: "))
		mostaza[0] = mostaza[0] + cantidadMostaza
		menu_agregar()
	elif respuestaAgregar == 10:
		cantidadKetchup = int(input("Cantidad: "))
		ketchup[0] = ketchup[0] + cantidadKetchup
		menu_agregar()
	elif respuestaAgregar == 11:
		cantidadTartara = int(input("Cantidad: "))
		tartara[0] = tartara[0] + cantidadTartara
		menu_agregar()
	elif respuestaAgregar == 12:
		almacen()
	else:
		print("Opcion Incorrecta, vuelva a ingresar")
		menu_agregar()

def listarInsumos():
	print("Inventario")
	print("===========")
	sumaAla = sum(ala)
	sumaPierna = sum(pierna)
	sumaEncuentro = sum(encuentro)
	sumaPecho = sum(pecho)
	sumaArroz = sum(arroz)
	sumaEnsalada = sum(ensalada)
	sumaPapas = sum(papas)
	sumaMayonesa = sum(mayonesa)
	sumaMostaza = sum(mostaza)
	sumaKetchup = sum(ketchup)
	sumaTartara = sum(tartara)
	print("Alas:",sumaAla)
	print("Piernas:",sumaPierna)
	print("Encuentros:",sumaEncuentro)
	print("Pecho:",sumaPecho)
	print("Arroz:",sumaArroz)
	print("Ensalada:",sumaEnsalada)
	print("Papas:",sumaPapas)
	print("Mayonesa:",sumaMayonesa)
	print("Mostaza:",sumaMostaza)
	print("Ketchup:",sumaKetchup)
	print("Tartara:",sumaTartara)
	regreso = input("Presiona la letra 's' para regresar: ")
	if regreso == 's' or regreso == 'S':
		menu_agregar()
	else:
		listarInsumos()	

def menu_venta():
	os.system ("cls")
	print("Bienvenidos al modulo de Ventas:")
	print("================================")
	print("1. Alita")
	print("2. Pierna")
	print("3. Encuentro")
	print("4. Pecho")
	print("3. Regresar al menu principal")
	respuestaVenta = int(input("Que opcion elige: "))
	if respuestaVenta == 1:
		alitaVenta()
	elif respuestaVenta == 2:
		piernaVenta()
	elif respuestaVenta == 3:
		encuentroVenta()
	elif respuestaVenta == 4:
		pechoVenta()
	elif respuestaVenta == 5:
		menu_principal()
	else:
		print("Opcion Incorrecta, vuelva a ingresar")
		menu_venta()

def alitaVenta():
	os.system ("cls")
	if ala[0] > 0 and arroz[0] > 0 and papas[0] > 0:
		ala[0] = ala[0] - 1
		venta()
	else:
		print("No cuentas con los insumos necesarios.")
		menu_principal()

def piernaVenta():
	os.system ("cls")
	if pierna[0] > 0 and arroz[0] > 0 and papas[0] > 0:
		pierna[0] = pierna[0] - 1
		venta()
	else:
		print("No cuentas con los insumos necesarios.")
		menu_principal()

def encuentroVenta():
	os.system ("cls")
	if encuentro[0] > 0 and arroz[0] > 0 and papas[0] > 0:
		encuentro[0] = encuentro[0] - 1
		venta()
	else:
		print("No cuentas con los insumos necesarios.")
		menu_principal()

def pechoVenta():
	os.system ("cls")
	if pecho[0] > 0 and arroz[0] > 0 and papas[0] > 0:
		pecho[0] = pecho[0] - 1
		venta()
	else:
		print("No cuentas con los insumos necesarios.")
		menu_principal()
		
def venta():
	arroz[0] = arroz[0] - 1
	ar = 1
	papas[0] = papas[0] - 1
	pa = 1
	if ensalada[0] > 0:
		preguntaEnsalada = input("Con ensalada? (s/n): ")
		if preguntaEnsalada == 's':
			ensalada[0] = ensalada[0] - 1
			en = 1
		else:
			ensalada[0] = ensalada[0]
			en = 0
	else:
		print("No cuentas con ensalada")
	if mayonesa[0] > 0 and mostaza[0] > 0 and ketchup[0] > 0 and tartara[0] > 0:
		preguntaMayonesa = input("Mayonesa? (s/n): ")
		if preguntaMayonesa == 's':
			mayonesa[0] = mayonesa[0] - 1
			ma = 1
		else:
			mayonesa[0] = mayonesa[0]
			ma = 0
		preguntaMostaza = input("Mostaza? (s/n): ")
		if preguntaMostaza == 's':
			mostaza[0] = mostaza[0] - 1
			mo = 1
		else:
			mostaza[0] = mostaza[0]
			mo = 0
		preguntaKetchup = input("Ketchup? (s/n): ")
		if preguntaKetchup == 's':
			ketchup[0] = ketchup[0] - 1
			ke = 1
		else:
			ketchup[0] = ketchup[0]
			ke = 0
		preguntaTartara = input("Tartara? (s/n): ")
		if preguntaTartara == 's':
			tartara[0] = tartara[0] - 1
			ta = 1
		else:
			tartara[0] = tartara[0]
			ta = 0
	else:
		print("No cuentas con cremas.")
	print("Pedido enviado")
	time.sleep(2)
	menu_principal()
	
menu_principal()



