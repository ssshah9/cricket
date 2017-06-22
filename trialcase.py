# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:00:29 2017

@author: siddhant
"""

import unittest
from cric import towin

class CricketTestCase(unittest.TestCase):
    
    def test_winner(self):
        self.assertTrue(towin('235831.yaml') == 'Pakistan')
  
def main():
    unittest.main()
      
if __name__ == '__main__':
    main()
    