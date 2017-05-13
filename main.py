import sys
import numpy as np
import idx2numpy
from scipy.optimize import fmin # funcion de optimizacion
from nnFuncionCosto import nnFuncionCosto
from scipy.special import expit # funcion sigmoide ej: expit(9)
from scipy.stats import logistic # funcion sigmoide gradiente ej: logistic.pdf(np.array([[2, 4, 6], [7, 8, 9]]))
import random
# from mnist import MNIST

# Este metodo carga las 60000 imagenes
def leerTrainingSet():
	x_training = idx2numpy.convert_from_file('datos/train-images-idx3-ubyte') # Las imagenes son 60000 cada una de 28x28
	y_training = idx2numpy.convert_from_file('datos/train-labels-idx1-ubyte')
	return (x_training, y_training)

def printMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				sys.stdout.write('.')
			else:
				sys.stdout.write('#')
		print
	print

def main():
	input_layer_size  = 784
	hidden_layer_size = 25
	num_labels = 10

	print 'Cargando y visualizando datos\n'

	(x_training, y_training) = leerTrainingSet()

	print '\nFeedforward usando Redes Neuronales...\n'
	lambdaP = 0
	theta1 = np.random.random((hidden_layer_size, input_layer_size + 1))	
	theta2 = np.random.random((num_labels, hidden_layer_size + 1))

	#print theta1
	#print theta2

	vectorTheta1 = theta1.flatten(1)
	vectorTheta2 = theta2.flatten(1)

	#print vectorTheta1.shape
	#print vectorTheta2.shape


	nn_params = np.concatenate((vectorTheta1, vectorTheta2), axis=0)
	#print nn_params.shape


	J = nnFuncionCosto(nn_params, input_layer_size, hidden_layer_size, num_labels, x_training, y_training, lambdaP);

main()


