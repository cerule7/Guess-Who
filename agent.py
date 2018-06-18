from player import Player
from numpy import random

class Agent(Player):

	gameboard = ''
	score = 0 
	name = 'Skynet'
	selectedCharacter = 0

	def __init__(self, gameboard, selectedCharacter):
		self.gameboard = gameboard
		self.selectedCharacter = selectedCharacter
	
	# Makes a random choice
	# 24 < choice > -1 for random character
	# 40 < choice > 23 for random trait
	def guessRandom(self):
		choice = -1
		
		action = self.chooseRandom()
		
		if action == "trait":
			choice = random.randint(24, 40)
		else:
			choice = random.randint(0, 24)
		
		return choice
	
	# Makes a random number to make a binary choice 
	def chooseRandom(self):
		action = ""
		
		if random.randint(0, 2) == 1:
			action = "trait"
		else:
			action = "character"
		
		return action


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