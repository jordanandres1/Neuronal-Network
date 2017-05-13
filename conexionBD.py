import MySQLdb as mdb

def pruebaBD():
	db = mdb.connect("localhost","root","ruben13","Proyecto1")

	cursor = db.cursor()
	cursor.execute("SHOW TABLES;")

	data = cursor.fetchone()
	return data

def main():
	print pruebaBD()

main()