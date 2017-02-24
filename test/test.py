import sys
sys.path.append('../src')
import unittest
from main import *

class Test(unittest.TestCase):

    def testParseFileMethod(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.assertTrue(len(self.a.parseFile()) != 0)

if __name__ == '__main__':
    unittest.main()