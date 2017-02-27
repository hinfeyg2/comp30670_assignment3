import matplotlib.pyplot as plt

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
		It returns a list with each line in that file. It avoids empty lines."""
		
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
			lineSplitSpaceList = self.parseList[i].split(" ")
			if lineSplitSpaceList[0] == 'turn' and lineSplitSpaceList[1] == 'on':

				xStart = lineSplitSpaceList[2].split(",")[0]
				yStart = lineSplitSpaceList[2].split(",")[1]
				xEnd = lineSplitSpaceList[4].split(",")[0]
				yEnd = lineSplitSpaceList[4].split(",")[1]
				self.parseList[i] = [True, xStart, yStart, xEnd, yEnd]

			elif lineSplitSpaceList[0] == 'turn' and lineSplitSpaceList[1] == 'off':
				xStart = lineSplitSpaceList[2].split(",")[0]
				yStart = lineSplitSpaceList[2].split(",")[1]
				xEnd = lineSplitSpaceList[4].split(",")[0]
				yEnd = lineSplitSpaceList[4].split(",")[1]
				self.parseList[i] = [False, xStart, yStart, xEnd, yEnd]

			elif lineSplitSpaceList[0] == 'switch':
				xStart = lineSplitSpaceList[1].split(",")[0]
				yStart = lineSplitSpaceList[1].split(",")[1]
				xEnd = lineSplitSpaceList[3].split(",")[0]
				yEnd = lineSplitSpaceList[3].split(",")[1]
				self.parseList[i] = [None, xStart, yStart, xEnd, yEnd]

		return self.parseList

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
			for a in range(int(i[1]), int(i[3]) + 1):
				for b in range(int(i[2]), int(i[4]) + 1):
					x.append(a)
					y.append(b)
					state.append(i[0])

			for i in range(len(x)):
				self.changeState(x[i],y[i],state[i])
			# return [len(x), len(y), len(state)]
