#!/usr/bin/env python

import unittest
import os
from selenium import webdriver


class CantTestThis(unittest.TestCase):

   def setup(self):
      self.se_grid_server = os.environ.get('SE_GRID_SERVER')
      self.remote_webdriver_url = '{}/wd/hub'.format(self.se_grid_server)
      self.browsers_to_test = { 'firefox': webdriver.DesiredCapabilities.FIREFOX.copy(), 
                                'chrome': webdriver.DesiredCapabilities.CHROME.copy(), 
                              }



   def teardown(self):
      pass

 
   def test_get_env_var(self):
       self.assertIsNotNone(self.se_grid_server)
       
       
   def test_remote_webdriver(self):
       # how to remove a browser from a test
       del self.browsers_to_test['chrome']
       
       for each_browser in self.browsers_to_test:
       	 driver = webdriver.Remote(self.remote_webdriver_url, self.browsers_to_test[each_browser])
         driver.get('http://www.google.com')
         self.assertEqual(driver.title, 'Google')


   def test_q2smart_hit(self):
   
       for each_browser in self.browsers_to_test:
       	 driver = webdriver.Remote(self.remote_webdriver_url, self.browsers_to_test[each_browser])
         driver.get('https://q2smart-preprod.q2ebanking.com/000000014/test/#/login')
         self.assertEqual(driver.title, 'Goat')
   
