import matplotlib.pyplot as plt

class LedSwitcher:

	def __init__(self, filename):
		self.filename = filename
		self.parseList = []
		self.switchSize = 0
		self.ledStateList = []

	def parseFile(self):
		
		with open(self.filename) as f:
			for line in f:
				if len(line) > 1:
					self.parseList.append(line.strip())
		print(len(self.parseList), "parseList")
		return self.parseList

	def getSize(self):
		if len(self.parseList) == 0:
			return "List Empty"
		else:
			self.switchSize = int(self.parseList[0])
			for x in range(0, self.switchSize):
				for y in range(0, self.switchSize):
					self.ledStateList.append([False, x, y])
		return self.switchSize

	def getParseLines(self):
		
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



