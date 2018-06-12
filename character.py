class Character:
	
	name = ''
	female = False
	hat = False
	glasses = False
	beard = False
	mustache = False
	cheeks = False
	smile = False
	hairColor = '' 
	isActive = True

	def __init__(self, name, female, hat, glasses, beard, mustache, cheeks, smile, hairColor):
		self.name = name
		self.female = female
		self.hat = hat
		self.glasses = glasses
		self.beard = beard
		self.mustache = mustache
		self.cheeks = cheeks
		self.smile = smile
		self.hairColor = hairColor
		self.isActive = True 

	def toggleActive():
		isActive = not isActive

	def isActive():
		return isActive

	def hasAttribute(attribute):
		if(attribute.equals('female')): 
			return hat 
		if(attribute.equals('hat')): 
			return hat 
