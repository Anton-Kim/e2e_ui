from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


base_url = 'https://www.saucedemo.com'


def get_browser():
    brwsr = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    brwsr.implicitly_wait(5)
    yield brwsr
    brwsr.quit()


browser = next(get_browser())
browser.get(base_url)


def authorization():
    browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()
    if browser.find_element(By.CLASS_NAME, 'title').text == 'Products':
        print('OK. Авторизация на сайте прошла успешно.')
    else:
        print('ERROR. Ошибка авторизации на сайте.')


def add_to_cart():
    browser.find_element(By.CSS_SELECTOR, '.inventory_item:nth-child(5) button').click()
    if browser.find_element(By.CSS_SELECTOR, '.inventory_item:nth-child(5) button').text == 'Remove':
        print('OK. Товар успешно добавлен в корзину.')
    else:
        print('ERROR. Ошибка при добавлении товара в корзину.')


def make_order():
    browser.get(f'{base_url}/cart.html')
    cart_list = browser.find_elements(By.CLASS_NAME, 'cart_item')
    if cart_list and browser.find_element(By.CLASS_NAME, 'inventory_item_name').text == 'Sauce Labs Onesie':
        browser.find_element(By.ID, 'checkout').click()
        browser.find_element(By.ID, 'first-name').send_keys('Harry')
        browser.find_element(By.ID, 'last-name').send_keys('Potter')
        browser.find_element(By.ID, 'postal-code').send_keys('-0001')
        browser.find_element(By.ID, 'continue').click()
        browser.find_element(By.ID, 'finish').click()
        print('OK. Оформление покупки осуществлено успешно.')
    else:
        print('ERROR. В корзине отсутствует добавленный товар.')


def order_completed():
    if browser.find_element(By.CLASS_NAME, 'complete-header').text == 'Thank you for your order!':
        print('OK. Покупка завершена успешно.')
    else:
        print('ERROR. Ошибка при завершении покупки.')


def tests():
    authorization()
    add_to_cart()
    make_order()
    order_completed()


if __name__ == '__main__':
    tests()
