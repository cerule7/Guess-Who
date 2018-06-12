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

	def getName():
		return name

	def isActive():
		return isActive

	def toggleActive():
		isActive = not isActive

	def hasAttribute(attribute):
		if(attribute.equals('isFemale')): 
			return isFemale 
		if(attribute.equals('hasHat')): 
			return hasHat 
		if(attribute.equals('hasGlasses')): 
			return hasGlasses 
		if(attribute.equals('hasBeard')): 
			return hasBeard 
		if(attribute.equals('hasMustache')): 
			return hasMustache 
		if(attribute.equals('hasRosyCheeks')): 
			return hasRosyCheeks 
		if(attribute.equals('isSmiling')): 
			return isSmiling 
		if(attribute.equals('isBald')): 
			return isBald 
		return hairColor.equals(attribute)
