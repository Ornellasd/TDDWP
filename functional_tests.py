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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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
        self.check_for_row_in_list_table('1: Buy some chew bones')
                
        # text box remains, Scooter enters "Chew bone and and sleep"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Chew bone and sleep')
        inputbox.send_keys(Keys.ENTER)

        # page updates, both list items are shown
        self.check_for_row_in_list_table('1: Buy some chew bones')
        self.check_for_row_in_list_table('2: Chew bone and sleep')
        
        # scooter takes note of url to save his list
        self.fail('Finish the test!')
        
        ## User stories ##
        
        
        
        
        # Scooter derps
        
if __name__ == '__main__':
    unittest.main(warnings='ignore') 