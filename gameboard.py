from character import Character 

class gameBoard:

	characterList = []
	selectedCharacter = 0 
	totFlips = 0

	def __init__(self, selectedCharacter):
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
			hasBlueEyes = line
			
			line = myFile.readline()
			line = line.strip()
			hasBigNose = line
			
			line = myFile.readline()
			line = line.strip()
			hasBigMouth = line
			
			line = myFile.readline()
			line = line.strip()
			hasEarrings = line
			
			line = myFile.readline()
			line = line.strip()
			hasButtchin = line

			line = myFile.readline()
			line = line.strip()
			hairColor = line

			characterList.append(Character(name, isFemale, hasHat, hasGlasses, hasBeard, hasMustache, hasRosyCheeks, isSmiling, isBald, hasBlueEyes, hasBigNose, hasBigMouth, hasEarrings, hasButtchin, hairColor))
		self.characterList = characterList
		self.selectedCharacter = selectedCharacter

	def getBoard(self):
		return self

	def numberActive(self):
		j = 0
		for i in range(0, 24):
			if(self.characterList[i].isitActive()):
				j += 1
		return int(j)

	def getSelected(self):
		return self.selectedCharacter

	def getCharacter(self, num):
		return self.characterList[num]

	def getCharacterList(self):
		return self.characterList

	def askQ(self, attribute, otherBoard):
		#if the other player's selected character DOES have the attribute, flip over ones that don't
		guess = bool(self.characterList[otherBoard.getSelected()].hasAttribute(attribute))
		numFlipped = 0 
		if guess:
			for i in range(0, 24):
				hasAttribute = bool(self.characterList[i].hasAttribute(attribute))
				if bool(hasAttribute is False) and self.characterList[i].isitActive():
					print("FLIPPED " + self.characterList[i].getName())
					self.characterList[i].toggleActive()
					numFlipped += 1
		else: 
			for i in range(0, 24):
				hasAttribute = bool(self.characterList[i].hasAttribute(attribute))
				if bool(hasAttribute is True) and self.characterList[i].isitActive():
					print("FLIPPED " + self.characterList[i].getName())
					self.characterList[i].toggleActive()
					numFlipped += 1
		return self.characterList, numFlipped
	
	def binarySearch(self, binaryPositions, otherBoard):
		numFlipped = 0 
		m = int((binaryPositions[0] + binaryPositions[1]) / 2)
		selPos = int(otherBoard.getSelected())
		print("GUESS " + str(m) + " SEL " + str(selPos))
		if m == selPos:
			for i in range(0, 24):
				if i != selPos and self.characterList[i].isitActive():
					print("FLIPPED " + self.characterList[i].getName())
					self.characterList[i].toggleActive()
					numFlipped += 1
		elif m > selPos:
			for i in range(m, 24):
				if self.characterList[i].isitActive():
					print("FLIPPED " + self.characterList[i].getName())
					self.characterList[i].toggleActive()
					numFlipped += 1
			binaryPositions[1] = m - 1
		else:
			for i in range(0, m):
				if self.characterList[i].isitActive():
					print("FLIPPED " + self.characterList[i].getName())
					self.characterList[i].toggleActive()
					numFlipped += 1
			binaryPositions[0] = m + 1
		return binaryPositions, self.characterList, numFlipped

	# Compares the total number of flips with the last recorded number
	# May be obsolete 
	def flippedLast(self):
		currentTot = 0
		for char in self.characterList:
			currentTot += not char.isActive
		
		currentTot -= self.totFlips
		self.totFlips += currentTot
		
		return currentTot
	
	def getActiveCharacters(self):
		activeList = []
		
		for character in self.characterList:
			if character.isActive == True:
				activeList.append(character)
				
		return activeList

	def askHairColor(self, i, otherBoard):
		color = ''
		if i == 38:
			color = 'black'
		if i == 39:
			color = 'red'
		if i == 40:
			color = 'white'
		if i == 41:
			color == 'blonde'
		else:
			color == 'brown'
		return self.askQ(color, otherBoard)

	def updateList(self, list):
		self.characterList = list

	def printBoard(self):
		for i in range(0, len(self.characterList)):
			print(self.characterList[i].getName() + " " + str(self.characterList[i].isitActive())  + "\n")