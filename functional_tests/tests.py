from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

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
        #self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)

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
        scooter_list_url = self.browser.current_url
        self.assertRegex(scooter_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy some chew bones')
                
        # text box remains, Scooter enters "Chew bone and and sleep"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Chew bone and sleep')
        inputbox.send_keys(Keys.ENTER)

        # page updates, both list items are shown
        self.check_for_row_in_list_table('1: Buy some chew bones')
        self.check_for_row_in_list_table('2: Chew bone and sleep')
            
        # now a new user, Spike, comes along to the site
        ## we use a new browser session to make sure that no information
        ## of scooter's list is coming thourgh from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Spike visits the home page, no sign of Scooter's list apparent
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy some chew bones', page_text)
        self.assertNotIn('make a fly', page_text)

        # Spike starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy pig ear')
        inputbox.send_keys(Keys.ENTER)

        # Spike gets his own unique URL
        spike_list_url = self.browser.current_url
        self.assertRegex(spike_list_url, '/lists/.+')
        self.assertNotEqual(spike_list_url, scooter_list_url)

        # Again, no trace of scooter's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy some chew bones', page_text)
        self.assertIn('Buy pig ear', page_text)

        # satisfied, they both blep




        # scooter takes note of url to save his list
        #self.fail('Finish the test!')

        # scooter visits the url, his to-do list is still there
        # satisfied, he chews his bone on his bed