import numpy as np
from scipy.optimize import fmin # funcion de optimizacion
from nnFuncionCosto import nnFuncionCosto
from scipy.special import expit # funcion sigmoide ej: expit(9)
from scipy.stats import logistic # funcion sigmoide gradiente ej: logistic.pdf(np.array([[2, 4, 6], [7, 8, 9]]))
from mnist import MNIST
import random


def leerTrainingSet(mndata):
	images, labels = mndata.load_training()
	x_training = np.array(images)
	y_training = np.array(labels)
	return (x_training, y_training)


def main():
	input_layer_size  = 784
	hidden_layer_size = 25
	num_labels = 10

	print 'Cargando y visualizando datos\n'
	mndata = MNIST('datos')
	(x_training, y_training) = leerTrainingSet(mndata)

	print mndata.display(x_training[0])
	print
	print mndata.display(x_training[1])
	print
	print mndata.display(x_training[2])
	print
	print mndata.display(x_training[3])
	print
	print mndata.display(x_training[4])

	print '\nFeedforward usando Redes Neuronales...\n'
	lambdaP = 0
	nn_params = np.array([[0], [0]])
	J = nnFuncionCosto(nn_params, input_layer_size, hidden_layer_size, num_labels, x_training, y_training, lambdaP);

main()


