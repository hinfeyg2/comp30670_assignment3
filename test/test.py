import sys
sys.path.append('../')
import unittest
from LedSwitcher import *

class Test(unittest.TestCase):

    # Testing each method...

    def testParseFileMethodSmall(self):
        """Tests that the class is reading the correct number of lines in a file"""

        self.a = LedSwitcher("../test/testinputs/input_assign3d.txt")
        self.assertTrue(len(self.a.parseFile()) == 1001)

    def testGetParseLines3d(self):
        """Makes sure that the Parselines method is examining all lines in the file"""

        self.a = LedSwitcher("../test/testinputs/input_assign3d.txt")
        self.a.parseFile()
        self.a.getSize()
        self.assertTrue(len(self.a.getParseLines()) == 1000)

    def testGetParseLines3(self):
        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.a.getSize()
        self.assertTrue(len(self.a.getParseLines()) == 300)

    def testGetResultSmall(self):
        """Tests the whole program on a small custom data set."""

        self.a = LedSwitcher("../test/testinputs/testLength5.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 17)

    def testParseFileMethod(self):
        """Makes sure that parseFile is reading an input."""

        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.assertTrue(len(self.a.parseFile()) != 0)

    def testGetSize(self):
        """Asserts that the getSize method is working correctly"""

        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.assertTrue(self.a.getSize() == 1000)

    # Testing parsing of each line...

    def testLineParsingNormal(self):
        """testing the line parsing output."""

        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.a.getSize()
        self.assertTrue(self.a.parseEachLine("turn on 619,181 through 736,944") == [True, 619, 181, 736, 944])

    def testLineParsingCommaSpace(self):
        """testing the line parsing output."""

        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.a.getSize()
        self.assertTrue(self.a.parseEachLine("switch 857,894 through 920 ,932") == [None, 857, 894, 920, 932])

    # With supplied test files...

    def testGetResultAssign3(self):
        """Test result against input files."""

        self.a = LedSwitcher("../test/testinputs/input_assign3.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 400410)

    def testGetResultAssign3a(self):
        """Test result against input files."""

        self.a = LedSwitcher("../test/testinputs/input_assign3a.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 7)

    def testGetResultAssign3b(self):
        """Test result against input files."""

        self.a = LedSwitcher("../test/testinputs/input_assign3b.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 29942250)

    def testGetResultAssign3c(self):
        """Test result against input files."""

        self.a = LedSwitcher("../test/testinputs/input_assign3c.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 477452)

    def testGetResultAssign3d(self):
        """Test result against input files."""

        self.a = LedSwitcher("../test/testinputs/input_assign3d.txt")
        self.a.parseFile()
        self.a.getSize()
        self.a.getParseLines()
        self.a.applyValues()
        self.assertTrue(self.a.getResult() == 349037)

if __name__ == '__main__':
    unittest.main()