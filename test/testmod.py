#!/usr/bin/env python

import unittest
import os
from selenium import webdriver
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class CantTestThis(unittest.TestCase):

   def setUp(self):
      self.se_grid_server = os.environ.get('SE_GRID_SERVER')
      self.remote_webdriver_url = '{}/wd/hub'.format(self.se_grid_server)
      self.browsers_to_test = { 'firefox': webdriver.DesiredCapabilities.FIREFOX.copy(), 
                                'chrome': webdriver.DesiredCapabilities.CHROME.copy(), 
                              }
      logging.debug('setUp.')


   def tearDown(self):
      pass

 
   def test_get_env_var(self):
       self.assertIsNotNone(self.se_grid_server)
       
       
   def trest_remote_webdriver(self):
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


   def test_q2smart_hit(self):
       del self.browsers_to_test['chrome']
       logging.debug('test_q2smart_hit')
   
       for each_browser in self.browsers_to_test:
         logging.debug(each_browser)
         try:
	         driver = webdriver.Remote(self.remote_webdriver_url, self.browsers_to_test[each_browser])
    	     driver.get('https://q2smart-preprod.q2ebanking.com/000000014/test/#/login')
        	 self.assertEqual(driver.title, 'Goat')
         finally:
	     	 driver.quit()
   
