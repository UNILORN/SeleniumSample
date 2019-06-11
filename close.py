from selenium import webdriver
import os
from os.path import abspath,dirname
from random import randrange
from time import sleep

sleep(randrange(300))
if os.name == 'posix':
    path = abspath(dirname(__file__)+'./mac/chromedriver')
else:
    path = abspath(dirname(__file__)+'\win\chromedriver.exe')
browser = webdriver.Chrome(executable_path=path)
browser.get('https://www1.shalom-house.jp/komon/')
browser.implicitly_wait(3)
el = browser.find_element_by_id('txtID')
el.send_keys('B0597859')
el = browser.find_element_by_id('txtPsw')
el.send_keys('86f21d')
el = browser.find_element_by_id('btnLogin')
el.click()
el = browser.find_element_by_id('ctl00_ContentPlaceHolder1_imgBtnSyuugyou')
el.click()
el = browser.find_element_by_id('ctl00_ContentPlaceHolder1_ibtnOut4')
el.click()
browser.close()