import numpy as np
from scipy.special import expit

def predecir(theta1, theta2, X):

	m = len(X)
	num_labels = len(theta2)

	p = np.zeros((len(X), 1))

	unos = np.ones((m, 1))

	temp1 = np.concatenate((unos, X), axis=1)
	h1 = expit(np.dot(temp1, theta1.transpose()))
	temp2 = np.concatenate((unos, h1), axis=1)
	h2 = expit(np.dot(temp2, theta2.transpose()))

	p = np.argmax(h2, axis=1)
	return p