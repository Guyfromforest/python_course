#Task1 спеціально Failed,aби працювало треба додати round(cos(2))

from math import cos
import unittest

class FitstTestCase(unittest.TestCase):#,for Failure
    def test_cos(self):
        t1=(cos(2))
        self.assertEquals(t1,0)
unittest.main