import sys
sys.path.append('../src')
import unittest
from main import *

class Test(unittest.TestCase):

    def testParseFileMethodSmall(self):
        self.a = LedSwitcher("../test/testinputs/testLength5.txt")
        self.assertTrue(len(self.a.parseFile()) == 4)

    def testGetSizeSmall(self):
        self.a = LedSwitcher("../test/testinputs/testLength5.txt")
        self.a.parseFile()
        self.assertTrue(self.a.getSize() == 5)

    def testGetParseLinesSmall(self):
        self.a = LedSwitcher("../test/testinputs/testLength5.txt")
        self.a.parseFile()
        self.a.getSize()
        self.assertTrue(len(self.a.getParseLines()) == 3)

    def testGetResultSmall(self):
        self.a = LedSwitcher("../test/testinputs/testLength5.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 17)

    def testParseFileMethod(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.assertTrue(len(self.a.parseFile()) != 0)

    def testGetSize(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.assertTrue(self.a.getSize() == 1000)

    def testGetParseLines(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.a.getSize()
        self.assertTrue(len(self.a.getParseLines()) == 300)

    def testGetResult(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 400410)

if __name__ == '__main__':
    unittest.main()