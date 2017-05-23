import sys
import scipy.io
import scipy.optimize as optimize
import numpy as np
import idx2numpy
from nnFuncionCosto import nnFuncionCosto, minimizarCosto
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

def leerTestSet():
	x = idx2numpy.convert_from_file('datos/t10k-images-idx3-ubyte') # Las imagenes son 60000 cada una de 28x28
	y = idx2numpy.convert_from_file('datos/t10k-labels-idx1-ubyte')
	x = np.reshape(x, (10000, 784))
	x_cv = x[0:5000]
	x_test = x[5000:]
	y_cv = y[0:5000]
	y_test = y[5000:]
	return (x_cv, y_cv, x_test, y_test)

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

	warnings.filterwarnings("ignore")


	print 'Cargando y visualizando datos...\n'
	input_layer_size = 784
	#input_layer_size = 400
	hidden_layer_size = 25
	num_labels = 10
	lambdaP = 0
	#training = scipy.io.loadmat('data1.mat')
	#x_training = training['X']
	#y_training = training['y']
	#y_training = np.squeeze(np.asarray(y_training))
	(x_training, y_training) = leerTrainingSet()
	(x_cv, y_cv, x_test, y_test) = leerTestSet()


	print '\nFeedforward usando Redes Neuronales...'
	theta1 = randInitializeWeights(hidden_layer_size, input_layer_size) # 25 x 785
	theta2 = randInitializeWeights(num_labels, hidden_layer_size) # 10 x 26

	'''
	thetas = scipy.io.loadmat('pesos.mat')
	theta1 = thetas['Theta1']
	theta2 = thetas['Theta2']
	theta1 = np.array(theta1)
	theta2 = np.array(theta2)
	'''

	vectorTheta1 = theta1.flatten(1) # 19625 x 1
	vectorTheta2 = theta2.flatten(1) # 260 x 1
	nn_params = np.concatenate((vectorTheta1, vectorTheta2), axis=0) # 19885 x 1

	(J, grad) = nnFuncionCosto(nn_params, input_layer_size, hidden_layer_size, num_labels, x_training, y_training, lambdaP)
	print 'El valor de costo inicial sin regularizar es: ' + str(J)

	lambdaP = 1
	(J, grad) = nnFuncionCosto(nn_params, input_layer_size, hidden_layer_size, num_labels, x_training, y_training, lambdaP)
	print 'El valor de costo inicial regularizado es: ' + str(J)

	print '\nEntrenando la Red Neuronal...'
	extra = (input_layer_size, hidden_layer_size, num_labels, x_training, y_training, lambdaP)
	res = optimize.minimize(minimizarCosto, nn_params, extra, method='L-BFGS-B', jac=True, options={'maxiter': 25, 'disp': True})
	res = res.x

	theta1 = np.reshape(res[:hidden_layer_size * (input_layer_size + 1)], (hidden_layer_size, (input_layer_size + 1)), order='F')  # 25 x 785
	theta2 = np.reshape(res[((hidden_layer_size * (input_layer_size + 1))):], (num_labels, (hidden_layer_size + 1)), order='F')

	pred = predecir(theta1,theta2, x_training)
	print 'Precision de la Red Neuronal sobre el training set: ' +  str(np.mean(pred == y_training) * 100)

	print '\nRealizando Test...'






