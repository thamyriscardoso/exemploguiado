class Cliente:
    def __init__(self,cpf,nome,email):
        self._codigo = None
        self._cpf = cpf
        self._nome = nome
        self._email = email

    def _get_codigo(self):
        return self._codigo
    
    def _set_codigo(self,codigo):
        self._codigo = codigo

    def _get_cpf(self):
        return self._cpf

    def _set_cpf(self,cpf):
        self._cpf = cpf

    def _get_nome(self):
        return self._nome

    def _set_nome(self,nome):
        self._nome = nome

    def _get_email(self):
        return self._email

    def _set_email(self,email):
        self._email = email
    
    email = property(_get_email, _set_email)
    cpf = property(_get_cpf,_set_cpf)
    nome = property(_get_nome,_set_nome)
    codigo = property(_get_codigo,_set_codigo)
