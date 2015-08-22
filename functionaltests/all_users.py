# -*- coding: utf-8 -*-
from selenium import webdriver      # import webdriver from selenium
import unittest                     # import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        '''Инициализация теста. Открывает браузер и ждет три секунды загрузки страницы'''                           
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        '''Метод запускается после каждого теста и закрывает браузер '''
        self.browser.quit()
    def test_it_worked(self):
        '''Метод запускает тест и проверяет равен ли title вебстраницы Welcome to Django'''
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)
if __name__ == '__main__':
    unittest.main(warnings='ignore')