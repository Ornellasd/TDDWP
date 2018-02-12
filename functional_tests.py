from selenium import webdriver

## User stories ##

# he is invited to enter a to-do

# he types "Buy bones" in text box

# he hits enter and now "Buy bones" appears as to-do item

# text box remains, Scooter enters "sleep and poop"

# page updates, both list items are shown

# scooter takes not of url to save his list

# Scooter derps

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.broser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Scooter goes to checkout the homepage
        self.browser.get('http://localhost:8000')

        # He notices tile mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore') 