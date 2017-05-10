import idx2numpy
import numpy as np
from scipy.optimize import fmin # funcion de optimizacion
from nnFuncionCosto import nnFuncionCosto
from scipy.special import expit # funcion sigmoide ej: expit(9)
from scipy.stats import logistic # funcion sigmoide gradiente ej: logistic.pdf(np.array([[2, 4, 6], [7, 8, 9]]))

# Este metodo carga las 10000 imagenes
def leerArchivo():
	matrices = idx2numpy.convert_from_file('t10k-images.idx3-ubyte') # Las imagenes son 10000 cada una de 28x28
	return matrices

def main():
	input_layer_size  = 784
	hidden_layer_size = 25
	num_labels = 10

	print 'Cargando y visualizando datos\n'
	training_set = leerArchivo()
	m = len(training_set)
	print m

	print '\nFeedforward usando Redes Neuronales...\n'
	lambdaP = 0
	nn_params = np.array([[0], [0]])
	X  = training_set
	#J = nnFuncionCosto(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lambdaP);

main()


