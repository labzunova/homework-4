from tests.pages.base import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from components.navbar import NavbarComponent
from selenium.common.exceptions import NoSuchElementException


class CustomerAuthPage(Page):
    PATH = '/signin'
    ADDRESS_INPUT = '//input[@id="js__map-add-address"]'
    ADDRESS_SUBMIT_BUTTON = '//button[@id="js__add-new-address__btn"]'
    LOGIN_INPUT = '//input[@name="login"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    SUBMIT_BUTTON = '//input[@value="Войти"]'
    REGISTRATION_BUTTON = '//a[text()="Я тут впервые"]'
    RESTAURANT_AUTH_BUTTON = '//a[text()="Войти как владелец ресторана"]'

    @property
    def navbar(self):
        return NavbarComponent(self.driver)

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN_INPUT).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def wait_until_login(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, self.navbar.USERNAME)))

    def go_to_registration(self):
        self.driver.find_element_by_xpath(self.REGISTRATION_BUTTON).click()

    def go_to_restaurant_auth(self):
        self.driver.find_element_by_xpath(self.RESTAURANT_AUTH_BUTTON).click()

    def set_address(self, address):
        try:
            elem = self.driver.find_element_by_xpath(self.ADDRESS_INPUT)
            elem.clear()
            elem.send_keys(address)
        except NoSuchElementException:
            return

    def submit_address(self):
        try:
            self.driver.find_element_by_xpath(self.ADDRESS_SUBMIT_BUTTON).click()
        except NoSuchElementException:
            return
