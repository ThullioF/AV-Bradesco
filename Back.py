import sqlite3 as sql

class TransactionObject():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        self.conn = sql.connect(self.database)
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        if self.connected:
            self.conn.close()
            self.connected = False

    def execute(self, sql_query, params=None):
        if self.connected:
            if params is None:
                self.cur.execute(sql_query)
            else:
                self.cur.execute(sql_query, params)
                return True
        else:
            return False

    def fetchall(self):
        return self.cur.fetchall()

    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False

    def initDB(self):
        self.connect()
        self.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        self.persist()
        self.disconnect()

def insert(nome, sobrenome, email, cpf):
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf))
    transaction.persist()
    transaction.disconnect()

def view():
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("SELECT * FROM clientes")
    rows = transaction.fetchall()
    transaction.disconnect()
    return rows

def search(nome="", sobrenome="", email="", cpf=""):
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email, cpf))
    rows = transaction.fetchall()
    transaction.disconnect()
    return rows

def delete(id):
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("DELETE FROM clientes WHERE id = ?", (id,))
    transaction.persist()
    transaction.disconnect()

def update(id, nome, sobrenome, email, cpf):
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, cpf = ? WHERE id = ?", (nome, sobrenome, email, cpf, id))
    transaction.persist()
    transaction.disconnect()
