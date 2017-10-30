#!/usr/bin/env python

import unittest
import os
from selenium import webdriver
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.CRITICAL)


class CantTestThis(unittest.TestCase):

   def setUp(self):
      self.se_grid_server = os.environ.get('SE_GRID_SERVER')
      self.test_URL = os.environ.get('TEST_URL')
      self.test_URL_title = os.environ.get('TEST_URL_TITLE')
      self.remote_webdriver_url = '{}/wd/hub'.format(self.se_grid_server)
      self.browsers_to_test = { 'firefox': webdriver.DesiredCapabilities.FIREFOX.copy(), 
                                'chrome': webdriver.DesiredCapabilities.CHROME.copy(), 
                              }
      logging.debug('setUp.')


   def tearDown(self):
      pass

 
   def test_get_env_var(self):
       self.assertIsNotNone(self.se_grid_server)
       
       
   def test_remote_webdriver(self):
       # how to remove a browser from a test
       del self.browsers_to_test['chrome']
       logging.debug('test_remote_webdriver')
       
       for each_browser in self.browsers_to_test:
         logging.debug(each_browser)
         try:
	       	 driver = webdriver.Remote(self.remote_webdriver_url, self.browsers_to_test[each_browser])
	         driver.get('http://www.google.com')
	         self.assertEqual(driver.title, 'Google')
         finally:
	     	 driver.quit()


   def test_testURL_hit(self):
       del self.browsers_to_test['chrome']
       logging.debug('test_testURL_hit')
   
       for each_browser in self.browsers_to_test:
         logging.debug(each_browser)
         try:
             driver = webdriver.Remote(self.remote_webdriver_url, self.browsers_to_test[each_browser])
             driver.get(self.test_URL)
             self.assertEqual(driver.title, self.test_URL_title)
         finally:
	     	 driver.quit()
   
