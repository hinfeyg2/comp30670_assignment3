import sys
sys.path.append('../')
import unittest
from LedSwitcher import *

class Test(unittest.TestCase):

    # Testing each method...

    # def testGetResultSmall(self):
    #     """Tests the whole program on a small custom data set."""

    #     a = LedSwitcher("../test/testinputs/testLength5.txt")
    #     self.assertTrue(a.parseFile() == 17)

    # def testGetSize(self):
    #     """Asserts that the getSize method is working correctly"""

    #     a = LedSwitcher("../test/testinputs/input_assign3.txt")
    #     a.parseFile()
    #     self.assertTrue(a.switchSize == 1000)

    # Testing parsing of each line...

    # def testLineParsingNormal(self):
    #     """testing the line parsing output."""

    #     a = LedSwitcher("../test/testinputs/input_assign3.txt")
    #     a.parseFile()
    #     self.assertTrue(a.parseEachLine("turn on 619,181 through 736,944") == [True, 619, 181, 736, 944])

    # def testLineParsingCommaSpace(self):
    #     """testing the line parsing output."""

    #     a = LedSwitcher("../test/testinputs/input_assign3.txt")
    #     a.parseFile()
    #     self.assertTrue(a.parseEachLine("switch 857,894 through 920 ,932") == [None, 857, 894, 920, 932])

    # # # With supplied test files...

    # def testGetResultAssign3Web(self):
    #     """Test result against input files from web."""

    #     self.a = LedSwitcher("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    #     self.a.parseFile()
    #     self.assertTrue(self.a.getResult() == 400410)

    def testGetResultAssign3Local(self):
        """Test result against input files."""

        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.assertTrue(self.a.parseFile() == 400410)

    # def testGetResultAssign3a(self):
    #     """Test result against input files."""

    #     self.a = LedSwitcher("../test/testinputs/input_assign3a.txt")
    #     self.assertTrue(self.a.parseFile() == 7)

    # def testGetResultAssign3b(self):
    #     """Test result against input files."""

    #     self.a = LedSwitcher("../test/testinputs/input_assign3b.txt")
    #     self.a.parseFile()
    #     self.assertTrue(self.a.getResult() == 29942250)

    # def testGetResultAssign3c(self):
    #     """Test result against input files."""

    #     self.a = LedSwitcher("../test/testinputs/input_assign3c.txt")
    #     self.a.parseFile()
    #     self.assertTrue(self.a.getResult() == 477452)

    # def testGetResultAssign3d(self):
    #     """Test result against input files."""

    #     self.a = LedSwitcher("../test/testinputs/input_assign3d.txt")
    #     self.assertTrue(self.a.parseFile() == 349037)

if __name__ == '__main__':
    unittest.main()