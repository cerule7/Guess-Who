from player import Player
from numpy import random

class Agent(Player):

	gameboard = ''
	score = 0 
	name = 'Randbot: '
	selectedCharacter = 0
	listGuesses = 0
	binaryPositions = [0, 23] #left, right

	def __init__(self, name, gameboard, selectedCharacter):
		self.gameboard = gameboard
		self.selectedCharacter = selectedCharacter
		self.name += name
		self.listGuesses = []
		self.binaryPositions = [0, 23] 
	
	# Makes a random choice
	# 24 < choice > -1 for random character
	# 40 < choice > 23 for random trait
	def guessRandom(self):
		choice = -1
		
		action = self.chooseRandom()
		
		if action == "trait":
			choice = random.randint(24, 40)
			
			newChoice = False
			if choice not in self.listGuesses:
				newChoice = True
				
			while not newChoice:
				choice = random.randint(24, 40)
				
				if choice not in self.listGuesses:
					newChoice = True
			
		else:
			choice = random.randint(0, 24)
			
			newChoice = False
			if choice not in self.listGuesses:
				newChoice = True
				
			while not newChoice:
				choice = random.randint(0, 24)
				
				if choice not in self.listGuesses:
					newChoice = True
		
		self.listGuesses.append(choice)
		return choice
	
	# Makes a random number to make a binary choice 
	def chooseRandom(self):
		return "trait"
# 		action = ""
#    		
# 		if random.randint(0, 2) == 1:
# 			action = "trait"
# 		else:
# 			action = "character"
#    		
# 		return action


#===============================================================================
#	Unmodified methods
#
#	def getBinaryPositions(self):
#		return self.binaryPositions
#
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