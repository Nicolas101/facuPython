import random

# Funciones

def armar_pal_separada(pal) :
	x = []
	for i in pal :
		x.append(['_ '])
	return x

def sigue(cant1,cant2,pal) :
    if cant1 == len(pal) :
        print('Ganaste!')
        return False
    elif cant2 == 3 :
        print('Perdiste!. La palabra era:', pal)
        return False
    else :
        return True

def mostrar_letra(pal_separada) :
	pal_imprime = ''
	for i in pal_separada :
		pal_imprime = pal_imprime + i[0]	
	print (pal_imprime)

def mostrar_ahorcado(cantidad_partes_cuerpo,ahorcado) :
	for i in range(cantidad_partes_cuerpo) :
		print(ahorcado[i])

# Preparo el juego

palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}

ahorcado = [' O ', '/|\\','/ \\']

tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))

pal = palabras[tema][random.randrange(len(palabras[tema]))]

pal_separada = armar_pal_separada(pal) # Funcion agregada

print ('- '*len(pal))

cantidad_letras_adivinadas = 0
cantidad_partes_cuerpo = 0

while sigue(cantidad_letras_adivinadas,cantidad_partes_cuerpo,pal): # Funcion agregada 
	letra = input('Ingresa una letra: ').lower()
	if letra in pal:	
		for pos in range(len (pal)):			
			if pal[pos] == letra:
				pal_separada[pos] = letra				
				cantidad_letras_adivinadas = cantidad_letras_adivinadas + 1		
		mostrar_letra(pal_separada)	# Funcion agregada	
	else:
		cantidad_partes_cuerpo=cantidad_partes_cuerpo + 1
		mostrar_ahorcado(cantidad_partes_cuerpo,ahorcado) # Funcion agregada			