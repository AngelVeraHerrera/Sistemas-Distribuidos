import os

operaciones = ['+', '-', '/', '*']

def main():
	global x
	calculo = raw_input("Introduzca la operacion: ")
	for it in operaciones:
		if it in calculo:
			partes = calculo.split(it)
			print partes

main()
