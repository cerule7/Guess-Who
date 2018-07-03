from gym.envs.guesswho.player import Player

class OptimalAgent(Player):

	gameboard = ''
	score = 0 
	name = 'GT_Agent: '
	selectedCharacter = 0
	binaryPositions = [0, 23] #left, right

	def __init__(self, name, gameboard, selectedCharacter):
		self.gameboard = gameboard
		self.selectedCharacter = selectedCharacter
		self.name += name
		self.binaryPositions = [0, 23] 
	
	def makeOptimalGuess(self, turnNum, agentNum, opponentNum):
		# Risky case
		if(agentNum > 2**(turnNum + 1) and (opponentNum > 2**(turnNum) and opponentNum < 2**(turnNum + 1))):
			return getRiskiestGuess(self, compileTraitList(self))
		# Safe Case
		elif (opponentNum > 2**(turnNum) and (agentNum > 2**(turnNum) and agentNum < 2**(turnNum + 1))):
			return 13
		# Debug case, shouldn't hit this
		else:
			return -100
			
	def getRiskiestGuess(self, traitList):
		lowestTrait = 0
		
		for i in range(19):
			
			if int(traitList[i]) < int(traitList[lowestTrait]):
				lowestTrait = i
	
		return lowestTrait
	
	def compileTraitList(self):
		listTraits = [19]
		listTraits[13] = 30
		
		for character in self.gameboard.characterList:
			listTraits[0] += int(character.isFemale)
			listTraits[1] += int(character.hasHat)
			listTraits[2] += int(character.hasGlasses)
			listTraits[3] += int(character.hasBeard)
			listTraits[4] += int(character.hasMustache)
			listTraits[5] += int(character.hasRosyCheeks)
			listTraits[6] += int(character.isSmiling)
			listTraits[7] += int(character.isBald)
			listTraits[8] += int(character.hasBlueEyes)
			listTraits[9] += int(character.hasBigNose)
			listTraits[10] += int(character.hasBigMouth)
			listTraits[11] += int(character.hasEarrings)
			listTraits[12] += int(character.hasButtchin)
			listTraits[14] += int(character.hairColor == 'black') 
			listTraits[15] += int(character.hairColor == 'red')
			listTraits[16] += int(character.hairColor == 'white')
			listTraits[17] += int(character.hairColor == 'blonde')
			listTraits[18] += int(character.hairColor == 'brown')


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