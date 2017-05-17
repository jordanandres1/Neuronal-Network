import numpy as np
from scipy.special import expit # funcion sigmoide ej: expit(9)
from scipy.stats import logistic # funcion sigmoide gradiente ej: logistic.pdf(np.array([[2, 4, 6], [7, 8, 9]]))

def nnFuncionCosto(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lambdaP):
	
	theta1 = np.reshape(nn_params[0:hidden_layer_size * (input_layer_size + 1)], (hidden_layer_size, (input_layer_size + 1))) # 25 x 785
	theta2 = np.reshape(nn_params[((hidden_layer_size * (input_layer_size + 1))):], (num_labels, (hidden_layer_size + 1))) # 10 x 26

	m = len(X)

	J = 0
	theta1_grad = np.zeros(X.shape) # 60000 x 784
	theta2_grad = np.zeros(y.shape) # 60000 x 1

	unos = np.ones((m, 1)) # 60000 x 1
	a1 = np.concatenate((unos, X), axis=1) # 60000 x 785
	z1 = np.dot(a1, theta1.transpose()) # 60000 x 25
	a2 = np.concatenate((np.ones((len(z1), 1)), expit(z1)), axis=1) # 60000 x 26
	z2 = np.dot(a2, theta2.transpose()) # 60000 x 10
	a3 = expit(z2) # 60000 x 10
	h = a3 # 60000 x 10

	Y = np.zeros((num_labels, m)) # 10 x 60000
	for i in range(num_labels):
		Y[i,] = (y == i)
	Y = Y.transpose() # 60000 x 10

	parte1 = (1.0 / m)
	parte2 = -Y * np.log(h) - (1.0 - Y) * np.log(1.0 - h) # 60000 x 10
	parte3 = parte2.sum(axis=0) # 10 x 1
	parte4 = parte3.sum(axis=0)
	J = parte1 * parte4

	theta1Reg = theta1[:,1:] # 25 x 784
	theta2Reg = theta2[:,1:] # 10 x 25
	theta1Reg = theta1Reg ** 2.0 # 25 x 784
	theta2Reg = theta2Reg ** 2.0 # 10 x 25
	sumTheta1 = theta1Reg.sum(axis=0).sum(axis=0)
	sumTheta2 = theta2Reg.sum(axis=0).sum(axis=0)

	reg = (lambdaP / (2.0 * m)) * (sumTheta1 + sumTheta2)
	J = J + reg

	# Se realiza el backpropagation
	d2 = h - Y # 60000 x 10
	temp0 = np.ones((len(z1), 1)) # 60000 x 1
	temp1 = np.concatenate((temp0, z1), axis=1) # 60000 x 26

	d1 = np.dot(d2, theta2) * logistic.pdf(temp1) # 60000 x 26
	d1 = d1[:, 1:] # 60000 x 25

	#% Se calculan los Delta dividiendo los errores entre m
	delta_1 = np.dot(d1.transpose(), a1) / m # 25 x 785
	delta_2 = np.dot(d2.transpose(), a2) / m # 10 x 26

	# Se obtiene la regularizacion para las gradientes de los 2 Theta
	temp2 = np.zeros((len(theta1), 1)) # 25 x 1
	temp3 = np.zeros((len(theta2), 1)) # 10 x 1
	temp4 = theta1[:, 1:] # 25 x 784
	temp5 = theta2[:, 1:] # 10 x 25
	regGrad1 = np.dot((lambdaP / m), np.concatenate((temp2, temp4), axis=1)) # 25 x 785
	regGrad2 = np.dot((lambdaP / m), np.concatenate((temp3, temp5), axis=1)) # 10 x 26

	theta1_grad = delta_1 + regGrad1 # 25 x 785
	theta2_grad = delta_2 + regGrad2 # 10 x 26

	grad = np.concatenate((theta1_grad.flatten(1), theta2_grad.flatten(1)), axis=0) # 19885 x 1

	return (J, grad)


