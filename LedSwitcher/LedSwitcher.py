import sys
from urllib.request import urlopen

class LedSwitcher:
	
	def __init__(self, filename):

		self.filename = filename

		# Will contain each line from the assigned input file.
		self.parseList = []
		# Will be set to how big the size of the LED array is.
		self.switchSize = 0
		# Will contain a list of each led and its associated state.
		self.ledStateList = []

	def parseFile(self):
		"""This method opens the file containing the assigned data input.
		It returns a list with each line in that file or url. It avoids empty lines."""
		
		if self.filename[:4] == "http":
			for line in urlopen(self.filename):
				line = line.decode("utf-8")
				line = line.strip()
				if len(line) > 1:
					self.parseList.append(line)
		else:
			with open(self.filename) as f:
				for line in f:
					if len(line) > 1:
						self.parseList.append(line.strip())
			f.closed
		return self.parseList


	def getSize(self):
		"""This method gets the size of the current LED array."""
		
		if len(self.parseList) == 0:
			return "List Empty"
		else:
			self.switchSize = int(self.parseList[0])
			for x in range(0, self.switchSize):
				for y in range(0, self.switchSize):
					self.ledStateList.append([False, x, y])
		return self.switchSize


	def getParseLines(self):
			"""take each line from the parse list and convert it to something readable.
			Perhaps this could be merged with the parseFile method to reduce iteratsion."""
			
			self.parseList.pop(0)
			for i in range(0, len(self.parseList)):
				self.parseList[i] = self.parseEachLine(self.parseList[i])
			return self.parseList


	def parseEachLine(self, x):

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


	def changeState(self, curX, curY, state):
		"""a method for changing the state of the ledStateList with and an input position and state"""

		Index = (curX * self.switchSize) + curY
		
		if state == None:
			boolean = self.ledStateList[Index][0]
			boolean ^= True
			self.ledStateList[Index][0] = boolean
		else:
			self.ledStateList[Index][0] = state
		self.ledStateList[Index][1] = curX
		self.ledStateList[Index][2] = curY


	def applyValues(self):
			for i in self.parseList:
				x = []
				y = []
				state = []
				for a in range(i[1], i[3] + 1):
					for b in range(i[2], i[4] + 1):
						x.append(a)
						y.append(b)
						state.append(i[0])

				for i in range(len(x)):
					self.changeState(x[i],y[i],state[i])
				# return [len(x), len(y), len(state)]

	def getResult(self):

		x = []
		y = []
		counter = 0
		for i, data in enumerate(self.ledStateList):
			if data[0] == True:
				counter = counter + 1
				x.append(data[1])
				y.append(data[2])
		return counter

if __name__ == '__main__':
	a = LedSwitcher(sys.argv[1])
	a.parseFile()
	a.getSize()
	a.getParseLines()
	a.applyValues()
	print(a.getResult())
