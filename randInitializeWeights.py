import numpy as np

def randInitializeWeights(param1, param2):
	pesos = np.zeros((param1, 1 + param2))

	epsilon_inicial = 0.12
	factor1 = 2 * epsilon_inicial
	factor2 = np.dot(np.random.rand(param1, 1 + param2), factor1)
	pesos = factor2 - epsilon_inicial

	return pesos
