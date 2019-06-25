from psycopg2 import connect
from cliente import Cliente

class clienteDao:
    def __init__(self):
       self._dados_con = "dbname=contaBancaria host=localhost user=postgres password=postgres"
    
    def buscar(self,codigo):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM cliente WHERE codigo = %s',[codigo])
            linha = cur.fetchall()
            cliente = Cliente(linha[0][1],linha[0][2],linha[0][3])
            cliente.codigo = linha[0][0]
            return cliente
            conn.commit()
            cur.close()

    def listar(self):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            lista_cliente = []
            cur.execute('SELECT * FROM cliente')
            for linha in cur.fetchall():
                cliente = Cliente(linha[1],linha[2],linha[3])
                cliente.codigo = linha[0]
                lista_cliente.append(cliente)
            return lista_cliente
            conn.commit()
            cur.close()