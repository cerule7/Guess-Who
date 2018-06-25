class Player:

	gameboard = ''
	score = 0 
	name = ''
	selectedCharacter = 0
	binaryPositions = [0, 23] #left, right

	def __init__(self, name, gameboard, selectedCharacter):
		self.gameboard = gameboard
		self.name = name
		self.selectedCharacter = selectedCharacter
		self.binaryPositions = [0, 23]

	def getBinaryPositions(self):
		return self.binaryPositions

	def setBinaryPositions(self, newBin):
		self.binaryPositions = newBin 

	def getName(self):
		return self.name

	def getSelected(self):
		return self.selectedCharacter

	def getBoard(self):
		return self.gameboard

	def setBoard(self, board):
		self.gameboard = board

	def setScore(self, score):
		self.score = score

	def getScore(self):
		return self.score

	def setSelected(num):
		selectedCharacter = num 