import numpy as np

def nnFuncionCosto(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lambdaP):
	
	theta1 = np.reshape(nn_params[0:hidden_layer_size * (input_layer_size + 1)], (hidden_layer_size, (input_layer_size + 1)))
	theta2 = np.reshape(nn_params[((hidden_layer_size * (input_layer_size + 1))):], (num_labels, (hidden_layer_size + 1)));
	#print theta1
	#print nn_params[(1 + (hidden_layer_size * (input_layer_size + 1))):]

	#theta1 = np.reshape(nn_params[0:hidden_layer_size * (input_layer_size + 1)], hidden_layer_size, (input_layer_size + 1));
	#theta2 = np.reshape(nn_params[(1 + (hidden_layer_size * (input_layer_size + 1))):], num_labels, (hidden_layer_size + 1));

	#print theta1
	#print theta2

	m = len(X)

	J = 0
	Theta1_grad = np.zeros(X.shape)
	Theta2_grad = np.zeros(y.shape)

	unos = np.ones((m, 1))

	print unos.shape
	print X.shape

	#a1 = np.concatenate((unos, X))

	'''t
	#Se procede a realizar el feedforward
	a1 = np.concatenate(np.ones(shape=(m, 1)), X)
	z1 = a1*Theta1.transpose()
	a2 = np.concatenate(np.ones(size(z1, 1), 1), sigmoid(z1))
	z2 = a2*Theta2.transpose()
	a3 = sigmoid(z2)
	h = a3
	'''






