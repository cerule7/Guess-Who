class gameBoard:

	characterList = []
	selectedCharacter = 0 

	def __init__(self, selectedCharacter):
		populateList()
		self.selected
		Character = selectedCharacter

	def getCharacter(num):
		return characterList[num]

	def makeGuess(character):
		if(selectedCharacter == character):
			return true
		return false 

	def askQ(attribute):
		for i in range(0, 23):
			if(not characterList[i].hasAttribute(attribute) && characterList[i].isActive()):
				characterList[i] = characterList[i].toggleActive()

	def printBoard():
		for i in range(0, 23):
			print(characterList[i].getName() + " " + characterList[i].isActive()  + "\n")


	def populateList():
		with open ("/Users/it/Desktop/Classbook/masterClassList.txt", "r") as myfile:
			for j in range(0, 23):
				for i in range(0, 8):
					for line in myfile:

			characterList[j] = new Character(self, name, isFemale, hasHat, hasGlasses, hasBeard, hasMustache, hasRosyCheeks, isSmiling, isBald, hairColor)