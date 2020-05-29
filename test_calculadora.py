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


if __name__ == "__main__":
	test_suma()