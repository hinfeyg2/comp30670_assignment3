
class LedSwitcher:

	def __init__(self, filename):
		self.filename = filename

	def parseFile(self):
		parseList = []
		with open(self.filename) as f:
			for line in f:
				parseList.append(line)
		return parseList