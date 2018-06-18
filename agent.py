import player.py

class Agent(player.Player):

	gameboard = ''
	score = 0 
	name = 'Skynet'
	selectedCharacter = 0

	def __init__(self, gameboard, selectedCharacter):
		self.gameboard = gameboard
		self.selectedCharacter = selectedCharacter

#===============================================================================
#	Unmodified methods

# 	def getName(self):
# 		return self.name
# 
# 	def getSelected(self):
# 		return self.selectedCharacter
# 
# 	def getBoard(self):
# 		return self.gameboard
# 
# 	def setBoard(self, board):
# 		self.gameboard = board
# 
# 	def setScore(self, score):
# 		self.score = score
# 
# 	def getScore(self):
# 		return self.score
# 
# 	def setSelected(num):
# 		selectedCharacter = num 
#===============================================================================