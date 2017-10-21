from page.menupage import menuPage
from page.resultpage import resultPage

class PageFactory():

    def getPage(self, pageName, driver):

        if pageName == "menuPage":
            return menuPage( driver )

        elif pageName == "resultPage":
            return resultPage(driver)
        
