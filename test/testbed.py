# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:09:01 2017

@author: rjr
"""


# Testbed


import unittest
import pytest


# content of test_sample.py
def func(x):
    return x + 1

def answer():
    assert func(3) == 5

"""
class MyTest(unittest.TestCase):
    
    def test(self):
        self.assertEqual(add(1, 1), 4)



z = MyTest()
print(z.test())
"""