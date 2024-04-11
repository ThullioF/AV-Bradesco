import sqlite3

con = sqlite3.connect("nome_do_banco.bd")

cur = con.cursor()

#cur.execute("CREATE TABLE contato(nome text, endereco text, telefone text)")

cur.execute("INSERT INTO contato2 VALUES ('Fulan','Rua Brasi', '12345678')")

con.commit()

#cur.execute("SELECT * FROM contato")
#print(cur.fetchall())
