class gameBoard:

	characterList = []
	selectedCharacter = 0 

	def __init__(self, selectedCharacter):
		populateList()
		self.selectedCharacter = selectedCharacter

	def makeGuess(character):
		if(selectedCharacter == character):
			return true
		return false 

	def askQ(attribute):
		for i in range(0, 23):
			if(not characterList[i].hasAttribute(attribute) && characterList[i].isActive()):
				charactersList[i] = charactersList[i].toggleActive()

