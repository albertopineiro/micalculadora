from calculadora import suma

def test_suma():
	# arrange
	valor1 = 5
	valor2 = 7
	resultadoEsperado = 14
	# act
	r = suma(valor1, valor2)
	# assert
	if r == resultadoEsperado:
		print("SUMA CORRECTA")
	else:
		print("SUMA INCORRECTA------------------")


def test_resta():
	# arrange
	valor1 = 9
	valor2 = 4
	resultadoEsperado = 5
	# act
	r = resta(valor1, valor2)
	# assert
	if r == resultadoEsperado:
		print("RESTA CORRECTA")
	else:
		print("RESTA INCORRECTA------------------")



def test_multiplicacion():
	# arrange
	valor1 = 6
	valor2 = 3
	resultadoEsperado = 18
	# act
	r = multiplicacion(valor1, valor2)
	# assert
	if r == resultadoEsperado:
		print("MULTIPLICACION CORRECTA")
	else:
		print("MULTIPLICACION INCORRECTA------------------")


def test_division():
	# arrange
	valor1 = 27
	valor2 = 3
	resultadoEsperado = 9
	# act
	r = division(valor1, valor2)
	# assert
	if r == resultadoEsperado:
		print("MULTIPLICACION CORRECTA")
	else:
		print("MULTIPLICACION INCORRECTA------------------")




if __name__ == "__main__":
	test_suma()
	test_resta()
	test_multiplicacion()
	test_division()
