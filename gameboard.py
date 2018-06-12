class gameBoard:

	characterList = []
	selectedCharacter = 0 

	def __init__(self, selectedCharacter):
		populateList()
		self.selected
		Character = selectedCharacter

	def getSelected():
		return selectedCharacter

	def getCharacter(num):
		return characterList[num]

	def makeGuess(character):
		if(selectedCharacter == character):
			return true
		return false 

	def askQ(attribute, otherBoard):
		if(attribute.equals('hairColor')):
			attribute = input("Which hair color?")
		if(otherBoard.getSelected().hasAttribute()):
			for i in range(0, 23):
				if(not characterList[i].hasAttribute(attribute) && characterList[i].isActive()):
					characterList[i] = characterList[i].toggleActive()
		else: 
			for i in range(0, 23):
				if(characterList[i].hasAttribute(attribute) && characterList[i].isActive()):
					characterList[i] = characterList[i].toggleActive()

	def printBoard():
		for i in range(0, 23):
			print(characterList[i].getName() + " " + characterList[i].isActive()  + "\n")


	def populateList():

		myFile open ("characterList.txt", "r")
		for j in range(24):
			
			line = myFile.next()
			line.rstrip()
			name = line

			line = myFile.next()
			line.rstrip()
			isFemale = line

			line = myFile.next()
			line.rstrip()
			hasHat = line

			line = myFile.next()
			line.rstrip()
			hasGlasses = line

			line = myFile.next()
			line.rstrip()
			hasBeard = line

			line = myFile.next()
			line.rstrip()
			hasMustache = line

			line = myFile.next()
			line.rstrip()
			hasRosyCheeks = line

			line = myFile.next()
			line.rstrip()
			isSmiling = line

			line = myFile.next()
			line.rstrip()
			isBald = line

			line = myFile.next()
			line.rstrip()
			hairColor = line

			characterList[j] = new Character(self, name, isFemale, hasHat, hasGlasses, hasBeard, hasMustache, hasRosyCheeks, isSmiling, isBald, hairColor)


