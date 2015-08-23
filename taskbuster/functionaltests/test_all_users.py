# -*- coding: utf-8 -*-
from selenium import webdriver      # import webdriver from selenium
from django.core.urlresolvers import reverse              
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        '''Инициализация теста. Открывает браузер и ждет три секунды загрузки страницы'''                           
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        '''Метод запускается после каждого теста и закрывает браузер '''
        self.browser.quit()
    def get_full_url(self, namespace):        
        '''Метод возвращает url local hosta + относительный url заданного namespace '''
        return self.live_server_url + reverse(namespace)
    def test_home_title(self):
        ''' Метод проверяет что заголовок домашней страницы содержит слово TaskBuster'''
        self.browser.get(self.get_full_url("home"))
        self.assertIn('TaskBuster', self.browser.title)
    def test_h1_css(self):
        ''' Метод проверяет имеет ли требуемый цвет заголовок h1 '''
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), "rgba(200, 50, 255, 1)")


