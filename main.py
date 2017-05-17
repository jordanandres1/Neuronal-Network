import sys
import numpy as np
import idx2numpy
from nnFuncionCosto import nnFuncionCosto
from randInitializeWeights import randInitializeWeights
from predecir import predecir
import warnings
from Tkinter import *

# Este metodo carga las 60000 imagenes
def leerTrainingSet():
	x_training = idx2numpy.convert_from_file('datos/train-images-idx3-ubyte') # Las imagenes son 60000 cada una de 28x28
	y_training = idx2numpy.convert_from_file('datos/train-labels-idx1-ubyte')
	x_training = np.reshape(x_training, (60000, 784))
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

def solicitarNeuronas():
	top = Toplevel(root)
	Label(top, text="Neuronas por capa", font="Helvetica 14 bold").grid(row=0, column=0)

	for i in range(int(capas.get())):
		Label(top, text="Capa " + str(i+1)).grid(row=(i+1), column=0)
		c = Entry(top)
		c.grid(row=(i+1), column=1)
		listaCapas.append(c)

	Button(top, text="Listo", command=imprimir).grid(column=1, sticky=E, pady=4)

def imprimir():
	global listaCapas

	for c in listaCapas:
		print c.get()

	listaCapas = []

if __name__ == '__main__':

	'''
	root = Tk()
	root.title("Red neuronal")

	listaCapas = []

	Label(root, text="Proporciones", font="Helvetica 14 bold").grid(row=0, column=0)
	Label(root, text="Validation").grid(row=1, column=0)
	Label(root, text="Test").grid(row=2, column=0)

	validation = Entry(root)
	test = Entry(root)
	validation.grid(row=1, column=1)
	test.grid(row=2, column=1)

	Label(root, text="Arquitectura", font="Helvetica 14 bold").grid(row=3, column=0)
	Label(root, text="Capas ocultas").grid(row=4, column=0)

	capas = Entry(root)
	capas.grid(row=4, column=1)

	Button(root, text="Listo", command=solicitarNeuronas).grid(row=5, column=1, sticky=E, pady=4)
	
	mainloop()
	'''
	
	input_layer_size  = 784
	hidden_layer_size = 25
	num_labels = 10
	lambdaP = 1

	warnings.filterwarnings("ignore")
	print 'Cargando y visualizando datos...\n'

	(x_training, y_training) = leerTrainingSet()

	print '\nFeedforward usando Redes Neuronales...'
	theta1 = randInitializeWeights(hidden_layer_size, input_layer_size) # 25 x 785
	theta2 = randInitializeWeights(num_labels, hidden_layer_size) # 10 x 26

	#theta1 = np.random.uniform(-1, 1, (hidden_layer_size, input_layer_size + 1))	
	#theta2 = np.random.uniform(-1, 1, (num_labels, hidden_layer_size + 1))

	vectorTheta1 = theta1.flatten(1) # 19625 x 1
	vectorTheta2 = theta2.flatten(1) # 260 x 1

	nn_params = np.concatenate((vectorTheta1, vectorTheta2), axis=0) # 19885 x 1

	(J, grad) = nnFuncionCosto(nn_params, input_layer_size, hidden_layer_size, num_labels, x_training, y_training, lambdaP)
	print 'El valor de costo inicial regularizado es: ' + str(J)

	#res1 = optimize.fmin_cg(nnFuncionCosto, )

	print '\nEntrenando la Red Neuronal...'
	pred = predecir(theta1, theta2, x_training) # 60000 x 1
	
	
