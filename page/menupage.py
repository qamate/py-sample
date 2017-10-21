from selenium.webdriver.common.by import By
from base.basepageobject import basePageObject

class menuPage(basePageObject):

    go = (By.XPATH, "//input[@value = 'Go']")
    query = (By.ID, "q")

    def typeSearch(self, query):
        self.driver.find_element(*menuPage.query).send_keys(query);

    def submit(self):
        self.driver.find_element(*menuPage.go).click()