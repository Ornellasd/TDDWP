from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Scooter goes to checkout the homepage
        self.browser.get('http://localhost:8000')

        # He notices page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # he is invited to enter a to-do
        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # he types "Buy bones" in text box
        inputbox.send_keys('Buy some chew bones')
        
        # he hits enter and now "Buy bones" appears as to-do item
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy some chew bones' for row in rows),
            "New to-do item did not appear in table"
        )

        # text box remains, Scooter enters "sleep and poop"
        self.fail('Finish the test!')

        ## User stories ##
        # page updates, both list items are shown
        
        # scooter takes not of url to save his list
        
        # Scooter derps
        
if __name__ == '__main__':
    unittest.main(warnings='ignore') 