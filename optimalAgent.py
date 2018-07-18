from gym.envs.guesswho.player import Player
import math


class OptimalAgent(Player):
    gameboard = ''
    score = 0
    name = 'GT_Agent: '
    selectedCharacter = 0
    binaryPositions = [0, 23]  # left, right

    def __init__(self, name, gameboard, selectedCharacter):
        self.gameboard = gameboard
        self.selectedCharacter = selectedCharacter
        self.name += name
        self.binaryPositions = [0, 23]

    def getRiskiestGuess(self, traitList):
        lowestTrait = 0

        for i in range(19):
            if int(traitList[i]) != 0:
                if int(traitList[lowestTrait]) == 0:
                    lowestTrait = i
                else:
                    if int(traitList[i]) < int(traitList[lowestTrait]):
                        lowestTrait = i

        return lowestTrait

    def compileTraitList(self):
        listTraits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for character in self.gameboard.characterList:
            if character.isitActive():
                listTraits[0] += int(eval(character.isFemale))
                listTraits[1] += int(eval(character.hasHat))
                listTraits[2] += int(eval(character.hasGlasses))
                listTraits[3] += int(eval(character.hasBeard))
                listTraits[4] += int(eval(character.hasMustache))
                listTraits[5] += int(eval(character.hasRosyCheeks))
                listTraits[6] += int(eval(character.isSmiling))
                listTraits[7] += int(eval(character.isBald))
                listTraits[8] += int(eval(character.hasBlueEyes))
                listTraits[9] += int(eval(character.hasBigNose))
                listTraits[10] += int(eval(character.hasBigMouth))
                listTraits[11] += int(eval(character.hasEarrings))
                listTraits[12] += int(eval(character.hasButtchin))
                listTraits[14] += int(bool(character.hairColor == 'black'))
                listTraits[15] += int(bool(character.hairColor == 'red'))
                listTraits[16] += int(bool(character.hairColor == 'white'))
                listTraits[17] += int(bool(character.hairColor == 'blonde'))
                listTraits[18] += int(bool(character.hairColor == 'brown'))

        listTraits[13] = 30

        # Trait debug
        # print("\n\n\n\nLIST TRAITS DEBUG:")
        # for i in range (0,19):
        #     print("listTraits[" + str(i) + "] = " + str(listTraits[i]) + "\n")
        # print("\n\n\n\n")

        return listTraits

    def makeOptimalGuess(self, agentNum, opponentNum):
        # 2**k = 2**(log2(n-1))
        if agentNum - 1 > 0:
            k = math.floor(math.log((agentNum - 1), 2))
            # "in the weeds"
            if 2 ** (k + 1) <= opponentNum and 2 ** k <= agentNum and agentNum <= 2 ** (k + 1):
                return self.getRiskiestGuess(self.compileTraitList())
            else:
                return 13
        else:
            return 13

# ===============================================================================
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
# ===============================================================================
