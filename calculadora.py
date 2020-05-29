def suma(val1, val2):
	return val1 + val2


def resta(val1, val2):
	return val1 - val2

def multiplicacion(val1, val2):
	return val1 * val2

def division(val1, val2):
	return val1 / val2

def raizcuadrada(val1):
	# Calculamos el cuadrado perfecto más cercano al valor
	j = 0
	i = 1
	while i < val1:
		n = i*i
		if (val1 < n):
			n = i-1
			break
		i += 1
	# Aplicamos la fórmula de Bakhshali para calcular la raiz cuadrada
	raizcuadrada = (((n*n*n*n)+(6*(n*n)*val1)+(val1*val1))/(4*(n*n*n)+(4*n*val1)))
	return raizcuadrada
  