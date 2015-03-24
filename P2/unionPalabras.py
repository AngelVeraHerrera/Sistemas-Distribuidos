
#Segundo ejercicio de seminarios del grupo numero 4.
#Jose Crespo Guerrero y Jose Carlos Montanez Aragon

#Metodo de lectura del fichero.
#Se abre el fichero, se lee, posteriormente se eliminan los
#caracteres de salto de linea y de retorno de cargo y se divide
#la cadena en una lista con todas las palabras
def leerFichero(fichero):
	fich = open(fichero, 'r')
	lista = fich.read()
	lista = lista.replace('\n', '')
	lista = lista.replace('\r', '')
	lista = lista.split(' ')
	return lista

#Metodo que, dado una lista de palabras, busca la secuencia 
#de mayor longitud haciendo palabras encadenadas
def crearPalabras(lista):
	lista_final = []

	#Iteramos por cada palabra de la lista y generamos la secuencia
	for i in lista:
		lista_auxiliar = [i]

		#Para ir guardando el elemento sobre el que se esta comparando
		temp = i

		#Comparamos con todos los elementos
		j = -1
		while j < len(lista)-1:
			j += 1

			#Si no esta en la lista, comprobamos
			if lista[j] not in lista_auxiliar:

				#Si la condicion se cumple, se inserta y se
				#actualiza el elemento comparador
				if lista[j][0] == temp[-1]:
					lista_auxiliar.append(lista[j])
					temp = lista[j]
					j = -1
			
		#Guardamos la nueva lista si es de mayor longitud
		if len(lista_auxiliar) > len(lista_final):
			lista_final = lista_auxiliar

	return lista_final


array = leerFichero('pokemon.txt')
array = crearPalabras(array)
print(array)

