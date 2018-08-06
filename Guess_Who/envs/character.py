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
    hasBlueEyes = False
    hasBigNose = False
    hasBigMouth = False
    hasEarrings = False
    hasButtchin = False
    hairColor = ''
    isActive = True

    def __init__(self, name, isFemale, hasHat, hasGlasses, hasBeard, hasMustache, hasRosyCheeks, isSmiling, isBald,
                 hasBlueEyes, hasBigNose, hasBigMouth, hasEarrings, hasButtchin, hairColor):
        self.name = str(name)
        self.isFemale = isFemale
        self.hasHat = hasHat
        self.hasGlasses = hasGlasses
        self.hasBeard = hasBeard
        self.hasMustache = hasMustache
        self.hasRosyCheeks = hasRosyCheeks
        self.isSmiling = isSmiling
        self.isBald = isBald
        self.hasBlueEyes = hasBlueEyes
        self.hasBigNose = hasBigNose
        self.hasBigMouth = hasBigMouth
        self.hasEarrings = hasEarrings
        self.hasButtchin = hasButtchin
        self.hairColor = hairColor
        self.isActive = True

    def getName(self):
        return str(self.name)

    def isitActive(self):
        return self.isActive

    def setInactive(self):
        self.isActive = False

    def hasAttribute(self, attribute):
        if (attribute == 'isFemale'):
            return eval(self.isFemale)
        if (attribute == 'hasHat'):
            return eval(self.hasHat)
        if (attribute == 'hasGlasses'):
            return eval(self.hasGlasses)
        if (attribute == 'hasBeard'):
            return eval(self.hasBeard)
        if (attribute == 'hasMustache'):
            return eval(self.hasMustache)
        if (attribute == 'hasRosyCheeks'):
            return eval(self.hasRosyCheeks)
        if (attribute == 'isSmiling'):
            return eval(self.isSmiling)
        if (attribute == 'isBald'):
            return eval(self.isBald)
        if (attribute == 'hasBlueEyes'):
            return eval(self.hasBlueEyes)
        if (attribute == 'hasBigNose'):
            return eval(self.hasBigNose)
        if (attribute == 'hasBigMouth'):
            return eval(self.hasBigMouth)
        if (attribute == 'hasEarrings'):
            return eval(self.hasEarrings)
        if (attribute == 'hasButtchin'):
            return eval(self.hasButtchin)
        return (self.hairColor == attribute)

    # Debug print of all characters attributes, not updated with the 5 new attributes
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
        print("\t", "Has blue eyes: ", self.hasBlueEyes)
        print("\t", "Has a big schnoz: ", self.hasBigNose)
        print("\t", "Has a big gob: ", self.hasBigMouth)
        print("\t", "Has some dangly earrings: ", self.hasEarrings)
        print("\t", "Has a chin like an ass: ", self.hasButtchin)
        print("\t", "Hair color: ", self.hairColor)
