import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        user = "testuser"
        pwd = "test123"

        # log in as user
        driver.get("http://127.0.0.1:8000/accounts/login/")
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        # adds tuxedo to cart
        driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Add to cart']").click()
        time.sleep(3)

        # clicks continue shopping
        driver.find_element(By.CSS_SELECTOR, "a[href='/'][class='button light']").click()
        time.sleep(3)

        # adds pinstripe suit to cart
        driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/form/input[2]').click()
        time.sleep(3)

        # clicks continue shopping
        driver.find_element(By.CSS_SELECTOR, "a[href='/'][class='button light']").click()
        time.sleep(3)

        # adds blazer set
        driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[3]/form/input[2]').click()
        time.sleep(3)

        # updates quantity to 2
        driver.find_element(By.XPATH, '//*[@id="id_quantity"]/option[2]').click()
        time.sleep(3)

        # clicks update
        driver.find_element(By.XPATH, '//*[@id="content"]/table/tbody/tr[1]/td[3]/form/input[3]').click()
        time.sleep(3)

        # clicks checkout
        driver.find_element(By.CSS_SELECTOR, "a[href='/orders/create/']").click()

        # checkout information
        time.sleep(3)
        first_name = "Group"
        last_name = "Four"
        email = "group4@gmail.com"
        address = "Group Four Drive"
        postal_code = "444444"
        city = "Omaha"

        # fills in first name
        elem = driver.find_element(By.ID, "id_first_name")
        elem.send_keys(first_name)

        # fills in last name
        elem = driver.find_element(By.ID, "id_last_name")
        elem.send_keys(last_name)

        # fills in email
        elem = driver.find_element(By.ID, "id_email")
        elem.send_keys(email)

        # fills in address
        elem = driver.find_element(By.ID, "id_address")
        elem.send_keys(address)

        # fills in postal code
        elem = driver.find_element(By.ID, "id_postal_code")
        elem.send_keys(postal_code)

        # fills in city
        elem = driver.find_element(By.ID, "id_city")
        elem.send_keys(city)

        time.sleep(5)
        elem.send_keys(Keys.RETURN)

        time.sleep(5)

        driver.find_element(By.XPATH, '/html/body/div[2]/form/button').click()
        time.sleep(3)



if __name__ == "__main__":
    unittest.main()