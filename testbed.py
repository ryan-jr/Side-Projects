# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:09:01 2017

@author: rjr
"""


# Testbed


import unittest
import pytest


def add(x, y):
    return x + y



def test_answer():
    assert add(3, 2) == 5


"""
class MyTest(unittest.TestCase):
    
    def test(self):
        self.assertEqual(add(1, 1), 4)



z = MyTest()
print(z.test())
"""