import MySQLdb as mdb

def insertarDatosBD(capas, neuronas, lambdaP, costo_inicial, precision_training, precision_test, error_training, error_test):
	db = mdb.connect("localhost", "user", "user1234", "Neural_Network")

	cursor = db.cursor()

	cursor.execute("INSERT INTO ejecucion (capas, neuronas, lambda, costo_inicial, precision_training, precision_test, error_training, error_test) VALUES (%d,%d,%f,%f,%f,%f,%f,%f)" % (capas, neuronas, lambdaP, costo_inicial, precision_training, precision_test, error_training, error_test))

	db.commit()

	db.close()
