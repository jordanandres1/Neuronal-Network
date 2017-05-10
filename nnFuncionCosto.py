import numpy as np

def nnFuncionCosto(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lambdaP):
	Theta1 = np.reshape(nn_params[0:hidden_layer_size * (input_layer_size + 1)], hidden_layer_size, (input_layer_size + 1));
	Theta2 = np.reshape(nn_params[(1 + (hidden_layer_size * (input_layer_size + 1))):], num_labels, (hidden_layer_size + 1)); 

	m = len(X)

	J = 0
	Theta1_grad = np.zeros(len(Theta1))
	Theta2_grad = np.zeros(len(Theta2))

	#Se procede a realizar el feedforward
	a1 = concatenate(np.ones(shape=(m, 1)), X)
	z1 = a1*Theta1.transpose()
	a2 = concatenate(np.ones(size(z1, 1), 1), sigmoid(z1))
	z2 = a2*Theta2.transpose()
	a3 = sigmoid(z2)
	h = a3






