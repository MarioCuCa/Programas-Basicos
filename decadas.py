#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  decadas.py
#  


print("Vamos a calcular a separar por milenio, siglos, decadas, lustros")
cantidad = int(input("Digita la cantidad de años a calcular: "))

milenios = cantidad / 1000
resto_milenios = cantidad % 1000
siglos = resto_milenios / 100
resto_siglos = resto_milenios % 100
decadas = resto_siglos / 10
resto_decadas = resto_siglos % 10
lustros = resto_decadas / 5
anios = resto_decadas % 5
lista = []

if milenios:
	lista.append(str(milenios) + " milenio(s)")
	
if siglos:
	lista.append(str(siglos) + " siglo(s)")
	
if decadas:
	lista.append(str(decadas) + " decada(s)")

if lustros:
	lista.append(str(lustros) + " lustros(s)")
	
if anios:
	lista.append(str(anios) + " años(s)")


print("Contiene %s" % ", ".join(lista))
