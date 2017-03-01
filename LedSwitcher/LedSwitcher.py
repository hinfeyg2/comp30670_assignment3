import sys
from urllib.request import urlopen

class LedSwitcher:
	
	def __init__(self, filename):

		self.filename = filename
		self.listTest = []
		self.switchSize = 0
		# self.dictionaryTest[curX,curY] = state

	def parseFile(self):
		"""This method opens the file containing the assigned data input.
		It returns a list with each line in that file or url. It avoids empty lines."""

		firstLineCount = 0
		if self.filename[:4] == "http":
			for line in urlopen(self.filename):
				line = line.decode("utf-8")
				line = line.strip()
				if firstLineCount == 0:
					self.switchSize = int(line)
					firstLineCount = firstLineCount + 1
				elif len(line) > 1:
					if self.parseEachLine(line) != True:
						self.applyValues(self.parseEachLine(line))

		else:
			with open(self.filename) as f:
				self.switchSize = int(f.readline())
				for line in f:
					if len(line) > 1:
						if self.parseEachLine(line) != True:
							self.applyValues(self.parseEachLine(line))
			f.closed
		return len(self.listTest)

	def parseEachLine(self, x):
		"""this file parses the data from each line and returns a list with the results."""
		
		x = x.strip()

		if ", " in x:
			x = x.replace(", ", ",")
		elif " ," in x:
			x = x.replace(" ,", ",")

		lineSplitSpaceList = x.split(" ")

		if lineSplitSpaceList[0] == "turn" and lineSplitSpaceList[1] == "on":

			xStart = lineSplitSpaceList[2].split(",")[0].strip()
			yStart = lineSplitSpaceList[2].split(",")[1].strip()
			xEnd = lineSplitSpaceList[4].split(",")[0].strip()
			yEnd = lineSplitSpaceList[4].split(",")[1].strip()
			result = [True, max(0, min(int(xStart), self.switchSize - 1)), max(0, min(int(yStart), self.switchSize - 1)), max(0, min(int(xEnd), self.switchSize - 1)), max(0, min(int(yEnd), self.switchSize - 1))]
			return result

		elif lineSplitSpaceList[0] == "turn" and lineSplitSpaceList[1] == "off":
			xStart = lineSplitSpaceList[2].split(",")[0].strip()
			yStart = lineSplitSpaceList[2].split(",")[1].strip()
			xEnd = lineSplitSpaceList[4].split(",")[0].strip()
			yEnd = lineSplitSpaceList[4].split(",")[1].strip()
			result = [False, max(0, min(int(xStart), self.switchSize - 1)), max(0, min(int(yStart), self.switchSize - 1)), max(0, min(int(xEnd), self.switchSize - 1)), max(0, min(int(yEnd), self.switchSize - 1))]
			return result

		elif lineSplitSpaceList[0] == "switch":
			xStart = lineSplitSpaceList[1].split(",")[0].strip()
			yStart = lineSplitSpaceList[1].split(",")[1].strip()
			xEnd = lineSplitSpaceList[3].split(",")[0].strip()
			yEnd = lineSplitSpaceList[3].split(",")[1].strip()
			result = [None, max(0, min(int(xStart), self.switchSize - 1)), max(0, min(int(yStart), self.switchSize - 1)), max(0, min(int(xEnd), self.switchSize - 1)), max(0, min(int(yEnd), self.switchSize - 1))]
			return result
		return (True)

	def changeState(self, curX, curY, state):
		"""a method for changing the state of the ledStateList with and an input position and state"""
		tempTuple = [curX, curY]
		if state is None:
			if tempTuple in self.listTest:
				self.listTest.remove(tempTuple)
			else:
				self.listTest.append(tempTuple)
		elif state:
			if tempTuple not in self.listTest:
				self.listTest.append(tempTuple)
		else:
			if tempTuple in self.listTest:
				self.listTest.remove(tempTuple)

	def applyValues(self, lineItem):
		"""Apply the valus in the parseList to the ledStateList"""
		for a in range(lineItem[1], lineItem[3] + 1):
			for b in range(lineItem[2], lineItem[4] + 1):
				self.changeState(a, b, lineItem[0])

def main():
	"""This function is used when running the setup.py entry points."""
	a = LedSwitcher(sys.argv[1])
	print(a.parseFile())

if __name__ == '__main__':
	"""Run this if its the root python file."""
	a = LedSwitcher(sys.argv[1])
	print(a.parseFile())
