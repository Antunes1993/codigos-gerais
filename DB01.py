import MySQLdb 

db = MySQLdb.connect(user = "root", passwd = "Fumacento#30135609", db = "db_biblioteca", port = 3306)
print ("conexão realizada")

cursor = db.cursor()
cursor.execute("SELECT (NOME_LIVRO) FROM tb_livro")
print (cursor.fetchall())
print(cursor.fetchmany(1))
print(cursor.fetchone())
