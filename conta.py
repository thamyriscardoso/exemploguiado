class Conta:
    def __init__(self,numero,agencia,saldo,tipo):
        self._codigo = None
        self._numero = numero
        self._agencia = agencia
        self._saldo = saldo
        self._cliente = None
        self._tipo = tipo

    def _get_tipo(self):
        return self._tipo

    def _set_tipo(self,tipo):
        self._tipo = tipo

    def _get_cliente(self):
        return self._cliente
    
    def _set_cliente(self,cliente):
        self._cliente = cliente

    def _get_codigo(self):
        return self._codigo
    
    def _set_codigo(self,codigo):
        self._codigo = codigo

    def _get_numero(self):
        return self._numero

    def _set_numero(self,numero):
        self._numero = numero

    def _get_agencia(self):
        return self._agencia

    def _set_agencia(self,agencia):
        self._agencia = agencia
    
    def _get_saldo(self):
        return self._saldo

    def _set_saldo(self,saldo):
        self._saldo = saldo

    def addCliente(self,cliente):
        self._cliente = cliente

    def sacar(self, valor):
        if(valor <= self.saldo):
            self._saldo -= valor
            return True
        else:
            return False

    def depositar(self,valor):
        if (valor <= 1000):
            self._saldo += valor
            return True
        else:
            return False

    def transferencia(self,conta,valor):
        if(valor<= self.saldo):
            conta.saldo +=valor
            self.saldo -=valor
            return True
        else:
            return False
        
    
    numero = property(_get_numero,_set_numero)
    agencia = property(_get_agencia, _set_agencia)
    saldo = property(_get_saldo, _set_saldo)
    codigo = property(_get_codigo,_set_codigo)
    cliente = property(_get_cliente,_set_cliente)
    tipo = property(_get_tipo,_set_tipo)
