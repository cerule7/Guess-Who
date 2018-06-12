class Player:

	gameboard = ''
	score = 0 
	name = ''
	selectedCharacter = 0

	def __init__(self, name, gameboard, selectedCharacter):
		self.gameboard = gameboard
		self.name = name
		self.selectedCharacter = selectedCharacter

	def getName(self):
		return self.name

	def getSelected():
		return self.selectedCharacter

	def getBoard(self):
		return self.gameboard

	def setScore(self, score):
		self.score = score

	def getScore(self):
		return self.score

	def setSelected(num):
		selectedCharacter = num 