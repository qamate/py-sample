import unittest
from factory.driverfactory import Driver
from factory.pagefactory import PageFactory


class SeleniumSearch(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver = self.driver.start( "Firefox" )
        self.driver.get( "http://www.seleniumhq.org/" )

    def runTest(self):
        menu_page = PageFactory().getPage( "menuPage", self.driver );
        menu_page.typeSearch( "Page Object" );
        menu_page.submit();

        resultpage = PageFactory().getPage("resultPage", self.driver);

        tex = resultpage.findResult().text
        print (tex)
        tex = tex.split()
        tex= tex[1]

        if ("," in tex):
            tex = tex.replace(",","");

        self.assertTrue(int(tex) > 1);  #checks for result is more than 1 for valid search




    def tearDown(self):
        self.driver.quit()


