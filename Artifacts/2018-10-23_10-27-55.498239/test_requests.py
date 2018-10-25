# coding=utf-8
import unittest
import re
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as econd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

import apiritif
from bzt.resources import selenium_taurus_extras

_vars = {}
_tpl = selenium_taurus_extras.Template(_vars)

class TestRequests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service_log_path='/Users/chefe02/Desktop/presales_cert/2018-10-23_10-27-55.498239/webdriver.log', chrome_options=options)
        self.driver.implicitly_wait(60.0)
        self.wnd_mng = selenium_taurus_extras.WindowManager(self.driver)
        self.frm_mng = selenium_taurus_extras.FrameManager(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_requests(self):
        self.driver.implicitly_wait(60.0)

        with apiritif.transaction_logged(u'go to home page'):
            self.driver.get(_tpl.apply(u'http://demo.bzm-presales.com/nopcommerce'))


        with apiritif.transaction_logged(u'search "apple"'):
            self.driver.find_element(By.ID, _tpl.apply(u'small-searchterms')).click()
            self.driver.find_element(By.ID, _tpl.apply('small-searchterms')).clear()
            self.driver.find_element(By.ID, _tpl.apply('small-searchterms')).send_keys(_tpl.apply('apple'))
            self.driver.find_element(By.ID, _tpl.apply(u'small-search-box-form')).submit()


        with apiritif.transaction_logged(u'click macbook'):
            self.driver.find_element(By.CSS_SELECTOR, _tpl.apply(u'div.picture > a[title="Show details for Apple MacBook Pro 13-inch"] > img[alt="Picture of Apple MacBook Pro 13-inch"]')).click()


        with apiritif.transaction_logged(u'add macbook to cart'):
            self.driver.find_element(By.ID, _tpl.apply(u'add-to-cart-button-4')).click()


        with apiritif.transaction_logged(u'click "books"'):
            self.driver.find_element(By.LINK_TEXT, _tpl.apply(u'Books')).click()


        with apiritif.transaction_logged(u'add fahrenheit 451 to cart'):
            self.driver.find_element(By.LINK_TEXT, _tpl.apply(u'Accessories')).click()


        with apiritif.transaction_logged(u'add sunglasses to cart'):
            self.driver.find_element(By.XPATH, _tpl.apply(u"(//input[@value='Add to cart'])[2]")).click()


        with apiritif.transaction_logged(u'checkout as guest'):
            self.driver.find_element(By.LINK_TEXT, _tpl.apply(u'shopping cart')).click()
            self.driver.find_element(By.ID, _tpl.apply(u'termsofservice')).click()
            self.driver.find_element(By.ID, _tpl.apply(u'checkout')).click()
            self.driver.find_element(By.CSS_SELECTOR, _tpl.apply(u'input.button-1.checkout-as-guest-button')).click()
            self.driver.find_element(By.ID, _tpl.apply(u'NewAddress_FirstName')).click()
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_FirstName')).clear()
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_FirstName')).send_keys(_tpl.apply('captain'))
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_LastName')).clear()
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_LastName')).send_keys(_tpl.apply('herp-a-derp'))
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_Email')).clear()
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_Email')).send_keys(_tpl.apply('felicia.chen@blazemeter.com'))
            Select(self.driver.find_element(By.ID, _tpl.apply('NewAddress_CountryId'))).select_by_visible_text(_tpl.apply(u'United States'))
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_City')).clear()
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_City')).send_keys(_tpl.apply('pirate cove'))
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_Address1')).clear()
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_Address1')).send_keys(_tpl.apply('123 tall ship st.'))
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_ZipPostalCode')).clear()
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_ZipPostalCode')).send_keys(_tpl.apply('95050'))
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_PhoneNumber')).clear()
            self.driver.find_element(By.ID, _tpl.apply('NewAddress_PhoneNumber')).send_keys(_tpl.apply('4081234567'))
            Select(self.driver.find_element(By.ID, _tpl.apply('NewAddress_StateProvinceId'))).select_by_visible_text(_tpl.apply(u'California'))
            self.driver.find_element(By.NAME, _tpl.apply(u'nextstep')).click()
            self.driver.find_element(By.NAME, _tpl.apply(u'nextstep')).click()
            self.driver.find_element(By.NAME, _tpl.apply(u'nextstep')).click()
            self.driver.find_element(By.NAME, _tpl.apply(u'nextstep')).click()
            self.driver.find_element(By.NAME, _tpl.apply(u'nextstep')).click()
            self.driver.find_element(By.CSS_SELECTOR, _tpl.apply(u'input.button-1.order-completed-continue-button')).click()


