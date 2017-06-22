# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:25:12 2017

@author: siddhant
"""
#import unittest

#class Cricket(object):
    
def towin(file):
        with open(file, 'r') as f:

            for line in f:
                if line.__contains__('winner'):
                    lhs, rhs = line.split(": ")
                    print('The match was won by ' + rhs )
                    print('India lost')
                    print('pak shoulnt have won, I cant believe Pak won')
                    return str.strip(rhs)
                #f.close()
    

"""  
class CricketTest(unittest.TestCase)
         
     def test_cric(self):
             self.assertTrue(towin('235831.yaml'))
       
def main():
         unittest.main()
         
if __name__ == '__main__':
        main()

"""
    
 # print (f)
 # print (f.read()) shows file as is    
    
    
    