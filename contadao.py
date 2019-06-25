from psycopg2 import connect
from conta import Conta
from cliente import Cliente
from clientedao import clienteDao

class contaDao:
    def __init__(self):
       self._dados_con = "dbname=contaBancaria host=localhost user=postgres password=postgres"
    
    def salvar(self,conta):
        contadao = contaDao()
        if(conta.codigo == None):
            contadao.inserir(conta)
        else:
            contadao.alterar(conta)
    
    def inserir(self,conta):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO conta ("numConta",agencia,saldo,tipo,"codigoCliente") VALUES (%s,%s,%s,%s,%s) RETURNING codigo',[conta.numero,conta.agencia,conta.saldo,conta.tipo,conta.cliente.codigo])
            linhacod = cur.fetchone()[0]
            conta.codigo = linhacod
            conn.commit()
            cur.close()

    def buscar(self,numero):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM conta WHERE codigo = %s',[numero])
            linha = cur.fetchall()
            conta = Conta(linha[0][1],linha[0][2],linha[0][3],linha[0][4])
            conta.codigo = linha[0][0]
            daocl = clienteDao()
            busc = daocl.buscar(int(linha[0][5]))
            conta.addCliente(busc)
            return conta
            conn.commit()
            cur.close()

    def deletar(self,cod):
        with connect (self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('DELETE FROM conta WHERE "codigo" = %s',[cod])
            conn.commit()
            cur.close()

    def alterar(self,conta):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('UPDATE conta SET agencia = %s, saldo = %s, nome = %s WHERE codigo = %s and "numConta" = %s',[conta.agencia,conta.saldo,conta.nome,conta.codigo,conta.numero])
            conn.commit()
            cur.close()

    def listar(self):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            lista_conta = []
            cur.execute('SELECT * FROM conta')
            for linha in cur.fetchall():
                conta = Conta(linha[1],linha[2],linha[3],linha[4])
                conta.codigo = linha[0]
                daocl = clienteDao()
                busc = daocl.buscar(int(linha[5]))
                conta.addCliente(busc)
                lista_conta.append(conta)
            return lista_conta
            conn.commit()
            cur.close()