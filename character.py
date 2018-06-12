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

	def printCharacter():
		print("This character's name is: ", name)
		print("Their attributes are as follows:")
		print("\t", ("Female" if isFemale else "Male"))
		print("\t", ("Has a hat" if hasHat else "Is un-hatted"))
		print("\t", ("Has glasses" if hasGlasses else "Has good vision"))
		print("\t", ("Has a beard" if hasBeard else "Has a clean chin"))
		print("\t", ("Has a mustache" if hasMustache else "No fur under their nose"))
		print("\t", ("Has red cheeks" if hasRosyCheeks else "Doesn't look embarrased"))
		print("\t", ("Looks happy" if isSmiling else "Looks like a sad sack of shit"))
		print("\t", ("Has a chrome dome" if isBald else "Has a shaggy head of hair"))