import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url="https://www.nike.com"

@pytest.mark.parametrize("item",
                         [
                             "hats",
                             "pants"
                         ])

@pytest.mark.adidas
def test_nike_search(browser, item):
    browser.get(base_url)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".btn-md.btn-primary-dark.css-60b779.dialog-actions-accept-btn.ex41m6f0.nds-btn").click()
    #Cookie
    browser.find_element(By.ID, "VisualSearchInput").send_keys(item + Keys.ENTER)
    # SEARCH_FIELD
    browser.find_element(By.CLASS_NAME, "dropdown__btn-text-wrapper").click()
    #PRICE
    browser.find_element(By.CSS_SELECTOR, "div#sort-options > button:nth-of-type(4)").click()
    #LOW-HIGH
    browser.find_element(By.CLASS_NAME, "trigger-content__label").click()
    #SEX
    browser.find_element(By.CSS_SELECTOR, ".css-gr3fpq > div:nth-of-type(1) [aria-checked='false']:nth-of-type(1) div").click()
    #SEX
    time.sleep(5)


