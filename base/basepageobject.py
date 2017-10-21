import unittest

class basePageObject(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver