import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class SeleniumTeste(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/index")

    def test_title(self):
        driver = self.driver
        self.assertIn("Página Inicial - Exemplo guiado", driver.title)

    def test_listar(self):
        driver = self.driver
        #self.assertIn("Página Inicial - Exemplo guiado", driver.title)
        driver.find_element_by_link_text('Listar').click()
        self.assertIn('<h1>Listando</h1>', driver.page_source)

    def test_button_inserir_em_listar(self):
        driver = self.driver
        driver.find_element_by_link_text('Listar').click()
        self.assertTrue(driver.find_element_by_link_text("Inserir uma nova conta"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
