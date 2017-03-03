import sys
from urllib.request import urlopen

class LedSwitcher:
	
	def __init__(self, filename):

		self.filename = filename
		# Will be set to how big the size of the LED array is.
		self.switchSize = 0
		# Will contain a list of each led and its associated state.
		self.ledStateList = []


	def parseFile(self):
		"""This method opens the file containing the assigned data input.
		It returns a list with each line in that file or url. It avoids empty lines."""
		
		count = 0

		# open from a url.
		if self.filename[:4] == "http":
			for line in urlopen(self.filename):
				line = line.decode("utf-8")
				line = line.strip()
				if count == 0:
					self.switchSize = int(line)
					self.createTemplate()
					count = count + 1
				elif len(line) > 1:
					self.applyValues(self.parseEachLine(line))

		# else open from file.
		else:
			with open(self.filename) as f:
				self.switchSize = int(f.readline())
				self.createTemplate()
				for line in f:
					if len(line) > 1:
						self.applyValues(self.parseEachLine(line))
			f.closed

	def createTemplate(self):
		"""This method creates a 2d list of the current input size."""
		
		for x in range(0, self.switchSize):
			for y in range(0, self.switchSize):
				self.ledStateList.append([False])


	def parseEachLine(self, x):
		"""This file parses the data from each line and returns a list with the results."""
		
		# this strips white space from the front of each line.
		x = x.strip()

		# this section solves the instance of " ," in the input_assign3d file.
		if ", " in x:
			x = x.replace(", ", ",")
		elif " ," in x:
			x = x.replace(" ,", ",")

		# this splits by space.
		lineSplitSpaceList = x.split(" ")

		if lineSplitSpaceList[0] == "turn" and lineSplitSpaceList[1] == "on":

			xStart = lineSplitSpaceList[2].split(",")[0].strip()
			yStart = lineSplitSpaceList[2].split(",")[1].strip()
			xEnd = lineSplitSpaceList[4].split(",")[0].strip()
			yEnd = lineSplitSpaceList[4].split(",")[1].strip()
			# if and int is over the input size or under zero return the int to those values.
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

		# the method must return somthing!
		return ["BadFormat"]


	def changeState(self, curX, curY, state):
		"""a method for changing the state of the ledStateList with and an input position and state"""

		# create the index for searching the ledStateList.
		Index = (curX * self.switchSize) + curY
		
		# None means switch
		if state == None:
			boolean = self.ledStateList[Index][0]
			boolean ^= True
			self.ledStateList[Index][0] = boolean
		else:
			self.ledStateList[Index][0] = state

		return self.ledStateList


	def applyValues(self, lineItem):
		"""Apply the valus in the parseList to the ledStateList"""

		if lineItem[0] != "BadFormat":
			counter = 0
			# iterate over the values in each line.
			for a in range(lineItem[1], lineItem[3] + 1):
				for b in range(lineItem[2], lineItem[4] + 1):
					self.changeState(a, b, lineItem[0])
					counter = counter + 1
			return(counter)


	def getResult(self):
		"""Returns the result."""

		counter = 0
		for i in self.ledStateList:
			if i[0] == True:
				counter = counter + 1
		print("")
		print("Input File", self.filename)
		print("Result", counter)
		print("")
		return counter

def main():
	"""This function is used when running the setup.py entry points."""

	a = LedSwitcher(sys.argv[1])
	a.parseFile()
	print(a.getResult())

if __name__ == '__main__':
	"""Run this if its the root python file."""

	a = LedSwitcher(sys.argv[1])
	a.parseFile()
	print(a.getResult())