import sys
sys.path.append('../')
import unittest
from LedSwitcher import *

class Test(unittest.TestCase):


    # Testing each method...

    def testParseFileMethodSmall(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3d.txt")
        self.assertTrue(len(self.a.parseFile()) == 1001)

    def testGetSizeSmall(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3d.txt")
        self.a.parseFile()
        self.assertTrue(self.a.getSize() == 1000)

    def testGetParseLinesSmall(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3d.txt")
        self.a.parseFile()
        self.a.getSize()
        self.assertTrue(len(self.a.getParseLines()) == 1000)

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

    # Testing parsing of each line...

    def testLineParsingNormal(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.a.getSize()
        self.assertTrue(self.a.parseEachLine("turn on 619,181 through 736,944") == [True, 619, 181, 736, 944])

    def testLineParsingCommaSpace(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.a.getSize()
        self.assertTrue(self.a.parseEachLine("switch 857,894 through 920 ,932") == [None, 857, 894, 920, 932])

    # With supplied test files...

    def testGetResultAssign3(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 400410)

    def testGetResultAssign3a(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3a.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 7)

    def testGetResultAssign3b(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3b.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 29942250)

    def testGetResultAssign3c(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3c.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 477452)

    def testGetResultAssign3d(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3d.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 349037)

if __name__ == '__main__':
    unittest.main()