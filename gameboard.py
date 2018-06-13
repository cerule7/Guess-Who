from character import Character 

class gameBoard:

	characterList = []
	selectedCharacter = 0 

	def populateList():
		characterList = []
		myFile = open("characterList.txt", "r")
		for j in range(24):
			
			line = myFile.readline()
			line.rstrip()
			name = line

			line = myFile.readline()
			line.rstrip()
			isFemale = line

			line = myFile.readline()
			line.rstrip()
			hasHat = line

			line = myFile.readline()
			line.rstrip()
			hasGlasses = line

			line = myFile.readline()
			line.rstrip()
			hasBeard = line

			line = myFile.readline()
			line.rstrip()
			hasMustache = line

			line = myFile.readline()
			line.rstrip()
			hasRosyCheeks = line

			line = myFile.readline()
			line.rstrip()
			isSmiling = line

			line = myFile.readline()
			line.rstrip()
			isBald = line

			line = myFile.readline()
			line.rstrip()
			hairColor = line

			characterList.append(Character(name, isFemale, hasHat, hasGlasses, hasBeard, hasMustache, hasRosyCheeks, isSmiling, isBald, hairColor))
		return characterList

	characterList = populateList()

	def __init__(self, selectedCharacter):
		self.selectedCharacter = selectedCharacter

	def getBoard(self):
		return self

	def getSelected(self):
		return self.selectedCharacter

	def getCharacter(self, num):
		return self.characterList[num]

	def getCharacterList(self):
		return self.characterList

	def makeGuess(character):
		if(selectedCharacter == character):
			return true
		return false 

	def askQ(self, attribute, otherBoard):
		if(attribute == 'hairColor'):
			attribute = input("Which hair color?")
		#if the other player's selected character DOES have the attribute, flip over ones that don't
		guess = bool(self.characterList[otherBoard.getSelected()].hasAttribute(attribute))
		if guess:
			for i in range(0, 24):
				hasAttribute = bool(self.characterList[i].hasAttribute(attribute))
				if bool(hasAttribute is False):
					print("FLIPPED " + self.characterList[i].getName())
					self.characterList[i].toggleActive()
		else: 
			for i in range(0, 24):
				hasAttribute = bool(self.characterList[i].hasAttribute(attribute))
				if bool(hasAttribute is True):
					print("FLIPPED " + self.characterList[i].getName())
					self.characterList[i].toggleActive()
		return self.characterList

	def updateList(self, list):
		self.characterList = list

	def printBoard(self):
		for i in range(0, len(self.characterList)):
			print(self.characterList[i].getName() + " " + str(self.characterList[i].isitActive())  + "\n")
