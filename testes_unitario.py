import unittest
from conta import Conta
from cliente import Cliente
class ContaTeste(unittest.TestCase):
    def setUp(self):
        self.Conta1 = Conta('5555555','0668',1000,'87436981072','Thamyris Cardoso')
        self.Conta2 = Conta('222','0698',2500,'87436999079','Helena Leivas')

    def test_equal(self):
        self.assertEqual(self.Conta1.nome,'Thamyris Cardoso')

    def test_saldo(self):
        self.assertGreaterEqual(self.Conta1.saldo,1000)

    def test_sacarTrue(self):
        self.assertTrue(self.Conta1.sacar(500))

    def test_depositarFalse(self):
        self.assertFalse(self.Conta1.depositar(1100))
    
    def test_transfere(self):
        self.assertTrue(self.Conta1.transferencia(self.Conta2,500))


if __name__=='__main__':
    unittest.main()
