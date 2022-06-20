import time

from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import conftest

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert button == browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button"), "OK"
