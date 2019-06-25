from flask import Flask, render_template, request, redirect, session
import hashlib
from clientedao import clienteDao
from cliente import Cliente
from contadao import contaDao
from conta import Conta
import psycopg2

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/conta/salvar')
def formsConta():
    dao = clienteDao()
    lista_clientes = dao.listar()
    return render_template('salvar.html',clientes = lista_clientes)

@app.route('/conta/listar')
def listaConta():
    dao = contaDao()
    lista_contas = dao.listar()
    return render_template('listar.html', contas = lista_contas)

@app.route('/conta/excluir', methods = ['GET'])
def excluirConta():
    cod_conta = int(request.values["cod"])
    dao = contaDao()
    dao.deletar(cod_conta)
    return redirect ('/conta/listar')

@app.route('/conta/alterar')
def alterarConta():
    cod_alterar = int(request.values["cod"])
    dao = contaDao()
    conta = dao.buscar(cod_alterar)
    daocliente = clienteDao()
    lista_clientes = daocliente.listar()
    return render_template('salvar.html', conta = conta, clientes = lista_clientes)

@app.route('/conta/buscar')
def buscarConta():
    cod = int(request.values["codigo"])
    dao = contaDao()
    conta = dao.buscar(cod)
    return render_template('buscar.html', buscando = conta)

@app.route('/conta/salvar', methods = ['POST', 'GET'])
def salvarConta():
    numero = request.form["numero"]
    agencia = request.form["agencia"]
    saldo = request.form["saldo"]
    tipo = request.form["tipo"]
    cliente = request.form["cliente"]
    daocliente = clienteDao()
    c = daocliente.buscar(int(cliente))
    conta = Conta(numero,agencia,saldo,tipo)
    conta.addCliente(c)
    daoconta = contaDao()
    if(request.values.has_key("codigo") == True):
        cod = request.form["codigo"]
        conta.codigo = int(cod)
    daoconta.salvar(conta)
    return redirect('/conta/listar')



def main():
    app.secret_key = 'string'
    app.env = 'development'
    app.run(debug = True, port = 5000)

if __name__ == '__main__': 
    main()
