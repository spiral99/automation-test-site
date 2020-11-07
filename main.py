import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.action_chains import ActionChains


class MyListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        print("Before navigating to ", url)

    def after_navigate_to(self, url, driver):
        print("After navigating to ", url)

    def before_navigate_back(self, driver):
        print("before navigating back ", driver.current_url)

    def after_navigate_back(self, driver):
        print("After navigating back ", driver.current_url)

    def before_navigate_forward(self, driver):
        print("before navigating forward ", driver.current_url)

    def after_navigate_forward(self, driver):
        print("After navigating forward ", driver.current_url)

    def before_find(self, by, value, driver):
        print("before find")

    def after_find(self, by, value, driver):
        print("after_find")

    def before_click(self, element, driver):
        print("before_click")

    def after_click(self, element, driver):
        print("after_click")

    def before_change_value_of(self, element, driver):
        print("before_change_value_of")

    def after_change_value_of(self, element, driver):
        print("after_change_value_of")

    def before_execute_script(self, script, driver):
        print("before_execute_script")

    def after_execute_script(self, script, driver):
        print("after_execute_script")

    def before_close(self, driver):
        print("FIN")

    def after_close(self, driver):
        print("before_close")

    def before_quit(self, driver):
        print("before_quit")

    def after_quit(self, driver):
        print("after_quit")

    def on_exception(self, exception, driver):
        print("on_exception")


class Test(unittest.TestCase):
    def test_Beyonic_file(self):
        driver_plain = webdriver.Firefox(executable_path="d:\\geckodriver.exe")
        driver = EventFiringWebDriver(driver_plain, MyListener())
        driver.get("https://apidocs.beyonic.com/")
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver.maximize_window()
        sleep(12)
        action = ActionChains(driver)
        driver.find_element(By.ID, "input-search").click()
        action.send_keys("Listing all")
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        driver.find_element(By.LINK_TEXT, "Listing all Payments").click()
        element1 = driver.find_element_by_xpath("//*[@href='#listing-all-payments']").text
        print("This will return a", element1)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Listing all Contacts").click()
        element2 = driver.find_element_by_xpath("//*[@href='#listing-all-contacts']").text
        print("This will return a", element2)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Listing all transactions").click()
        element3 = driver.find_element_by_xpath("//*[@href='#listing-all-transactions']").text
        print("This will return a", element3)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Listing all Events").click()
        element4 = driver.find_element_by_xpath("//*[@href='#listing-all-events']").text
        print("This will return a", element4)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Listing all Collections").click()
        element5 = driver.find_element_by_xpath("//*[@href='#listing-all-collections']").text
        print("This will return a", element5)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Listing all webhooks").click()
        element6 = driver.find_element_by_xpath("//*[@href='#listing-all-webhooks']").text
        print("This will return a", element6)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Listing all networks").click()
        element7 = driver.find_element_by_xpath("//*[@href='#listing-all-networks']").text
        print("This will return a", element7)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Listing all accounts").click()
        element8 = driver.find_element_by_xpath("//*[@href='#listing-all-accounts']").text
        print("This will return a", element8)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Listing all currencies").click()
        element9 = driver.find_element_by_xpath("//*[@href='#listing-all-currencies']").text
        print("This will return a", element9)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Listing all Collection Requests").click()
        element10 = driver.find_element_by_xpath("//*[@href='#listing-all-collection-requests']").text
        print("This will return a", element10)
        sleep(2)

        driver.find_element(By.LINK_TEXT, "Collection Requests").click()
        element101 = driver.find_element_by_xpath("//aside[8]").text
        print(element101)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Collections").click()
        element102 = driver.find_element_by_xpath("//aside[9]").text
        print(element102)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Payments").click()
        element103 = driver.find_element_by_xpath("//aside[10]").text
        print(element103)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Currencies").click()
        element104 = driver.find_element_by_xpath("//aside[11]").text
        print(element104)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Networks").click()
        element105 = driver.find_element_by_xpath("//aside[12]").text
        print(element105)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Banks").click()
        element106 = driver.find_element_by_xpath("//aside[13]").text
        print(element106)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Accounts").click()
        element107 = driver.find_element_by_xpath("//aside[14]").text
        print(element107)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Transactions").click()
        element108 = driver.find_element_by_xpath("//aside[15]").text
        print(element108)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Contacts").click()
        element109 = driver.find_element_by_xpath("//aside[16]").text
        print(element109)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Events").click()
        element1010 = driver.find_element_by_xpath("//aside[17]").text
        print(element1010)
        sleep(2)
        driver.find_element(By.LINK_TEXT, "Webhooks").click()
        element1011 = driver.find_element_by_xpath("//aside[18]").text
        print(element1011)
        sleep(2)

        test_output = open("D:/test.txt", "w+")
        test_output.write(element101 + '\n')
        test_output.write(element102 + '\n')
        test_output.write(element103 + '\n')
        test_output.write(element104 + '\n')
        test_output.write(element105 + '\n')
        test_output.write(element106 + '\n')
        test_output.write(element107 + '\n')
        test_output.write(element108 + '\n')
        test_output.write(element109 + '\n')
        test_output.write(element1010 + '\n')
        test_output.write(element1011 + '\n')
        test_output.close()

        f1 = open("D:/test.txt", "r")
        f2 = open("D:/endpoints.txt", "r")
        f3 = open("D:/undocumented_endpoints.txt", "w")

        file1_raw = f1.read()
        file2_raw = f2.read()

        file1_words = file1_raw.split()
        file2_words = file2_raw.split()

        result1 = set(file1_words).difference(file2_words)
        result2 = set(file2_words).difference(file1_words)

        results = result1.union(result2)

        for endpoints in set(results):
            f3.write(endpoints + "\n")
        
        f1.close()
        f2.close()
        f3.close()

        driver.quit()


if __name__ == "__main__":
    unittest.main()
