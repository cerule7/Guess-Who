class Player:

	gameboard = ''
	score = 0 
	name = ''
	selectedCharacter = 0

	def __init__(self, name, gameboard, selectedCharacter):
		self.gameboard = gameboard
		self.name = name
		self.selectedCharacter = selectedCharacter

	def getName():
		return name

	def getSelected():
		return selectedCharacter

	def getBoard():
		return gameboard

	def setScore(score):
		self.score = score

	def setSelected(num):
		selectedCharacter = num 