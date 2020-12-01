from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import pyautogui
from PIL import Image

random.seed()


class BuyingAPlaystation():
    
    def __init__(self):
        self.username = 'clintonruairi@gmail.com'
        self.password = 'hopefullythisworks1'
        self.security_code = '833'

    def avoid_detection(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--disable-blink-features=AutomationControlled')
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])

    def startup_and_go_to_walmart(self):
        self.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=self.option)
        self.browser.get('https://www.walmart.ca/en')
        print('Loaded Walmart Page')

    def get_login_element(self):
        time.sleep(random.randint(2, 5))
        try:
            self.sign_in_option = self.browser.find_element_by_xpath('//a[@data-automation="sign-in-container"]')
        except NoSuchElementException:
            time.sleep(random.randint(1, 3))
            self.get_login_element()
        print("Got Login Element")

    def click_login_element(self):
        try:
            self.sign_in_option.click()
        except ElementNotInteractableException:
            time.sleep(random.randint(1, 3))
            self.click_login_element()
        print('Clicked login element')

    def get_username_element(self):
        time.sleep(random.randint(1, 3))
        try:
            self.email_field = self.browser.find_element_by_id("username")
        except NoSuchElementException:
            self.get_username_element()
        print('Got username element')

    def slow_typing(self, element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(0.15)

    def fill_in_username(self):
        try:
            self.email_field.clear()
            self.slow_typing(self.email_field, self.username)
        except (ElementNotInteractableException, NoSuchElementException):
            time.sleep(random.randint(3, 6))
            self.fill_in_username()
        # Determine whether the name has been successfully typed into the username box
        if self.browser.find_element_by_xpath(f'//input[@value="{self.username}"]'):
            print("filled in username")
        else:
            self.fill_in_username()


    def get_password_element(self):
        try:
            self.password_field = self.browser.find_element_by_id('password')
        except NoSuchElementException:
            self.get_password_element()
        print("Got password element")
    
    def fill_in_password(self):
        try:
            self.password_field.clear()
            self.slow_typing(self.password_field, self.password)
        except (NoSuchElementException, ElementNotInteractableException):
            time.sleep(random.randint(3, 6))
            self.fill_in_password()
        if self.browser.find_element_by_xpath(f'//input[@value="{self.password}"]'):
            print("filled in password")
        else:
            self.fill_in_password()
        
    def get_sign_in_button(self):
        try:
            self.sign_in_button = self.browser.find_element_by_xpath('//button[@data-automation="form-btn"]')
        except (ElementNotInteractableException, NoSuchElementException):
            time.sleep(random.randint(3, 5))
            self.get_sign_in_button()
        print("Got sign in button element")

    
    def click_sign_in_button(self):
        try:
            self.sign_in_button.click()
        except (ElementNotInteractableException, NoSuchElementException):
            self.get_sign_in_button()
        print('clicked Sign in button')


    def go_to_product_page(self):
        time.sleep(random.randint(2, 4))
        # self.browser.get('https://www.walmart.ca/en/ip/playstation5-console/6000202198562')
        self.browser.get('https://www.walmart.ca/en/ip/call-of-duty-black-ops-cold-war-ps4/6000201790883')
        print('loaded product page')
        self.get_add_to_cart_button()

    def remove_dropdown(self):
        time.sleep(random.randint(5, 8))
        print("moving mouse to x drop-down")
        pyautogui.moveTo(966, 131, 1.2)
        pyautogui.click()
        print("x-ed drop down")

    def get_add_to_cart_button(self):
        time.sleep(random.randint(2, 4))
        try:
            self.add_to_cart_button = self.browser.find_element(By.XPATH, "//*[text()='Add to cart']")
        except (NoSuchElementException, ElementNotInteractableException):
            time.sleep(random.randint(8, 15))
            print("Add to cart button not available, refreshing")
            self.go_to_product_page()
        print("Got add to cart button")
    
    def click_add_to_cart_button(self):
        try:
            self.add_to_cart_button.send_keys(Keys.ENTER)
        except (NoSuchElementException, ElementNotInteractableException):
            time.sleep(random.randint(1, 2))
            self.click_add_to_cart_button()
        print("clicked add to cart button")

    def get_checkout_button(self):
        try:
            self.checkout_button = self.browser.find_element(By.XPATH, "//*[text()='Checkout']")
        except NoSuchElementException:
            time.sleep(random.randint(3, 6))
            self.get_checkout_button()
        print("Got checkout button")

    def click_checkout_button(self):
        try:
            self.checkout_button.send_keys(Keys.ENTER)
        except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException):
            self.get_checkout_button()
        print("Clicked checkout button")


    #def get_final_checkout_button(self):
     #   time.sleep(random.randint(3, 6))
      #  try:
       #     self.proceed_to_checkout = self.browser.find_element(By.XPATH, "//*[text()='Proceed to checkout']")
       # except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException):
        #    self.get_final_checkout_button()
        # print("Got final checkout button")
        # self.click_final_checkout_button()
    
    #def click_final_checkout_button(self):
     #   try:
      #      self.proceed_to_checkout.send_keys(Keys.ENTER)
        # except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException):
         #   self.get_final_checkout_button()
        #print("Clicked final checkout button")


    # def click_final_checkout_button_with_gui(self):
      #  time.sleep(random.randint(3, 5))
       # pyautogui.moveTo(619, 488, 1.0)
        # pyautogui.click()

    def go_to_final_checkout_page(self):
        time.sleep(random.randint(2, 5))
        self.browser.get('https://www.walmart.ca/checkout')
        print("Loaded place order page")


    def get_security_box_element(self):
        time.sleep(random.randint(3, 6))
        try:
            self.security_box = self.browser.find_element_by_xpath('//input[@data-automation="securityCode-input"]')
        except (ElementNotInteractableException, NoSuchElementException):
            self.get_security_box_element()
        print("Got security box element")
        self.fill_in_security_box()

    def fill_in_security_box(self):
        try:
            self.slow_typing(self.security_box, self.security_code)
        except (ElementNotInteractableException, NoSuchElementException):
            self.get_security_box_element()
        print("Filled in security box")


    def get_confirm_button(self):
        try:
            self.confirm_button = self.browser.find_element_by_id('cvvConfirm')
        except (ElementNotInteractableException, NoSuchElementException):
            time.sleep(random.randint(1, 3))
            self.get_confirm_button()
        print("Got confirm button")
        self.click_confirm_button()

    def click_confirm_button(self):
        try:
            self.confirm_button.send_keys(Keys.ENTER)
        except (ElementNotInteractableException, NoSuchElementException):
            self.get_confirm_button()
        print("Clicked confirm button")

    #def get_place_order_button(self):
     #   time.sleep(random.randint(2, 3))
      #  try:
       #     self.place_order_button = self.browser.find_element(By.XPATH, "//*[text()='Place order']")
        #except (ElementNotInteractableException, NoSuchElementException):
         #   time.sleep(random.randint(1, 3))
          #  self.get_place_order_button()
        #print("Got place order button")
        #self.click_place_order_button()

    #def click_place_order_button(self):
     #   try:
      #      self.place_order_button.send_keys(Keys.ENTER)
       # except (ElementNotInteractableException, NoSuchElementException):
        #    time.sleep(random.randint(1, 3))
         #   self.get_place_order_button()
        # print("Clicked place order button. Congratulations Haardik, hope you enjoy your ps5.")

    def use_gui_to_place_order(self):
        print("moving mouse")
        pyautogui.moveTo(865, 426, 1.0)
        pyautogui.click()
        print("clicked place order button successfully.")



    

a = BuyingAPlaystation()
a.avoid_detection()
a.startup_and_go_to_walmart()
a.get_login_element()
a.click_login_element()

a.get_username_element()
a.fill_in_username()

a.get_password_element()
a.fill_in_password()

a.get_sign_in_button()
a.click_sign_in_button()
a.remove_dropdown()

a.go_to_product_page()
a.click_add_to_cart_button()
a.get_checkout_button()
a.click_checkout_button()

a.go_to_final_checkout_page()
a.get_security_box_element()
a.get_confirm_button()
a.use_gui_to_place_order()







