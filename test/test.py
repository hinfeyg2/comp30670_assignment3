import sys
sys.path.append('../')
import unittest
from LedSwitcher import *

class Test(unittest.TestCase):

    # Testing each method...

    def testGetResultSmall(self):
        """Tests the whole program on a small custom data set."""

        a = LedSwitcher("../test/testinputs/testLength5.txt")
        a.parseFile()
        self.assertTrue(a.getResult() == 17)

    def testCreateTemplate(self):
        """Asserts that the createTemplate method is working correctly"""

        a = LedSwitcher("../test/testinputs/input_assign3.txt")
        a.parseFile()
        self.assertTrue(len(a.ledStateList) == 1000000)

    def testApplyValues(self):
        """Asserts that the applyValues method is working correctly"""

        a = LedSwitcher("../test/testinputs/test1LineItem.txt")
        a.parseFile()
        self.assertTrue(a.applyValues([True, 0, 0, 3, 3]) == 16)

    def testChangeState(self):
        """Asserts that the changeState method is working correctly"""

        a = LedSwitcher("../test/testinputs/test1LineItem.txt")
        a.parseFile()
        self.assertTrue(a.changeState(0, 0, True) == True)


    # Testing parsing of each line...

    def testLineParsingNormal(self):
        """testing the line parsing output."""

        a = LedSwitcher("../test/testinputs/input_assign3.txt")
        a.parseFile()
        self.assertTrue(a.parseEachLine("turn on 619,181 through 736,944") == [True, 619, 181, 736, 944])

    def testLineParsingCommaSpace(self):
        """testing the line parsing output."""

        a = LedSwitcher("../test/testinputs/input_assign3.txt")
        a.parseFile()
        self.assertTrue(a.parseEachLine("switch 857,894 through 920 ,932") == [None, 857, 894, 920, 932])

    # With supplied test files...

    def testGetResultAssign3Web(self):
        """Test result against input files from web."""

        a = LedSwitcher("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
        a.parseFile()
        self.assertTrue(a.getResult() == 400410)

    def testGetResultAssign3Local(self):
        """Test result against input files."""

        a = LedSwitcher("../test/testinputs/input_assign3.txt")
        a.parseFile()
        self.assertTrue(a.getResult() == 400410)

    def testGetResultAssign3a(self):
        """Test result against input files."""

        a = LedSwitcher("../test/testinputs/input_assign3_a_v2.txt")
        a.parseFile()
        self.assertTrue(a.getResult() == 11322278)

    def testGetResultAssign3b(self):
        """Test result against input files."""

        a = LedSwitcher("../test/testinputs/input_assign3_b_v2.txt")
        a.parseFile()
        self.assertTrue(a.getResult() == 42880639)

    def testGetResultAssign3c(self):
        """Test result against input files."""

        a = LedSwitcher("../test/testinputs/input_assign3c.txt")
        a.parseFile()
        self.assertTrue(a.getResult() == 477452)

    def testGetResultAssign3d(self):
        """Test result against input files."""

        a = LedSwitcher("../test/testinputs/input_assign3d.txt")
        a.parseFile()      
        self.assertTrue(a.getResult() == 349037)

if __name__ == '__main__':
    unittest.main()