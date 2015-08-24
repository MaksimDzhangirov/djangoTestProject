# -*- coding: utf-8 -*-
from selenium import webdriver      # import webdriver from selenium
from datetime import date
from django.utils import formats
from django.core.urlresolvers import reverse              
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        '''Инициализация теста. Открывает браузер и ждет три секунды загрузки страницы'''                           
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        activate('ru')
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
    def test_home_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)
    def test_internationalization(self):
        for lang,h1_text in [('en', 'Hello, world!'), ('ru', 'Привет, мир!')]:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            h1 = self.browser.find_element_by_tag_name("h1")
            self.assertEqual(h1.text, h1_text)
    def test_localization(self):
        today = date.today()
        for lang in ['en', 'ru']:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            local_date = self.browser.find_element_by_id("local-date")
            non_local_date = self.browser.find_element_by_id("non-local-date")
            self.assertEqual(formats.date_format(today, use_l10n = True), local_date.text)
            self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)
    def test_time_zone(self):
        self.browser.get(self.get_full_url("home"))
        tz = self.browser.find_element_by_id("time-tz").text
        utc = self.browser.find_element_by_id("time-utc").text
        ny = self.browser.find_element_by_id("time-ny").text
        self.assertNotEqual(tz, utc)
        self.assertNotIn(ny, [tz, utc])



