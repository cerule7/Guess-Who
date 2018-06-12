class Character:
	
	name = ''
	isFemale = False
	hasHat = False
	hasGlasses = False
	hasBeard = False
	hasMustache = False
	hasRosyCheeks = False
	isSmiling = False
	isBald = False
	hairColor = '' 
	isActive = True

	def __init__(self, name, isFemale, hasHat, hasGlasses, hasBeard, hasMustache, hasRosyCheeks, isSmiling, isBald, hairColor):
		self.name = name
		self.isFemale = isFemale
		self.hasHat = hasHat
		self.hasGlasses = hasGlasses
		self.hasBeard = hasBeard
		self.hasMustache = hasMustache
		self.hasRosyCheeks = hasRosyCheeks
		self.isSmiling = isSmiling
		self.isBald = isBald
		self.hairColor = hairColor
		self.isActive = True 

	def getName(self):
		return self.name

	def isitActive(self):
		return self.isActive

	def toggleActive():
		isActive = not isActive

	def hasAttribute(self, attribute):
		if(attribute == 'isFemale'): 
			return self.isFemale 
		if(attribute == 'hasHat'): 
			return self.hasHat 
		if(attribute == 'hasGlasses'): 
			return self.hasGlasses 
		if(attribute == 'hasBeard'): 
			return self.hasBeard 
		if(attribute == 'hasMustache'): 
			return self.hasMustache 
		if(attribute == 'hasRosyCheeks'): 
			return self.hasRosyCheeks 
		if(attribute == 'isSmiling'): 
			return self.isSmiling 
		if(attribute == 'isBald'): 
			return self.isBald 
		return (self.hairColor == attribute)

	def printCharacter(self):
		print("This character's name is: ", self.name)
		print("Their attributes are as follows:")
		print("\t", "Female: ", self.isFemale)
		print("\t", "Has a hat: ", self.hasHat)
		print("\t", "Has glasses: ", self.hasGlasses)
		print("\t", "Has a beard: ", self.hasBeard)
		print("\t", "Has a mustache: ", self.hasMustache)
		print("\t", "Has red cheeks: ", self.hasRosyCheeks)
		print("\t", "Looks happy: ", self.isSmiling)
		print("\t", "Has a chrome dome: ", self.isBald)