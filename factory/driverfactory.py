from appium import webdriver
from selenium import webdriver

class Driver():

    def start(self, driverType, implicitWait=15):
        if driverType == 'Firefox':
            self.driver = webdriver.Firefox( )
        elif driverType == 'Chrome':
            self.driver = webdriver.Chrome( )
        elif driverType == 'IE':
            self.driver = webdriver.Ie( )
        else:
            raise Exception( 'Unknown webdriver type' )

        self.driver.implicitly_wait( implicitWait )

        return self.driver

    def get(self, url):
        try:
            self.driver.get( url )
        except:
            raise

    def close(self):
        try:
            self.driver.close( )
        except:
            raise