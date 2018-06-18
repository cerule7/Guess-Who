from character import Character 

class gameBoard:

	characterList = []
	selectedCharacter = 0 
	totFlips = 0

	def populateList():
		characterList = []
		myFile = open("characterList.txt", "r")
		for j in range(24):
			
			line = myFile.readline()
			line = line.strip()
			name = line

			line = myFile.readline()
			line = line.strip()
			isFemale = line

			line = myFile.readline()
			line = line.strip()
			hasHat = line

			line = myFile.readline()
			line = line.strip()
			hasGlasses = line

			line = myFile.readline()
			line = line.strip()
			hasBeard = line

			line = myFile.readline()
			line = line.strip()
			hasMustache = line

			line = myFile.readline()
			line = line.strip()
			hasRosyCheeks = line

			line = myFile.readline()
			line = line.strip()
			isSmiling = line

			line = myFile.readline()
			line = line.strip()
			isBald = line

			line = myFile.readline()
			line = line.strip()
			hairColor = line

			characterList.append(Character(name, isFemale, hasHat, hasGlasses, hasBeard, hasMustache, hasRosyCheeks, isSmiling, isBald, hairColor))
		return characterList

	characterList = populateList()
	for char in characterList:
		char.printCharacter()

	def __init__(self, selectedCharacter):
		self.selectedCharacter = selectedCharacter

	def getBoard(self):
		return self

	def isOneLeft(self):
		j = 24
		for i in range(0,24):
			if(self.characterList[i].isitActive()):
				j -= 1
		return bool(j == 1)

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
		#if the other player's selected character DOES have the attribute, flip over ones that don't
		guess = bool(self.characterList[otherBoard.getSelected()].hasAttribute(attribute))
		if guess:
			for i in range(0, 24):
				hasAttribute = bool(self.characterList[i].hasAttribute(attribute))
				if bool(hasAttribute is False) and self.characterList[i].isitActive():
					print("FLIPPED " + self.characterList[i].getName())
					self.characterList[i].toggleActive()
		else: 
			for i in range(0, 24):
				hasAttribute = bool(self.characterList[i].hasAttribute(attribute))
				if bool(hasAttribute is True) and self.characterList[i].isitActive():
					print("FLIPPED " + self.characterList[i].getName())
					self.characterList[i].toggleActive()
		return self.characterList
	
	# Compares the total number of flips with the last recorded number
	def flippedLast(self):
		currentTot = 0
		for char in self.characterList:
			currentTot += not char.isActive
		
		currentTot -= self.totFlips
		self.totFlips += currentTot
		
		return currentTot

	def askHairColor(self, i, otherBoard):
		color = ''
		if i == 35:
			color = 'black'
		if i == 36:
			color = 'red'
		if i == 37:
			color = 'white'
		if i == 38:
			color == 'blonde'
		else:
			color == 'brown'
		return self.askQ(color, otherBoard)

	def updateList(self, list):
		self.characterList = list

	def printBoard(self):
		for i in range(0, len(self.characterList)):
			print(self.characterList[i].getName() + " " + str(self.characterList[i].isitActive())  + "\n")
			
	# Allows for the reseting of a game board
	def resetBoard(self):
		self.selectedCharacter = 0
		self.totFlips = 0
		for character in self.characterList:
			character.isActive = True
			