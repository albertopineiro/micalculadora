import unittest
from calculadora import suma, resta, multiplicacion, division, raizcuadrada

class TestCalculadora(unittest.TestCase):		

	def test_suma(self):
		# arrange
		valor1 = 5
		valor2 = 7
		resultadoEsperado = 12
		# act
		resultado = suma(valor1, valor2)
		# assert
		self.assertEqual(resultado, resultadoEsperado)


	def test_resta(self):
		# arrange
		valor1 = 9
		valor2 = 4
		resultadoEsperado = 5
		# act
		resultado = resta(valor1, valor2)
		# assert
		self.assertEqual(resultado, resultadoEsperado)


	def test_multiplicacion(self):
		# arrange
		valor1 = 6
		valor2 = 3
		resultadoEsperado = 18
		# act
		resultado = multiplicacion(valor1, valor2)
		# assert
		self.assertEqual(resultado, resultadoEsperado)

	def test_division(self):
		# arrange
		valor1 = 27
		valor2 = 3
		resultadoEsperado = 9
		# act
		resultado = division(valor1, valor2)
		# assert
		self.assertEqual(resultado, resultadoEsperado)


	def test_raiz(self):
		# arrange
		valor1 = 50
		resultadoEsperado = 7.071067811865475
		# act
		resultado=raizcuadrada(valor1)
		# assert
		self.assertLess(abs(resultado-resultadoEsperado), 0.00000001)

if __name__ == "__main__":
	unittest.main()