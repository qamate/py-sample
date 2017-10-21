from selenium.webdriver.common.by import By
from base.basepageobject import basePageObject

class resultPage(basePageObject):

    result = (By.XPATH, '//*[@id="resInfo-0"]')

    def findResult(self):
        e = self.driver.find_element(*resultPage.result);
        return e;

